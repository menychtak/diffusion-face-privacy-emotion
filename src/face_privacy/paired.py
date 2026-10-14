"""Source-cluster paired descriptive analysis; cosine is NOT a probability."""
from __future__ import annotations
import numpy as np
import pandas as pd

KEYS = ("source_id", "seed")

def strict_pair(reference: pd.DataFrame, candidate: pd.DataFrame, *, columns: list[str]) -> pd.DataFrame:
    """Match identical source+seed pairs, refusing duplicates and omissions."""
    for label, df in (("reference", reference), ("candidate", candidate)):
        required = set(KEYS) | set(columns)
        if label == "reference":
            required = set(KEYS)
        missing = required - set(df.columns)
        if missing:
            raise ValueError(f"{label} missing columns: {sorted(missing)}")
        if df.duplicated(list(KEYS)).any():
            raise ValueError(f"{label} has duplicate source/seed pairs")
    if set(map(tuple, reference[list(KEYS)].to_numpy())) != set(map(tuple, candidate[list(KEYS)].to_numpy())):
        raise ValueError("source/seed keys differ; refusing unpaired comparison")
    result = reference.merge(candidate, on=list(KEYS), how="inner", validate="one_to_one", suffixes=("_ref", "_new"))
    if len(result) != len(reference):
        raise ValueError("matched row count differs")
    return result

def cluster_bootstrap_delta(frame: pd.DataFrame, column: str, *, draws: int = 10000, seed: int = 19019) -> dict:
    """Resample independent sources, keeping all seeds of each source together."""
    if column not in frame:
        raise ValueError(f"Missing metric: {column}")
    if frame.source_id.nunique() < 2:
        raise ValueError("Need at least two independent source clusters")
    if frame[column].isna().any():
        raise ValueError("Missing paired metrics; report coverage separately")
    groups = [g[column].to_numpy(dtype=float) for _, g in frame.groupby("source_id", sort=True)]
    if not all(np.isfinite(g).all() for g in groups):
        raise ValueError("Metrics must be finite")
    rng = np.random.default_rng(seed)
    ci_samples = np.empty(draws)
    for k in range(draws):
        sample = rng.integers(0, len(groups), size=len(groups))
        ci_samples[k] = np.concatenate([groups[j] for j in sample]).mean()
    lo, hi = np.quantile(ci_samples, [0.025, 0.975])
    return {"mean_delta": float(frame[column].mean()), "ci95_low": float(lo),
            "ci95_high": float(hi), "n_pairs": len(frame),
            "n_sources": int(frame.source_id.nunique()), "bootstrap_seed": seed,
            "bootstrap_draws": draws}
