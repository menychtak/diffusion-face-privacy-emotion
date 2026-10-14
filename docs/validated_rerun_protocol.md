# Validated rerun decision gate (2026-10-14)

This protocol supersedes informal requests to regenerate everything. **Do not rerun diffusion simply because a biometric evaluator was faulty.** Original generations are immutable experimental artifacts; first verify SHA-256 receipts and archived configuration. The corrected evaluation can run on those same images without altering the generator.

## Gates before any new computation

1. **Generation integrity**. Read N07 `resolved_config.json` and N17 frozen receipts. Verify each image and its SHA-256, FlowEdit commit `85594626161caca9dafa68592c1ffa21db87a806`, SD3-Medium revision `ea42f8cef0f178587cf766dc8129abd379c90671`, g=1.5/4.5/5.5 as recorded, source guidance 3.5, T=40, n_min=0, n_max=33, n_avg=1, seed matrix and prompt text. **Regenerate only a failed/unverifiable subset**, and label any new generation distinctly; never overwrite N07/N17.
2. **Biometric evaluator parity and coverage**. Prefer the already-executed N12 V3 corrected CPU ONNX evaluation on all 600 N07 images. Freeze SCRFD/ArcFace/AuraFace weight hashes and report numerator/denominator per condition, original-face vs generated-face detection failures and matched 4.5/5.5 source-seed pairs. Compare full-frame 512×512 with the historical YOLO-cropped route only as an explicit sensitivity experiment if evidence still fails coverage; do not blend incompatible protocols. Do not claim `>90%` without executed counts.
3. **Original-image FER baseline**. Verify executed N07 exact two-ViT original predictions against human labels on the **120 distinct** source faces. Existing recorded baseline: accuracy **0.475**, six-class macro-F1 **0.467**; re-extract exact numerator/denominator, class mapping and source split from raw outputs before publication. Separate this from single-ViT `trpakov` baseline specifically requested by the supervisor; the ensemble score is **not automatically** the single-ViT score.
4. **No-label same-expression control**. The supervisor asked for a target prompt specifying **"the same facial expression"** without an emotion class (e.g. g=4.5, seed 42). The existing N17 **neutral-expression** ablation is a *different* intervention and cannot satisfy this criterion. Treat this as a newly preregistered control requiring genuine generation and full paired evaluation if requested; do not relabel N17.
5. **Holdout**. Existing N15 analysis excludes the 12 tuning sources (108 sources, 540 synthetics). Revalidate source IDs, pairing, and exact CI from the saved run; avoid claiming it is pending if already executed.
6. **Quality**. N16 NIQE on 600 existing images and N21 paired NIQE on 24 exist. Use as no-reference IQA, specify lower is better and NIQE's limits. N22 screenshot QC is provisional, not independent full-resolution manual QC.

## Status and no-invention contract

- Already executed: N07 generations, N12 V3 corrected 600-image biometrics, N15 holdout, N16 NIQE, N17 24-image neutral ablation, N18/N19 paired metrics, N21 two-ViT FER replay, N22 provisional QC.
- **Do not rewrite thesis results until exact executed row-level evidence is extracted and statistical tables are frozen.**
- Genuinely missing: supervisor's *no-emotion, same-expression target* control; explicitly distinguish from N17 neutral prompt. Potentially missing: independently confirmed `trpakov`-only 120-source baseline, verification of N12 coverage by condition, full-resolution independent human QC.
- A prior faulty YOLO->FaceAnalysis route must not be described as an intrinsic failure of FlowEdit or as the final evaluator. Scientific methods can describe the selected corrected pipeline directly while disclosing limitations and protocol changes where necessary for reproducibility.
- Never make new quantitative claims from hypothetical reruns. Private faces, biometric per-image rows and source IDs stay in Drive; public GitHub only has frozen code and aggregate outcomes.

## PaperDock update gate

The active full thesis project is **MSc Thesis - Facial Identity Obfuscation with Pretrained Diffusion Models**. Existing Chapter 7 contains obsolete 424/600 and 51-pair figures from the original evaluator. Preserve those passages provisionally as historical, **not final results**, until the N12 V3 aggregate and genuine control results are verified. Do not overwrite accepted narrative revisions indiscriminately. Once new evidence is ready, revise methodology/tables/discussion together.
