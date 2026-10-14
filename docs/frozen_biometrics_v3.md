# Frozen biometric evaluator: N12 V3

## Decision

**Technical evaluator selected and frozen:** use the full, unmodified RGB 512 x 512 image as input; convert RGB to BGR; resize the whole image to BGR 320 x 320 using OpenCV INTER_AREA; place at pixels [160:480,160:480] on a black 640 x 640 canvas. Run SHA-256 pinned SCRFD ONNX detector at input_size=(640,640), threshold 0.1, CPUExecutionProvider. Select highest-confidence detection, map five landmarks back to 512-image coordinates with (coordinate - 160)/0.625, and use InsightFace norm_crop(..., image_size=112) on the **original BGR image**. Extract normalized 512-dimensional embeddings with both frozen ArcFace and AuraFace ONNX recognizers; report cosine similarities for every source-output pair. Missing/invalid detection or embedding is missing data, never evidence of obfuscation.

**No YOLO crop precedes SCRFD in the frozen V3 evaluator**; the source face remains inside the complete image prior to geometric resizing. Prior N07 YOLO + 15% margin crop is not part of the final method.

Pinned recognizer hashes (SHA-256): SCRFD `5838f7fe053675b1c7a08b633df49e7af5495cee0493c7dcf6697200b85b5b91`; ArcFace `4c06341c33c2ca1f86781dab0e829f88ad5b64be9fba56e56bc9ebdefc619e43`; AuraFace `a7933ea5330113b01c9b60351d8f4c33003f145d8470ac5f0e52ee2effe25c60`. See [frozen Python implementation](../src/face_privacy/biometrics.py). CPU ONNX results were generated using `insightface==1.0.1`, `onnxruntime==1.19.2` and `opencv-python==4.11.0.86`.

## Prior technical comparison (executed, not proposed)

| Input to SCRFD | Detections / 14 developmental sources |
| --- | ---: |
| Full original image, `det_size=1024` | 6 |
| Full original image, `det_size=640` | 1 |
| Direct scaled original image 320 | 14 |
| Centered 320-in-640 (V3) | **14** |
| Centered content with 1024 canvas | 6 |

Executed N10 tested the five detector scale/canvas variants. The selection was based on the 14 development sources, including comparison against YOLO rectangles as **non-ground-truth diagnostic geometry**.

Executed N11 independently applied the frozen V3 method to all 120 N07 originals: **120/120 detections, 120/120 technically plausible landmark/alignment checks, 120/120 finite ArcFace embeddings, 120/120 finite AuraFace embeddings** (14 development + 106 held-out-from-scale-selection). Executed N12 reused frozen V3 on 600 existing source/synthetic pairs: **600/600 finite pair cosines for each evaluator**. No diffusion generation was performed. Source code executed in archival notebooks: [N10](https://github.com/menychtak/thesis_notes/blob/main/Notebooks/current/10_scrfd_scale_canvas_diagnostic.ipynb), [N11](https://github.com/menychtak/thesis_notes/blob/main/Notebooks/current/11_v3_biometric_alignment_validation.ipynb), [N12](https://github.com/menychtak/thesis_notes/blob/main/Notebooks/current/12_corrected_v3_biometric_privacy_reevaluation.ipynb).

## Interpretation boundaries

100% here is **technical extraction coverage**, not proof that every detected region is the intended face, that alignment is subjectively correct, or that cosine similarity is a calibrated re-identification probability. Full manual face/alignment acceptance remains pending; the N21/N22b screenshot QC is provisional and covers only 24 neutral-target pairs, not all 600. The selection on 14 development images must be disclosed when describing the method; do not claim the geometry choice was blind to all images. Freeze V3 for future reporting; do not tune it again in response to outcome differences without a separately pre-registered sensitivity study.

## Supervisor request #1 checklist

- 15% YOLO crop: removed from final biometric pipeline (not necessary); cannot infer the exact causal contribution of crop width alone from N10.
- `det_size`: tested multiple variants; froze `(640,640)` with centered 320 content.
- Direct full-size image: tested; the unmodified full 512 content is retained *before* resize+padding; simply calling the detector on the unmodified full-size input did not yield satisfactory coverage in the 14-source diagnostic.
- Independent held-out technical coverage: N11 106/106; full-pair technical coverage: N12 600/600.
- Final evaluator code and hashed recognizers: frozen. Manual validity is an openly recorded remaining limitation.
