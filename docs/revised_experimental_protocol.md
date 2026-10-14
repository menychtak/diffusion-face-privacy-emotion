# Revised experimental protocol — final rerun requested, not yet executed

> **Historical planning artifact (superseded by executed NB23/NB24, 2026-10-14):** The proposed final rerun below **has since been executed**. Read the [Final Scientific Audit](final_scientific_audit_nb24.md) for actual verified results, limited manual QC, and unresolved interpretation limits. The old future-tense lines below are preserved solely as the pre-execution protocol, **not** current run status.


A fresh complete experimental reproduction has been requested. This remains a plan, **not an executed experiment or a result**. Existing executed N07/N12/N15/N16/N17/N19/N21 evidence must remain frozen and immutable.

## Preconditions
1. Use only original 120 AffectNet sources with verified source checksums, labeled six-class mapping and the exact development/tuning membership. Keep source identities private.
2. Record pinned FlowEdit commit `85594626161caca9dafa68592c1ffa21db87a806`, SD3-Medium revision `ea42f8cef0f178587cf766dc8129abd379c90671`, the original N07 prompts and all remaining N07 arguments verbatim from frozen resolved config. Do not infer parameters from thesis prose.
3. Freeze identities and evaluator preprocessing, ONNX detector/recognizer weight checksums, failure definitions, image integrity gates, seeds and image preprocessing **before** any new generation.
4. Keep new experiments in newly timestamped run directories; no overwrites of historical evidence, no raw images or row-level participant data in public GitHub.

## Evaluation strategy
- **Biometric coverage (professor point 1):** corrected N12 V3 / N15 already re-evaluated existing N07 outputs (600/600 attempted and reportedly finite). The new final run must independently confirm face detection, alignment and success coverage per condition rather than treating historical records as its outputs. Validate exact coverage by source, condition, model and matching pair; publish the corrected estimates, not the historical 424-failure pipeline. Do not repeat generation to repair detector coverage.
- **Original FER baseline (point 2):** 120-image recorded baseline 0.475 accuracy, 0.467 six-class macro-F1 is available historically, but before thesis publication verify its exact evaluator (N07 two-ViT ensemble vs trpakov-only) and denominator directly against archived executed rows. Label each evaluator explicitly. No artificial comparison with an incompatible classifier.
- **Prompt ablation (point 3):** this truly requires new **generation**. Use target prompt without a named emotion, specifically phrased `the same facial expression` while retaining the different-person identity instruction. Fix g=4.5 seed=42 and all frozen original parameters. Save a separate run/manifest. The existing N17 **neutral-target** pilot is not this ablation and cannot be used as substitute.
- **Tuning-held-out analysis (point 4):** recompute N15-style paired comparisons after excluding exact 12 development source IDs from the 120. Keep the 108-source results separate from full-120 descriptives.
- **Quality (point 5):** use executed N16 NIQE per-image results; report coverage, means, paired intervals, model/version and limitations. Qualitative review remains provisional (N22b 19 PASS / 5 UNCERTAIN / 0 FAIL); independent full-resolution QC has not been completed.

## New release gates

A new complete conclusion requires: matching source-image SHA-256, frozen generation revision/config receipts, strict source-seed pair coverage, both identity evaluators, exact FER definition and checkpoint, NIQE coverage, held-out analyses, bootstrap by source, status per failed inference, and a raw-vs-public aggregate consistency report.

## PaperDock policy

**Do not rewrite experimental history.** Document the original N07 production procedure, identify historical biometric missingness as a superseded evaluator implementation limitation only where methodologically pertinent, and present corrected N12/N15 estimates as the definitive evaluation. New emotion-agnostic prompt ablation should be described only once generated and evaluated. Avoid citation/number changes without verified sources, and do not blanket-rollback accepted prose revisions without a revision-to-revision diff. This document is a plan, not proof that a fresh run happened.
