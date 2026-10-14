"""SHA-pinned N12 V3 detector/alignment/recognizer algorithm used for evaluator checks.

Weights must be provided by user from private Drive; never download or silently
replace a missing checkpoint. CPU-only ONNX execution for deterministic replay.
"""
from __future__ import annotations
import hashlib
from pathlib import Path
import numpy as np

EXPECTED_WEIGHTS_SHA256 = {
    "detector": "5838f7fe053675b1c7a08b633df49e7af5495cee0493c7dcf6697200b85b5b91",
    "arcface": "4c06341c33c2ca1f86781dab0e829f88ad5b64be9fba56e56bc9ebdefc619e43",
    "auraface": "a7933ea5330113b01c9b60351d8f4c33003f145d8470ac5f0e52ee2effe25c60",
}

def load_frozen_models(paths: dict[str, str | Path]):
    """Load EXACT sha256-matched weights with N12 SCRFD parameters."""
    from insightface.model_zoo import get_model
    from face_privacy.provenance import file_sha256
    missing = set(EXPECTED_WEIGHTS_SHA256) - set(paths)
    if missing:
        raise ValueError(f"Missing frozen ONNX weights: {sorted(missing)}")
    for name, expected in EXPECTED_WEIGHTS_SHA256.items():
        if file_sha256(paths[name]) != expected:
            raise ValueError(f"Frozen {name} weight sha256 mismatch")
    detector = get_model(str(paths["detector"]), providers=["CPUExecutionProvider"])
    # InsightFace may expose the SHA-pinned detector ONNX with a RetinaFace
    # Python wrapper. Verify the exact file hash and detection interface,
    # rather than incorrectly requiring one wrapper class name.
    if not callable(getattr(detector, "detect", None)):
        raise TypeError("The SHA-pinned detector must expose detect()")
    detector.prepare(ctx_id=-1, input_size=(640, 640), det_thresh=0.1)
    recognizers = {}
    for name in ("arcface", "auraface"):
        model = get_model(str(paths[name]), providers=["CPUExecutionProvider"])
        model.prepare(ctx_id=-1)
        recognizers[name] = model
    return detector, recognizers

def embeddings(image_path, detector, recognizers):
    """Match N12 V3: RGB 512² => centered 320² on 640² => 112² aligned."""
    import cv2
    from PIL import Image
    from insightface.utils import face_align
    rgb = np.asarray(Image.open(image_path).convert("RGB"))
    if rgb.shape != (512, 512, 3):
        raise ValueError("N12 V3 expects exactly RGB 512 x 512")
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    canvas = np.zeros((640, 640, 3), dtype=np.uint8)
    canvas[160:480,160:480] = cv2.resize(bgr, (320,320), interpolation=cv2.INTER_AREA)
    boxes, landmark = detector.detect(canvas, max_num=0, metric="default")
    if not len(boxes):
        return {}, {"face_detected": False, "alignment_plausible": False}
    index = int(np.argmax(boxes[:,4]))
    box = np.asarray(boxes[index], dtype=np.float64)
    pts = (np.asarray(landmark[index], dtype=np.float64)-160)/0.625
    xy = (box[:4]-160)/0.625
    x1,y1,x2,y2=xy
    area=max(0,x2-x1)*max(0,y2-y1)
    intersection=max(0,min(512,x2)-max(0,x1))*max(0,min(512,y2)-max(0,y1))
    fraction=intersection/area if area>0 else 0.0
    plausible=bool(pts.shape==(5,2) and np.isfinite(pts).all()
                   and np.linalg.norm(pts[0]-pts[1])>=1 and fraction>=0.7)
    aligned=face_align.norm_crop(bgr,landmark=pts.astype(np.float32),image_size=112)
    plausible=bool(plausible and aligned.shape==(112,112,3) and aligned.dtype==np.uint8)
    scores={}
    for name,model in recognizers.items():
        arr=np.asarray(model.get_feat(aligned),dtype=np.float32).reshape(-1)
        norm=float(np.linalg.norm(arr))
        if plausible and arr.size==512 and np.isfinite(arr).all() and np.isfinite(norm) and norm>1e-10:
            scores[name]=arr/norm
    return scores, {"face_detected": True, "alignment_plausible": plausible}

def cosine_pairs(source, synthetic, detector, recognizers):
    """Return per-backend cosines (NaN on failure; never zero-fill)."""
    original, src_meta=embeddings(source,detector,recognizers)
    generated, dst_meta=embeddings(synthetic,detector,recognizers)
    result={}
    for name in ("arcface","auraface"):
        result[name+"_cosine"]=(float(np.dot(original[name],generated[name]))
                                if name in original and name in generated else float("nan"))
        result["pair_valid_"+name]=bool(name in original and name in generated)
    return {**result,"source_detection":src_meta,"output_detection":dst_meta}
