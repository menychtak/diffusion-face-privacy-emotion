# Frozen experiment registry and evidence boundaries

> **2026-10-14 current evidence note:** The original registry below describes the historical N07–N22 lineage. The separately executed final held-out NB23 generation (324/324), NB24 unified evaluation (324/324 automatic measurements, 108/108 FER replay), and completed limited human visual QC (12 sources / 36 images) are now documented in [Final Scientific Audit](final_scientific_audit_nb24.md). [Final NB24 aggregates](../results/nb24_heldout_aggregate_by_condition.csv), [paired contrasts](../results/nb24_heldout_paired_contrasts.csv), and [manual QC counts](../results/nb24_manual_qc_aggregate.csv) take precedence for **final** comparisons. Historical references to pending QC apply only to that historical phase; the final QC is limited, not full-sample.


| Experiment | Private run (under `thesis_all/outputs/runs/`) | Verified execution |
| --- | --- | --- |
| N07 | `20260818T210720Z_notebook07_affectnet_larger_6aeb3643_f1142664` | 120 sources / 600 synthetic images |
| N12 V3 | `nb12_v3_biometric_11faafd9beb1_20261013T211442695856Z_bcf37701` | Corrected ArcFace/AuraFace on 600 |
| N16 | N16 frozen NIQE run | NIQE image-quality statistics |
| N17 v2 | `nb17v2_neutral_expression_12sources_2seeds_sd3pinned` | 12 sources x 2 seeds = 24 verified outputs |
| N18 | `nb18_paired_neutral_pilot_analysis_v1` | Strict matched pilot / NIQE |
| N19 | N19 paired biometric run | ArcFace/AuraFace 24/24 |
| N21 | `nb21_final_exact_n07_ensemble_fer` | N07 two-ViT original predictions 12/12 reproduced; N17 24/24; final paired bootstrap |
| N22/N22b | N21 private run folder | AI-assisted **provisional screenshot QC**: 19 PASS / 5 UNCERTAIN / 0 FAIL |

## N21 final paired pilot

The exact N07 FER evaluator consists of two frozen ViT models: `trpakov/vit-face-expression@ef0bc6fc34241b6587e7e009e7711357be28c024` and `mo-thecreator/vit-Facial-Expression-Recognition@5aae4f09e1da247eb0f1c1e6f53271601fcafe09`. Class probabilities are combined for the ensemble. The primary preservation definition is generated ensemble predicted emotion = annotated human target emotion.

For the **matched 24 images (12 sources)**, N07 preserved emotion for 19/24 (79.17%) and N17 neutral prompt for 6/24 (25%). N17 - N07 = **-54.17 percentage points**, 95% source-cluster bootstrap CI **[-79.17, -29.17]**. ArcFace mean difference -0.00637, CI [-0.10970, 0.07983]; AuraFace -0.05917, CI [-0.15663, 0.02895]; NIQE +0.19239, CI [+0.00385, +0.42891]. Bootstrap: 10,000 source-cluster draws, seed 21021. See [aggregate evidence](../results/nb21_final_paired_aggregate.csv). Scores/intervals refer to this small pilot only.

## Superseded FER experiment

**N20 is historical and provisional, NOT the validated N07-compatible FER estimate**. It used one ViT rather than the N07 two-ViT ensemble, and evaluated agreement with original predicted emotion rather than the human annotation. Never mix its 45.83% or -33.33 pp with N21 outcomes.

## Visual QC

The separate private AI-assisted screenshot observation record contains 24 pairs, **19 preliminary PASS, 5 UNCERTAIN, 0 FAIL**, with uncertain indices 8, 15, 16, 21, 22. This is **not** independently completed human manual QC. The original private human-review template remains unmodified and unreviewed. Quality exclusion sensitivity is not reported; the quantitative pilot is an all-pairs analysis.

## Limits and reproducibility

Face and person images, identities, source IDs, per-image outcomes, embeddings, and proprietary/private checkpoint receipts **remain only on Google Drive**. Cosine scores are not calibrated re-identification likelihood. NIQE reflects natural-image statistics rather than expression correctness or clinical validity. 12 source clusters are too few to support broad conclusions or reliable emotion-specific analysis; paired source-cluster bootstrap reflects cluster structure but does not remedy sampling limitations. A lack of a non-zero biometric delta is **not** proof of equal privacy or protection. N21 FER is the final intended run; do not run diffusion, biometric, NIQE or FER again as part of cleanup.
