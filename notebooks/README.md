# Thesis-to-code map

This is an academic reproducibility repository. The **reporting unit** is the original source face, not a synthetic image, and the **final held-out experiment** is N23 generation followed by N24 evaluation.

## Reading order

1. [Experiment protocol and dataset boundaries](../docs/final_scientific_audit_nb24.md): development and final sources, conditions, metric definitions, limitations.
2. [Generate — N23](01_heldout_generation_N23.ipynb): **already executed** in private Google Drive; this GitHub copy contains the notebook source, not its executed cell outputs.
3. [Evaluate — N24](02_heldout_evaluation_N24.ipynb): **already executed**; 324/324 biometric/NIQE pairs and 108 source-FER replays.
4. [Results](../results/README.md): public aggregate CSVs and paired confidence intervals.
5. [Review limits](../docs/final_scientific_audit_nb24.md): no calibrated identification attack, no clinical evaluation, one final generation seed.

**Do not rerun 01/02 just to add execution badges.** They have completed private runs. Upload an authentic executed notebook copy only if its original outputs have been checked for identifiable faces, subject IDs, raw paths, secrets, and private row-level data; otherwise keep the existing source notebook and the public aggregated execution evidence.

## Notebook provenance

| Thesis topic | Experiment or notebook | Where its source currently lives | Execution claim |
|---|---|---|---|
| Ch. 5: DDIM, DDPM inversion | N01–N02 | [Historical source archive](https://github.com/menychtak/thesis_notes/tree/main/Notebooks/current) | Development history; not final result |
| Ch. 5: FER-2013 comparison | N03 | [Historical source](https://github.com/menychtak/thesis_notes/blob/main/Notebooks/current/03_fer2013_methods_a_to_g_fer_dino.ipynb) | Development experiment; figures/numbers are historical |
| Ch. 5: FlowEdit prompt/guidance sweeps | N04–N06c | [Historical sources](https://github.com/menychtak/thesis_notes/tree/main/Notebooks/current) | Development/tuning; different denominators |
| Ch. 4–5: 120 sources / 600 synthetic images | N07 | [Original N07 source](https://github.com/menychtak/thesis_notes/blob/main/Notebooks/current/07_affectnet_final_multi_image_evaluation.ipynb) | Previously executed; **not** final held-out evidence |
| Ch. 5–6: detector alignment / corrected biometrics | N10–N12 | [Original notebooks](https://github.com/menychtak/thesis_notes/tree/main/Notebooks/current) | Previous evaluator development; N12 V3 algorithm used in N24 |
| Ch. 5–6: FER, exclusion, NIQE | N13–N16 | [Original notebooks](https://github.com/menychtak/thesis_notes/tree/main/Notebooks/current) | Prior validation/quality checks |
| Ch. 5: neutral prompt pilot | N17–N18 | [Original notebooks](https://github.com/menychtak/thesis_notes/tree/main/Notebooks/current) | Historical only; **different target prompt** from N23 |
| FER evaluator parity | N21 | [Historical notebook retained here](history/N21_fer_evaluator_validation.ipynb) | Evaluator-provenance notebook, not main pipeline |
| Final held-out generation | N23 | [01 — generation](01_heldout_generation_N23.ipynb) | Executed 324/324; original notebook execution remains private |
| Final unified evaluation | N24 | [02 — evaluation](02_heldout_evaluation_N24.ipynb) | Executed 324/324, 108/108 source FER replay |
| Human visual QC | Checklist (not an executable notebook) | [Public aggregate](../results/nb24_manual_qc_aggregate.csv) | 36 images reviewed once, exploratory sample |

## Historical evaluator code mirrored here

These notebooks were imported from the earlier [`thesis_notes/Notebooks/current`](https://github.com/menychtak/thesis_notes/tree/main/Notebooks/current) archive. **Embedded cell outputs were intentionally removed**: the copies below are **source-only**, even where the original notebook had been run. They are provided for code traceability, not as newly executed evidence.

| Research topic | Notebook |
| --- | --- |
| N11: biometrics alignment | [N11](history/11_v3_biometric_alignment_validation.ipynb) |
| N12: corrected ArcFace / AuraFace | [N12](history/12_corrected_v3_biometric_privacy_reevaluation.ipynb) |
| N13: QC-aware sensitivity | [N13](history/13_qc_aware_privacy_utility_sensitivity.ipynb) |
| N14: original FER baseline | [N14](history/14_original_fer_baseline_from_notebook07.ipynb) |
| N15: development-source exclusions | [N15](history/15_verified_tuning_exclusion_sensitivity.ipynb) |
| N16: NIQE | [N16](history/16_no_reference_image_quality_niqe.ipynb) |
| N17: neutral-prompt pilot | [N17](history/17_neutral_target_prompt_flowedit_pilot.ipynb) |
| N17v2: resumable neutral-prompt generation | [N17v2](history/17v2_neutral_target_resume_safe.ipynb) |
| N18: strict pilot pairs | [N18](history/18_n17v2_strict_paired_evaluation.ipynb) |
| N21: FER evaluator validation | [N21](history/N21_fer_evaluator_validation.ipynb) |

Earlier N01–N07 notebooks are several megabytes each, and some contain embedded face images; **do not copy those public historical files into this repository unfiltered**. Their precise source links are given in the map above.

**N19, N20, N22:** their exact final canonical notebook source and executed notebook file **have not been verified in this repository**. Never create dummy notebooks, label a code-only copy as executed, or generate new outputs just to fill sequence numbers. The public summary/result exports are preserved but do not themselves prove the presence of an executed notebook artifact.

## What should be uploaded manually?

Only a **verified source or executed** notebook that materially adds traceability and has passed a privacy review. The original code-only N01–N18 files are already publicly accessible at the linked GitHub history, and can be imported later if a self-contained repo is required. For executed notebook copies, use the original Drive/Colab export rather than relying on reconstructed JSON. See [manual import checklist](../docs/notebook_import_checklist.md).
