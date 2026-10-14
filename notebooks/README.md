# Thesis-to-code map

**Executed and viewable on GitHub:** [03 — public NB24 results report](03_executed_public_results_report.ipynb) contains genuine Python execution counts and rendered aggregate outputs (no faces). This summarizes independently published result statistics; it is **not** the GPU run notebook. N23/N24 original algorithm notebooks remain source-only for privacy, with actual run evidence in private Drive and public aggregate tables.


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
| N11: biometrics alignment | [N11](history/N11_v3_biometric_alignment_validation.ipynb) |
| N12: corrected ArcFace / AuraFace | [N12](history/N12_corrected_v3_biometric_privacy_reevaluation.ipynb) |
| N13: QC-aware sensitivity | [N13](history/N13_qc_aware_privacy_utility_sensitivity.ipynb) |
| N14: original FER baseline | [N14](history/N14_original_fer_baseline_from_notebook07.ipynb) |
| N15: development-source exclusions | [N15](history/N15_verified_tuning_exclusion_sensitivity.ipynb) |
| N16: NIQE | [N16](history/N16_no_reference_image_quality_niqe.ipynb) |
| N17: neutral-prompt pilot | [N17](history/N17_neutral_target_prompt_flowedit_pilot.ipynb) |
| N17v2: resumable neutral-prompt generation | [N17v2](history/N17v2_neutral_target_resume_safe.ipynb) |
| N18: strict pilot pairs | [N18](history/N18_n17v2_strict_paired_evaluation.ipynb) |
| N21: FER evaluator validation | [N21](history/N21_fer_evaluator_validation.ipynb) |

Earlier N01–N07 notebooks are several megabytes each, and some contain embedded face images; **do not copy those public historical files into this repository unfiltered**. Their precise source links are given in the map above.

## Verified original Colab notebook sources — N19 / N20 / N22

The original private Colab files were located and examined. Public copies contain **code and markdown only**; recorded execution counts and embedded outputs were removed to protect subject images and private evaluation records.

| ID | Public source-only copy | Original Colab execution |
| --- | --- | --- |
| N19 (patched, completed version) | [N19 corrected](history/N19_neutral_pilot_biometric_evaluation.ipynb) | [Original executed N19](https://colab.research.google.com/drive/1eZ4Gs2pvxGhZGR16YZdo9TpQm0J0_iSO) |
| N19 initial attempt | Not mirrored; prior incomplete/failed setup | [Initial notebook](https://colab.research.google.com/drive/1qAcSZRxxrcYdNhP_XcwYhKGIt1tRrz9s) |
| N20 exact N07 FER replay | [N20](history/N20_fer_evaluator_reproduction.ipynb) | [Original executed N20](https://colab.research.google.com/drive/1aLijvkD01S49PqPe0QkVykSDtG8W7QTc) |
| N22 historical face alignment review | [N22 source-only](history/N22_historical_face_alignment_review.ipynb) | [Original executed N22](https://colab.research.google.com/drive/1SE_i4IK8KZpq7sFR7v6MZRMUQi50PaXL) |
| N22b provisional screenshot QC | [N22b source-only](history/N22b_provisional_visual_qc.ipynb) | [Original executed N22b](https://colab.research.google.com/drive/1hCe1m19eJ0qTjBDEdZTO3UvzKx4ToDw8) |

**Important:** N22 is a **historical** visual check of N07/N17 comparison pairs. N22b is explicitly a **provisional AI-assisted** record and must not be represented as the one-reviewer, 36-image **final NB24 manual QC**. N20 has saved output cells but includes explicit replay/provenance gates; it does not imply all earlier model-equivalence questions were conclusively resolved.


## What should be uploaded manually?

Only a **verified source or executed** notebook that materially adds traceability and has passed a privacy review. The original code-only N01–N18 files are already publicly accessible at the linked GitHub history, and can be imported later if a self-contained repo is required. For executed notebook copies, use the original Drive/Colab export rather than relying on reconstructed JSON. See [manual import checklist](../docs/notebook_import_checklist.md).

## N25 supplementary executed evaluation

[03 — held-out AU evaluation N25](03_heldout_au_evaluation_N25.ipynb) preserves execution counts and safe text-only results from the Colab run. Its aggregate outputs are in [`results/`](../results/nb25_au_aggregate.csv), with [paired contrasts](../results/nb25_au_paired_contrasts.csv) and [status](../results/nb25_au_run_status.json). The notebook estimates 20 AU features across 432 images; per-image predictions and original faces remain private. It is an exploratory post-hoc evaluation, not generation or manually annotated FACS.
