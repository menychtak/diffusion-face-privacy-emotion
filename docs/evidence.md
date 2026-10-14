# Frozen experiment registry and evidence boundaries

| Experiment | Private Drive run folder | Status |
|---|---|---|
| N07 | `20260818T210720Z_notebook07_affectnet_larger_6aeb3643_f1142664` | 600 generated images; original emotion results |
| N12 V3 | `nb12_v3_biometric_11faafd9beb1_20261013T211442695856Z_bcf37701` | corrected ArcFace/AuraFace for 600 |
| N16 | `nb16_no_reference_niqe_20261013T225209Z` | original and generated NIQE |
| N17 v2 | `nb17v2_neutral_expression_12sources_2seeds_sd3pinned` | 24/24 image generation verified |
| N18 | `nb18_paired_neutral_pilot_analysis_v1` | 24 paired NIQE comparisons |
| N19 | `nb19_n17v2_frozen_v3_biometrics` | 24/24 ArcFace/AuraFace valid; FER pending |

Source-level, biometric, face images, screenshots, manifests, and individual
scores are deliberately **not** committed to this public repository.

**Interpretation:** cosine similarity is not calibrated re-identification
probability. Lower NIQE typically indicates closer natural-image statistics;
it is not proof of facial realism or clinical utility. Bootstrap intervals
resample 12 source identities, not 24 independent images. Two sources per
emotion cannot establish reliable class-specific effects.

**Pending:** reproduce the exact frozen N07 FER checkpoint, preprocessing,
detection, and label map on the 24 N17v2 images, followed by source prediction
invariance and paired FER bootstrap. Manual face/alignment QC is still pending.
