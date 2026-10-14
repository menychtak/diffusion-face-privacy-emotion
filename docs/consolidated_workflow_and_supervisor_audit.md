# Consolidated thesis workflow — archived baseline and pending fresh final run

## Canonical workflow

The scientific workflow has **three conceptual stages**, not one Colab notebook per historical debugging step:

1. **Generation (frozen N07)**: 120 distinct AffectNet+ sources, six classes (20 each), 512 × 512 preprocessed images. FlowEdit commit `85594626161caca9dafa68592c1ffa21db87a806` with SD3-Medium revision `ea42f8cef0f178587cf766dc8129abd379c90671`. Conditions target guidance 4.5 and 5.5, seeds 42 and 123; weak reference g=1.5 seed 42. **600 historical images already generated**. A separately versioned final reproduction with verified configs and the supervisor's emotion-agnostic control has been requested; do not overwrite this original generation.
2. **Evaluation (frozen N12 V3 / N15 / N16 / N21)**: SCRFD-aligned ArcFace/AuraFace, existing source/target emotion classifier outputs, and NIQE. Evaluate previously generated files read-only; maintain independent checksum and evaluator provenance. N21's exact two-ViT ensemble replay is a *24-image N17 pilot evaluator*, not a replacement for every historical FER result.
3. **Analysis and manuscript tables**: join frozen records on **source ID, condition and seed**, exclude exact development/tuning sources for the 108-source sensitivity analysis, bootstrap by source, output public aggregates. Do not publish source-level data.

## Notebook entry points

| Purpose | Canonical evidence | What to keep |
| --- | --- | --- |
| Generation | [Historical executed N07](https://github.com/menychtak/thesis_notes/tree/main/Notebooks/current) and private N07 Drive run | Generation cells and exact immutable config, output receipts; no cached output re-run |
| Biometric evaluator | Archived N12 V3, N15 | Frozen detector, pre-processing, align/cosine, exact weight SHA-256, same 600 saved output images |
| Expression/FER | Archived N07 evaluation plus [exact ensemble N21](../notebooks/21_final_exact_n07_ensemble_fer.ipynb) | Separate the 120-original baseline, 600-image categorical statistics and N21 24-image ablation |
| Quality | Archived N16 | Executed NIQE results, coverage and meaning |
| Statistical results | N15, N18–N21 outputs | Public only aggregate metrics and source-cluster interval provenance |

This is a **logical reduction**, not a false claim that the many archived notebooks were all executed as one. Retain historical notebooks and run receipts unchanged (prefer keeping the archival `thesis_notes` repository separate from the final presentation repository). Avoid copying large embedded generated outputs into Git.

## Professor requirements — evidence status

| Requirement | Existing evidence | Missing or qualification |
| --- | --- | --- |
| 1. Biometric evaluation coverage | N12 V3 already evaluated **600/600** saved images; N15 108-source corrected sensitivity exists | Verify numeric coverage and failure-stage definitions from actual N12 V3 row-level output before replacing Table 7.1/7.2; *600 attempted ≠ 600 successful detections* |
| 2. FER original 120 baseline | Historical accuracy **0.475**, macro-F1 **0.467** recorded | Verify the classifier version/definition against N07 exactly; a single-ViT baseline must not be silently called the two-ViT ensemble |
| 3. Emotion-agnostic target | N17 neutral-expression pilot **12 sources × 2 seeds**, final N21 FER/biometrics | **Not the same** as proposed `the same facial expression` at g=4.5 seed 42; teacher's exact requested condition remains unexecuted unless an existing matching run can be proven |
| 4. Remove 12 tuning sources | N15 dev-excluded **108-source / 540-synthetic** analysis already executed | Use frozen selection manifest to demonstrate exact exclusion |
| 5. Quantitative quality | N16 NIQE computed on **600** generated images; N18/19 pilot NIQE | Report actual per-condition means/CI from N16 rather than inventing values |
| 6. Formatting and bibliography | Frozen PDF is 92-page reference artifact | Do not selectively import accepted PaperDock prose that disagrees with the supplied PDF; correct spelling/citations only with verified sources |

## Verified corrected historical results (not final rerun results)

In N15 **108-source / 540-image dev-excluded analysis**: g=4.5 mean ArcFace **0.6498**, AuraFace **0.6536**, emotion correct **0.5958**; g=5.5 ArcFace **0.4583**, AuraFace **0.4795**, emotion correct **0.6417**. Paired g5.5-g4.5 ArcFace change **-0.1943** (95% source-cluster CI **[-0.21429,-0.17497]**); AuraFace **-0.17588** (CI **[-0.19316,-0.16008]**). Emotion correctness delta **+0.04630** (CI **[-0.00926,0.10648]**) does **not** exclude zero. These numbers must be explicitly marked as the N15 corrected dev-excluded analysis; they are **not** the PDF's original 70/65-record table or the small N21 neutral pilot.

The historical N21 pilot (12 sources) found a **-54.17 percentage-point** loss in emotion label preservation from 19/24 to 6/24 under neutral prompting. Its identity CIs cross zero; this pilot is not the professor's specified emotion-agnostic same-expression prompt condition.

## Manuscript baseline and integrity rules

The user-supplied PDF (`MSc Thesis - Facial Identity Obfuscation with Pretrained Diffusion Models (1)(1).pdf`, 92 pages) is the **text reference** for accepted PaperDock rollback decisions. Restore demonstrably changed sentences to the source PDF when asked; **do not retroactively present a post-hoc evaluator implementation correction as though it had been present in the PDF**. Present corrected analysis clearly when updating quantitative tables, and maintain scientific audit receipts separately, without narrating debugging chronology as a research finding.

Use a single canonical prose term, preferably «απόκρυψη ταυτότητας προσώπου», while defining why no anonymity certification is claimed. Keep original photos, private results, person-level metadata and output images off public GitHub.
