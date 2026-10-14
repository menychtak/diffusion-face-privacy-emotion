# Canonical notebooks — thesis presentation

The original **generation** is the archived executed 600-image N07 run. **A fresh final run has now been requested** using independently verified configurations and a distinct emotion-agnostic prompt control; it has not yet been executed. To present the research as a coherent implementation, use this three-stage index instead of an ordered list of debugging notebooks.

| Stage | Canonical source | Execution |
| --- | --- | --- |
| **01. Generate** | N07: `thesis_notes/Notebooks/current/07_affectnet_final_multi_image_evaluation.ipynb`; archived configuration and immutable receipts on private Drive | **Archived execution**; new final reproduction pending |
| **02. Evaluate** | N12 V3 ArcFace/AuraFace, N16 NIQE, N07 FER; the [N21 exact two-ViT pilot evaluator](21_final_exact_n07_ensemble_fer.ipynb) is a separate 24-image ablation | **Archived evaluation**; final run/evaluator parity pending |
| **03. Analyze** | N15 dev-held-out source-cluster paired analysis, N18–N21 exploratory neutral pilot | **Archived analysis**; recalculate final tables only from the new verified evidence |

## Presentation versus provenance

These are **conceptual chapters**, not a fabricated single historical execution. The full original notebooks in [`thesis_notes`](https://github.com/menychtak/thesis_notes/tree/main/Notebooks/current) must stay intact for provenance. They are deliberately not copied wholesale into the public final repository: outputs can include screenshots, face images, old evaluator code and large private records.

A polished standalone generation notebook could be produced by extracting only generation/config/receipt-validation code from the exact N07 source, **after** a code-level side-by-side parity review. Until parity is established, do not present a cleaned or rewritten generation notebook as a bitwise equivalent executed reproduction. The future final run must use new output paths and immutable per-image receipts. Similarly, avoid editing old execution notebooks to make their results appear obtained with a later evaluator.

See the [consolidated methodological index](../docs/consolidated_workflow_and_supervisor_audit.md), [original PDF fidelity audit](../docs/pdf_fidelity_audit.md), and [verified 600-image results](../results/verified_n12_v3_n16_conditions.csv).
