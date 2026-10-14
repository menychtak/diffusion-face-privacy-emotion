# Diffusion Face Privacy & Emotion Preservation

Research implementation and frozen evidence for a Master's thesis on diffusion-based face identity obfuscation with emotion preservation. **Historical experiments are archived, but the final thesis release is NOT frozen.** A new, independently pinned end-to-end experimental reproduction has been requested; its results must be verified before replacing thesis tables. No clinical anonymization claim is made.

## Historical executed evidence — not the final rerun

| Component | Status |
| --- | --- |
| N07 AffectNet baseline | Executed: 120 source images, 600 synthetic images |
| N12 v3 / N19 ArcFace and AuraFace | Executed; corrected biometric pipeline |
| N16 / N18 NIQE | Executed |
| N17 v2 neutral-target | Executed: 12 sources, two seeds, 24 synthetic images |
| N21 exact N07 two-ViT FER ensemble | Executed: 12/12 original predictions reproduced, 24/24 N17 images evaluated |
| N22 / N22b visual screenshot review | Provisional AI-assisted observations: 19 PASS, 5 UNCERTAIN, 0 FAIL; **not** independent full-resolution human QC |

The N21 exact ensemble **supersedes N20** (single ViT and a different preservation definition). Never cite the N20 FER delta as the final paired outcome.

## Historical exploratory pilot findings (N17 minus matched N07)

| Metric | Mean paired difference | 95% source-cluster bootstrap CI |
| --- | ---: | ---: |
| Emotion preserved, percentage points | -54.17 | [-79.17, -29.17] |
| ArcFace cosine similarity | -0.00637 | [-0.10970, 0.07983] |
| AuraFace cosine similarity | -0.05917 | [-0.15663, 0.02895] |
| NIQE | +0.19239 | [0.00385, 0.42891] |

Emotion preservation denotes agreement of **generated two-ViT ensemble prediction with the human target emotion**, not agreement with the original classifier prediction. N07: 19/24 (79.17%); N17: 6/24 (25%). 10,000 bootstrap replicates resampled 12 source clusters (seed 21021), not 24 independent faces. The biometric confidence intervals cross zero; no demonstrated additional identity obfuscation from neutral-target prompting. Increasing NIQE is an unfavorable image-quality change, not direct perceptual evidence.

## Next release gate

The newly agreed final workflow requires a **fresh, versioned run** using independently verified source checksums, frozen FlowEdit/SD3 configs, evaluator preprocessing, and reproducible output receipts, with the supervisor's exact emotion-agnostic target prompt (`the same facial expression`) as a distinct control condition. The existing N17 **neutral** ablation is not that condition. Reassess the 120-original FER baseline, biometric coverage, quality, and 108-source tuning-held-out comparisons under a consistent evaluation definition. Do not overwrite previous runs or publish unexecuted numbers. The implementation/config freeze and subsequent run have **not yet been executed**. See [revised experimental protocol](docs/revised_experimental_protocol.md).

## Repository contents

- [Python package](src/face_privacy) — paired analysis, provenance checks, frozen FER ensemble and biometric utilities.
- [N21 Colab code](notebooks/21_final_exact_n07_ensemble_fer.ipynb) — archived final FER evaluation implementation. **Do not rerun by default.**
- [Canonical notebook index](notebooks/README.md) — one coherent generation / evaluation / analysis workflow backed by already-executed runs.
- [Aggregate N21 results](results/nb21_final_paired_aggregate.csv) — public summary only.
- [Evidence registry and limitations](docs/evidence.md) — scope, provenance and unresolved QC.
- [Frozen V3 biometric pipeline](docs/frozen_biometrics_v3.md) — YOLO crop removal, detector scale comparison, aligned embeddings and technical coverage audit.
- [Private Drive data contract](docs/colab.md) — where already-executed private outputs live.
- [Historical research notebooks](https://github.com/menychtak/thesis_notes) — exploratory development lineage.

## Development

```bash
python -m pip install -e '.[test]'
pytest -q
```

## Privacy and scientific limits

Never commit original/generated faces, screenshots of participants, source identifiers, private row-level predictions, full manifests, embeddings, checkpoints or private receipts to this public repository. All raw evidence stays on private Google Drive. Cosine similarity is **not** calibrated re-identification risk. The source count is small, observations are exploratory, and no clinical efficacy or privacy guarantee has been established. The five visually uncertain pairs (8, 15, 16, 21, 22) remain flagged; independently reviewed, full-resolution face QC is still pending. An independently versioned final-generation/evaluation run is planned but not yet executed; historical figures remain labeled historical.
