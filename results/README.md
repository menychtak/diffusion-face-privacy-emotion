# Reproducible results, not private faces

The final held-out experiment is **N23→N24**, 108 source images × 3 conditions = 324 synthetic outputs, seed 42.

| File | Meaning |
|---|---|
| [nb24_heldout_aggregate_by_condition.csv](nb24_heldout_aggregate_by_condition.csv) | Final means and accuracy for three conditions; use for Chapter 7's main table |
| [nb24_heldout_paired_contrasts.csv](nb24_heldout_paired_contrasts.csv) | Within-source paired deltas and bootstrap uncertainty |
| [nb24_manual_qc_aggregate.csv](nb24_manual_qc_aggregate.csv) | Human review: 12 originals and 36 synthetic examples, one rater, non-random subset |
| [nb24_heldout_status.json](nb24_heldout_status.json) | Historical machine status at end of N24; `QC_PENDING` means manual review was not integrated **inside N24**. QC was subsequently done separately |
| [verified_n12_v3_n16_conditions.csv](verified_n12_v3_n16_conditions.csv) | **Historical** corrected biometrics and NIQE, not the final held-out N24 |
| [nb21_final_paired_aggregate.csv](nb21_final_paired_aggregate.csv) | **Historical** FER evaluator provenance |
| [nb19_public_summary.csv](nb19_public_summary.csv) | **Historical** analysis summary |

A lower ArcFace/AuraFace cosine is **not** a re-identification success rate. Classifier accuracy vs human emotion labels is **not** human-rated same-expression preservation. NIQE is not a clinical-quality measure. Do not aggregate 600 historic N07 rows with 324 N24 rows.

A complete public re-identification benchmark, new Macro-F1 value, or clinical claim cannot be produced from the data shared here. See [scientific audit](../docs/final_scientific_audit_nb24.md).

### N25 estimated-AU supplement

- [`nb25_au_aggregate.csv`](nb25_au_aggregate.csv): 20-AU per-condition aggregate measurements, 107 valid pairs per condition.
- [`nb25_au_paired_contrasts.csv`](nb25_au_paired_contrasts.csv): source-level paired AU MAE differences and 95% bootstrap intervals.
- [`nb25_au_run_status.json`](nb25_au_run_status.json): detector, counts, seeds and limitations.

These contain no facial images or private row-level data. The [executed notebook](../notebooks/03_heldout_au_evaluation_N25.ipynb) provides safe text outputs and retained execution counts.
