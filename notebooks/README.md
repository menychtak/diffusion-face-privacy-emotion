# Notebook index — executed final workflow

| Stage | Notebook | Verified execution | Storage |
| --- | --- | --- | --- |
| 01 — Generation | [23 — confirmed held-out regeneration](23_confirmed_heldout_regeneration.ipynb) | **324/324** verified images; 108 held-out sources × three conditions × seed 42 | Image hashes / receipts in private Drive |
| 02 — Evaluation | [24 — unified held-out evaluation](24_unified_heldout_evaluation.ipynb) | **324/324** ArcFace/AuraFace pairs, **324/324** NIQE, **108/108** FER source replay; evaluation status `EVALUATION_COMPLETE_QC_PENDING` | Per-image records remain in private Drive |
| 03 — Analysis | [NB24 aggregate results](../results/nb24_heldout_aggregate_by_condition.csv) and [paired contrasts](../results/nb24_heldout_paired_contrasts.csv) | 108 paired sources, 10,000 bootstrap draws | Public aggregates only |
| 04 — Human QC | [Limited human QC counts](../results/nb24_manual_qc_aggregate.csv) | 12 sources / 36 synthetic images; one reviewer; completed, **not full-dataset QC** | Private detailed checklist |

### Execution and provenance boundaries

NB23 and NB24 are the maintained code for this final workflow. Their completed run evidence is held separately in Google Drive. **Do not claim public notebook cell outputs themselves prove an executed run**, and do not rerun expensive generation just to tidy the repository. Scientific qualification and open audit actions: [Final Scientific Audit](../docs/final_scientific_audit_nb24.md).

Historical N07–N22 experiments remain available via [thesis_notes](https://github.com/menychtak/thesis_notes) and should not be silently relabeled as NB24 runs. In particular, N17 used a *neutral* target, not the NB23 *same-expression* target. Earlier N20 single-ViT emotion agreement is not equivalent to N07/N21/NB24 two-ViT human-label accuracy.
