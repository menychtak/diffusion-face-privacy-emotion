# Diffusion Face Privacy & Emotion Preservation

Research implementation and verified **held-out experimental evidence** for an MSc thesis on face identity obfuscation using pretrained diffusion models, while preserving facial emotion.

## Current research evidence (2026-10-14)

**Generation and automated evaluation complete; limited human visual QC complete. Thesis conclusions remain conditional on the [Final Scientific Audit](docs/final_scientific_audit_nb24.md).** This is not clinical validation or proof of irreversible anonymization.

| Stage | Protocol | Verified result |
| --- | --- | --- |
| Generate | [NB23 FlowEdit / SD3-Medium](notebooks/23_confirmed_heldout_regeneration.ipynb) | **324/324 verified** synthetic 512×512 images: 108 held-out AffectNet sources × 3 conditions × seed 42 |
| Evaluate | [NB24 unified frozen evaluators](notebooks/24_unified_heldout_evaluation.ipynb) | **324/324** paired valid ArcFace and AuraFace scores; **324/324** NIQE; **108/108** original FER predictions reproduced |
| Analyze | [Conditions](results/nb24_heldout_aggregate_by_condition.csv); [paired contrasts](results/nb24_heldout_paired_contrasts.csv) | 108 paired independent source units; source-level bootstrap, 10,000 draws |
| Human visual QC | [Limited QC summary](results/nb24_manual_qc_aggregate.csv) | **12 held-out source faces, 36 synthetic images** reviewed by one assessor; exploratory, non-random source-ID selection |
| Scientific review | [Final Scientific Audit](docs/final_scientific_audit_nb24.md) | Scope, supported findings, unresolved validity limits and release checklist |

**Key result:** Moving from guidance 4.5 to 5.5 reduces mean source–synthetic ArcFace cosine by **0.1992** (paired 95% CI [−0.2231, −0.1775]) and AuraFace cosine by **0.1776** (CI [−0.1983, −0.1586]). Human-label FER accuracy changes from **57.41% to 62.04%**, but the +4.63 percentage-point contrast has CI **[−2.78, +12.04] pp**. This supports *lower embedding similarity*, **not** proof of a general utility improvement or a calibrated re-identification rate.

The emotion-agnostic **same-expression** condition achieves **16.67%** human-label FER accuracy. Review [audit limitations](docs/final_scientific_audit_nb24.md) before attributing this result solely to failed expression preservation; the qualitative task and automated label task are different.

### Data handling

**Public GitHub:** code, protocol, source-independent aggregate statistics, limited aggregate QC counts, audit. **Private Google Drive:** original/generated face images, raw rows, source identifiers, personal labels/notes, per-image receipts, ONNX weights and executed Colab outputs. Do not upload the latter to this public repository. Public notebook source is not an executed-output export.

### Earlier experiments

Archived N07 (120 sources/600 images), N12 V3 biometrics, N16 NIQE, N17–N21 neutral-target pilot and N22 preliminary AI screenshot QC remain historical evidence and provenance **not** interchangeable with final NB23/NB24 data. See [experiment registry](docs/evidence.md) and [notebook index](notebooks/README.md).

## Developer checks

```bash
python -m pip install -e '.[test]'
pytest -q
```

A clean GitHub source tree is not equivalent to a fresh end-to-end Colab reproduction: access to licensed/private images, exact ONNX weights, and pinned model revisions is required. No medically deployable anonymization or privacy guarantee is claimed.
