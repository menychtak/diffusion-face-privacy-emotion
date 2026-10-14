"""Fail closed when evidence cannot be traced to the frozen experiments."""
from __future__ import annotations
import hashlib
from pathlib import Path
import pandas as pd

FLOWEDIT_COMMIT = "85594626161caca9dafa68592c1ffa21db87a806"
SD3_REVISION = "ea42f8cef0f178587cf766dc8129abd379c90671"

def file_sha256(path: str | Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for part in iter(lambda: f.read(1024 * 1024), b""):
            h.update(part)
    return h.hexdigest()

def verify_generation_receipts(receipts: pd.DataFrame, *, require_files: bool = True) -> None:
    expected = {"source_id","seed","status","output_path","output_sha256",
                "runner_commit","sd3_revision"}
    if expected - set(receipts):
        raise ValueError(f"Missing receipt columns: {sorted(expected - set(receipts))}")
    if len(receipts) != 24 or receipts.source_id.nunique() != 12 or receipts.duplicated(["source_id","seed"]).any():
        raise ValueError("Expected exactly 12 unique sources x 2 seeds")
    if set(receipts.seed) != {42,123} or not receipts.groupby("source_id").size().eq(2).all():
        raise ValueError("Seeds missing or duplicated")
    if set(receipts.status) != {"VERIFIED"}:
        raise ValueError("All 24 receipts must be VERIFIED")
    if set(receipts.runner_commit) != {FLOWEDIT_COMMIT} or set(receipts.sd3_revision) != {SD3_REVISION}:
        raise ValueError("Frozen code/model revision mismatch")
    if require_files:
        for row in receipts.itertuples(index=False):
            if file_sha256(row.output_path) != row.output_sha256:
                raise ValueError(f"Generated image digest mismatch: {row.source_id}/{row.seed}")

def require_exact_fer_provenance(rows: pd.DataFrame) -> None:
    fields={"source_id","seed","output_sha256","n17_emotion_predicted_class","fer_evaluator_provenance"}
    if fields - set(rows) or len(rows)!=24 or rows.duplicated(["source_id","seed"]).any():
        raise ValueError("Incomplete or non-unique FER predictions")
    if rows[list(fields)].isna().any().any():
        raise ValueError("FER predictions are pending")
    provenance=rows.fer_evaluator_provenance.astype(str).str.strip()
    if provenance.nunique()!=1 or provenance.iloc[0] in ("", "unknown", "unverified"):
        raise ValueError("No verified unique FER evaluator provenance")
    # This checks structural completeness only. Caller must independently audit
    # checkpoint bytes, preprocessing, label map and source predictions.
