# PDF text fidelity and revision audit

Reference document: user-provided 92-page `MSc Thesis - Facial Identity Obfuscation with Pretrained Diffusion Models (1)(1).pdf`. This is a **reference snapshot**, not proof that newer evaluators were never executed. PaperDock project: `MSc Thesis - Facial Identity Obfuscation with Pretrained Diffusion Models`.

## Verified restorations applied in PaperDock

- `chapters/07_results.tex`, table 7.1 introduction: restored `Ο Πίνακας~\\ref{tab:aggregate-results} συγκεντρώνει τις βασικές τελικές μετρικές.` matching PDF prose, instead of later prose claiming the table already contained N12 V3/N15 corrected values.
- Same section, table 7.1 caption: restored the PDF's neutral caption `Συνοπτικά αποτελέσματα της τελικής αξιολόγησης ανά συνθήκη...` instead of a later `Ιστορικά αποτελέσματα... N12 V3` caption.

Both were narrow text-only rollbacks; no numeric values, citations, figures or historical files were deleted. New corrected metrics belong in a **new evidence-backed updated Table 7.1**, not inside the old PDF with anachronistic wording.

## What has and has not been compared

Inspected PaperDock's `main.tex`, Chapters 1, 4–10 and bibliography for explicit insertion indicators (`N12 V3`, `N15`, `N21`, `NIQE`). Chapter 8 still describes the original 176/600 valid biometric comparisons and 424 missing values, **as the PDF originally did**, which is outdated as a **current numerical conclusion** but not a reason to falsify a text-only rollback. Do not treat the historical 424 failures as FlowEdit privacy evidence.

A complete **word-for-word/character-for-character diff of every LaTeX source paragraph against typeset PDF text has not been established** here: the PDF includes hyphenation, ligatures, line reflow and macro-expansion, which prevents naïve byte equality with TeX source. The two identified mismatching post-PDF edits have been restored, and all further edits must be based on a local paragraph-alignment diff plus explicit user review.

## Next manuscript table release

Existing [N12 V3 and N16 aggregate](../results/verified_n12_v3_n16_conditions.csv) records **600/600** finite ArcFace/AuraFace comparisons and 600 NIQE values. All three condition rows were read from the frozen private N12 diagnostic and N16 NIQE aggregate, not recomputed. The old table's 70 / 65 / 41 valid pairs and 424 failures must not be combined with N12 V3 means; retire the old values in the revised *results* table, and update the methodology text and discussion consistently when this newer evaluation is explicitly incorporated.

Do not conflate the post-hoc image-evaluator repair with a change to frozen FlowEdit generation. The generated images and configurations did not change. The teacher's request for an emotion-agnostic `same facial expression` target is a different prompt from N17's neutral-expression ablation, and remains unsupported as an executed exact condition.

No new Colab generation, evaluation or QC runs are required to implement this document review.
