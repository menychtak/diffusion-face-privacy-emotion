# Diffusion Face Privacy & Emotion Preservation

Research implementation and frozen evidence for a Master's thesis on diffusion-based face identity obfuscation with emotion preservation. **The exploratory 12-source neutral-target ablation is complete; this repository does not claim clinically validated anonymization.**

## Frozen experiment status — 14 October 2026

| Component | Status |
| --- | --- |
| N07 AffectNet baseline | Executed: 120 source images, 600 synthetic images |
| N12 v3 / N19 ArcFace and AuraFace | Executed; corrected biometric pipeline |
| N16 / N18 NIQE | Executed |
| N17 v2 neutral-target | Executed: 12 sources, two seeds, 24 synthetic images |
| N21 exact N07 two-ViT FER ensemble | Executed: 12/12 original predictions reproduced, 24/24 N17 images evaluated |
| N22 / N22b visual screenshot review | Provisional AI-assisted observations: 19 PASS, 5 UNCERTAIN, 0 FAIL; **not** independent full-resolution human QC |

The N21 exact ensemble **supersedes N20** (single ViT and a different preservation definition). Never cite the N20 FER delta as the final paired outcome.

## Pilot findings (N17 minus matched N07)

| Metric | Mean paired difference | 95% source-cluster bootstrap CI |
| --- | ---: | ---: |
| Emotion preserved, percentage points | -54.17 | [-79.17, -29.17] |
| ArcFace cosine similarity | -0.00637 | [-0.10970, 0.07983] |
| AuraFace cosine similarity | -0.05917 | [-0.15663, 0.02895] |
| NIQE | +0.19239 | [0.00385, 0.42891] |

Emotion preservation denotes agreement of **generated two-ViT ensemble prediction with the human target emotion**, not agreement with the original classifier prediction. N07: 19/24 (79.17%); N17: 6/24 (25%). 10,000 bootstrap replicates resampled 12 source clusters (seed 21021), not 24 independent faces. The biometric confidence intervals cross zero; no demonstrated additional identity obfuscation from neutral-target prompting. Increasing NIQE is an unfavorable image-quality change, not direct perceptual evidence.

## Repository contents

- [Python package](src/face_privacy) — paired analysis, provenance checks, frozen FER ensemble and biometric utilities.
- [N21 Colab code](notebooks/21_final_exact_n07_ensemble_fer.ipynb) — archived final FER evaluation implementation. **Do not rerun by default.**
- [Canonical notebook index](notebooks/README.md) — one coherent generation / evaluation / analysis workflow backed by already-executed runs.
- [Aggregate N21 results](results/nb21_final_paired_aggregate.csv) — public summary only.
- [Evidence registry and limitations](docs/evidence.md) — scope, provenance and unresolved QC.
- [Private Drive data contract](docs/colab.md) — where already-executed private outputs live.
- [Historical research notebooks](https://github.com/menychtak/thesis_notes) — exploratory development lineage.

## Development

```bash
python -m pip install -e '.[test]'
pytest -q
```

## Privacy and scientific limits

Never commit original/generated faces, screenshots of participants, source identifiers, private row-level predictions, full manifests, embeddings, checkpoints or private receipts to this public repository. All raw evidence stays on private Google Drive. Cosine similarity is **not** calibrated re-identification risk. The source count is small, observations are exploratory, and no clinical efficacy or privacy guarantee has been established. The five visually uncertain pairs (8, 15, 16, 21, 22) remain flagged; independently reviewed, full-resolution face QC is still pending. No additional diffusion or FER runs are planned.
