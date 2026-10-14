# Final Scientific Audit — NB23/NB24 held-out experiment

**Audit date:** 2026-10-14. **Status:** verified *aggregate* results with limited manual visual QC; **NOT** independently certified anonymity, not clinical evaluation, not publication-ready claims beyond the boundaries below.

## 1. What was actually run

- N07 historic: 120 AffectNet source images / 600 generated images, archived separately.
- Final **NB23**: exact **12 tuning/development source IDs excluded**; **108 held-out source images**, one generated image for each of **three prompt/guidance conditions** (n07_g4p5, n07_g5p5, same_expression_g4p5), seed 42, **324 verified outputs** with per-image SHA-256 receipts.
- Generation: FlowEdit commit `85594626161caca9dafa68592c1ffa21db87a806`; Stable Diffusion 3 Medium revision `ea42f8cef0f178587cf766dc8129abd379c90671`, 512×512. The new same-expression prompt is **not** the old N17 neutral prompt.
- Final **NB24**: N07 compatible pinned two-ViT FER ensemble (source prediction replay **108/108**), N12 V3 aligned ArcFace and AuraFace with SHA-pinned detector and recognizer weights (**324/324 valid pairs per backend**), N16-compatible pyiqa NIQE (**324/324 valid**). Recorded status: `EVALUATION_COMPLETE_QC_PENDING` because manual review had not yet been incorporated into the automatic run.
- Visual QC subsequently supplied by one human reviewer: **12 deterministic sources (first two IDs per each of six emotion labels)** × 3 conditions = **36 synthetic outputs**. Checklist fields are binary: `face_valid_YN` and `expression_similar_YN` use Y = yes; **`artifact_YN` uses Y = distortion present, N = no distortion**. The detailed checklist remains private.

## 2. Verified quantitative results

All means below are from the 108-source final held-out NB24 results; lower embedding cosine denotes greater *technical* dissimilarity, higher human-label FER matching denotes higher measured classification utility, and lower NIQE is generally preferred for natural-image statistics.

| Condition | ArcFace cosine ↓ | AuraFace cosine ↓ | FER = human target ↑ | FER = original model prediction ↑ | NIQE ↓ |
| --- | ---: | ---: | ---: | ---: | ---: |
| N07 guidance 4.5 | 0.6557 | 0.6539 | 57.41% (62/108) | 60.19% | 7.7020 |
| N07 guidance 5.5 | 0.4565 | 0.4763 | 62.04% (67/108) | 50.93% | 7.6126 |
| Same-expression guidance 4.5 | 0.5955 | 0.5903 | 16.67% (18/108) | 45.37% | 7.8309 |

**Paired g5.5 minus g4.5**, 10,000 source bootstrap replicates (seed 24024):
- ArcFace mean Δ **−0.1992**, 95% CI **[−0.2231, −0.1775]**.
- AuraFace mean Δ **−0.1776**, 95% CI **[−0.1983, −0.1586]**.
- Human-label FER accuracy Δ **+4.63 pp**, 95% CI **[−2.78, +12.04] pp**: interval crosses zero; **a positive utility improvement is not statistically established**.
- FER agreement with original model prediction Δ **−9.26 pp**, 95% CI **[−17.59, −0.93] pp**. This is a *different outcome*; it should not be conflated with human-label matching.
- NIQE Δ **−0.0894**, 95% CI **[−0.1491, −0.0311]**: small improvement in no-reference image naturalness only.

For *same-expression minus g4.5*, human-target FER Δ **−40.74 pp**, 95% CI **[−50.00, −31.48] pp**; compared with g5.5: **−45.37 pp**, CI **[−54.63, −35.19] pp**. This is classifier-based label preservation, not direct expression geometry or human equivalence.

Source provenance: [condition-level aggregates](../results/nb24_heldout_aggregate_by_condition.csv), [paired estimates](../results/nb24_heldout_paired_contrasts.csv), [NB24 execution status](../results/nb24_heldout_status.json). Do not mix these with the archived 600-image or 24-image pilot results.

## 3. Limited independent human visual check

| Condition | Valid face | Similar expression | Distortion present |
| --- | ---: | ---: | ---: |
| N07 guidance 4.5 | 8/12 | 10/12 | 5/12 |
| N07 guidance 5.5 | 8/12 | 9/12 | 9/12 |
| Same-expression guidance 4.5 | 9/12 | 8/12 | 3/12 |

The same assessor rated all conditions on **the same 12 originals**. Their selection by ascending source ID is **not a random sample** of 108 held-out sources and no assessor reliability or agreement statistic is available. **Do not generalize 9/12 distortion rate to all g5.5 images.** Not every valid face or visually similar expression implies biometric safety or correct human-labeled FER class. The contrast between 8/12 judged similar expressions and 18/108 correct human-label predictions in same-expression is *not* direct disagreement on matched denominators: different tasks and sample sizes.

## 4. Claim ledger (evidence / interpretation / limitation)

| Claim | Classification | Evidence and defensible wording |
| --- | --- | --- |
| Three final conditions completed on held-out sources | **Supported** | NB23 receipts 324/324; 108 unique held-out source clusters. |
| g5.5 produces lower biometric embedding similarity than g4.5 | **Supported, technical metric only** | ArcFace and AuraFace paired CIs exclude zero; no operating-point verification. |
| g5.5 preserves human-annotated emotion more accurately than g4.5 | **Not demonstrated as general improvement** | Numerical +4.63 pp, 95% CI includes zero. |
| same-expression preserves the annotated emotion as well as label-conditioned prompts | **Contradicted for the measured two-ViT classifier outcome** | Human-label match 16.67%, paired declines with CIs below zero; no proof of total loss of physical expression. |
| g5.5 has more visible distortions | **Observed in limited QC subset; not population estimate** | 9/12 vs 5/12 marks of distortion, source-ID selected, one assessor. |
| Low embedding cosine means anonymization cannot be reversed / clinical privacy | **Unsupported** | No calibrated face matching threshold, attack success rate, gallery search, membership or inversion resistance testing. |
| Quality acceptable for healthcare | **Unsupported** | NIQE alone is not a clinical-quality test; no clinicians or DAIC-WOZ clinical evaluation. |
| Absence of statistical FER improvement means a broken evaluator | **Unsupported inference** | Frozen FER models loaded; 108/108 original prediction replay. Remaining uncertainty is sampling/generalization and output failure modes, not automatically a pipeline defect. |

## 5. Audit checks and remaining limits

**Passed / evidenced:** 324 generated output receipts; no tuning overlap in NB23 selection; source-level paired denominators; ArcFace/AuraFace complete finite pairs; FER original prediction parity 108/108; NIQE complete; public aggregate files agree with the recorded run exports; QC checklist totals 36 and binary fields completed.

**Important methodological caveat:** The frozen detector ONNX SHA-256 identifies the unchanged model, but the `insightface` API exposes it with class name `RetinaFace` for this runtime; code checks must not confuse a Python wrapper name with a change to ONNX weights. The visual-QC subset includes face-validity failures, meaning automatically finite embeddings do **not** imply every generated output is visually valid.

**Remaining, not silently passed:**
1. Human QC covered **36/324 images**; no independent second rater and not representative random sampling.
2. A single seed (42) limits between-seed stability conclusions.
3. No calibrated identification gallery/threshold attack: avoid the term measured *re-identification risk* for raw cosine.
4. Differences in prompting, photo style (including possible grayscale/color effects) can confound attributing differences exclusively to emotion conditioning; a detailed prompt/style parity check remains an interpretive limitation.
5. The main public GitHub notebooks are source/protocol copies; executed Colab cell output bytes remain private. A clean fresh-runtime replay was **not** established by this audit.
6. Baseline 108-original human-label accuracy/macro-F1 and per-emotion stratified effects are not included in these public aggregate files. Do not invent those statistics or a final Macro-F1.
7. Limited QC is attached *outside* the original NB24 execution status; the original `EVALUATION_COMPLETE_QC_PENDING` is an accurate historical snapshot and should **not** be overwritten as if the QC were in the run.

## 6. Release decision

**Repository research-evidence presentation: READY WITH QUALIFICATIONS.** Final held-out generation and automated assessment are complete; QC summary is recorded and limitations explicit. **Full scientific closure / clinical privacy validation: NOT CLAIMED.** The next writing step is to align thesis Chapters 7–8 to the verified NB24 aggregates and distinctions above, not to request new images or retrofit unsupported claims.

**No new generation is recommended by this audit.** Optional extensions (additional blinded raters, larger random QC sample, attack-based re-identification test, baseline Macro-F1) are future work, not hidden prerequisites for the recorded MSc experimental report.
