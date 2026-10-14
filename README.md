# Face Identity Obfuscation with Diffusion Models
**MSc thesis · University of Piraeus · Python / Google Colab**

Can a pretrained image editor alter the biometric identity of a face without discarding information needed for facial emotion recognition?

This repository accompanies the thesis with **code, an experiment map, result tables, and an explicit scientific audit**. It distinguishes development work from the final held-out experiment. It does **not** claim certified anonymization or clinical fitness.

**Want to see executed cells directly on GitHub?** Open [03 — executed public NB24 results report](notebooks/03_executed_public_results_report.ipynb). Its Python cells were executed against the published aggregate values; it displays the three condition means and the g5.5–g4.5 contrast. **This is a descriptive report, not a rerun of GPU generation, model inference, or the raw bootstrap.**

## Reproduce the scientific narrative

| Read | Material | Thesis |
| --- | --- | --- |
| 1 | [Notebook map and experiment history](notebooks/README.md) | Chapters 4–6 |
| 2 | [01 — held-out generation (N23)](notebooks/01_heldout_generation_N23.ipynb) | Chapter 6 |
| 3 | [02 — held-out evaluation (N24)](notebooks/02_heldout_evaluation_N24.ipynb) | Chapters 6–7 |
| 4 | [Final condition-level results](results/nb24_heldout_aggregate_by_condition.csv) and [paired contrasts](results/nb24_heldout_paired_contrasts.csv) | Chapter 7 |
| 5 | [Manual visual QC aggregates](results/nb24_manual_qc_aggregate.csv) | Chapter 7 |
| 6 | [Scientific audit / interpretation limits](docs/final_scientific_audit_nb24.md) | Chapters 8–10 |
| 7 | [Historical notebooks (original research archive)](https://github.com/menychtak/thesis_notes/tree/main/Notebooks/current) | Chapter 5 |

### Final experiment

108 held-out AffectNet+ face images × 3 processing conditions × seed 42 = **324 generated images**, confirmed in N23 and assessed in N24. The 12 development sources were excluded from this final comparison. For more details and exact limitations read the [scientific audit](docs/final_scientific_audit_nb24.md).

| Condition | ArcFace cosine ↓ | AuraFace cosine ↓ | Human-label FER accuracy ↑ | NIQE ↓ |
| --- | ---: | ---: | ---: | ---: |
| Emotion prompt, guidance 4.5 | 0.6557 | 0.6539 | 57.41% | 7.7020 |
| Emotion prompt, guidance 5.5 | 0.4565 | 0.4763 | 62.04% | 7.6126 |
| Same-expression prompt, guidance 4.5 | 0.5955 | 0.5903 | 16.67% | 7.8309 |

The **paired human-label FER change** (g5.5 minus g4.5) was **+4.63 percentage points**, with **95% CI [−2.78, +12.04] pp**. This does **not** establish a statistically reliable emotion-utility gain. Lower ArcFace/AuraFace cosine represents greater embedding difference, **not a measured re-identification risk**.

Human visual review covered 36 generated images from 12 sources, with one reviewer. It was a limited, deliberately selected subset and is not a whole-population estimate.

## Repository structure

```text
notebooks/
  01_heldout_generation_N23.ipynb
  02_heldout_evaluation_N24.ipynb
  history/N21_fer_evaluator_validation.ipynb
  README.md                           # map from thesis to every experiment
results/
  nb24_*                              # final PUBLIC aggregate statistics
  nb19_*, nb21_*, verified_n12_*       # historical public evidence, not final
  README.md
src/face_privacy/                     # reusable inference/evaluation modules
scripts/                              # historical provenance-check utility
tests/                                # small, data-free reproducibility tests
docs/                                 # scientific audit, protocol, import guidance
```

The `src/`, `scripts/`, and `tests/` directories are **supporting reproducibility code**, not extra experiments or evidence of better model performance. Keeping focused unit tests is standard responsible research engineering: they catch mistakes in paired comparisons and inference semantics without exposing any study images.

For lightweight verification (no private data, no GPU):
```bash
python -m pip install -e '.[test]'
pytest -q
```

Running the full notebooks requires licensed/private study inputs, pre-existing model checkpoints and a compatible Colab environment. **N23 and N24 have already been executed privately.** The notebooks in this repository are code copies; their outputs are intentionally not embedded.

See the [reproduction/completeness ledger](docs/reproduction_status.md) for the verified run status of every notebook family and outstanding archive imports.

## Original-image emotion-classifier baseline

The [original FER baseline summary](results/original_fer_baseline_120_and_108.csv) reports Accuracy and six-class/seven-class Macro-F1 separately for the initial 120 sources and the final 108 held-out sources. The 108-source figures were computed once per original source from saved N24 predictions, not 324 synthetic outputs. They provide essential context for interpreting FER changes after editing. This is a **post hoc aggregate extraction**, not newly executed model inference.

## Public evidence companion (Google Drive)

A curated [**N24 public-evidence release folder**](https://drive.google.com/drive/folders/1_2d0dJM4aUOxOEtR_bPsbM87gD_HptRF) contains **only** aggregated `N24_aggregate_by_condition.csv`, `N24_paired_contrasts.csv`, and the source-independent `N24_run_status.json`. These are redundant convenience copies: the same statistical evidence is publicly accessible in [`results/`](results/).

**Drive sharing note:** the folder has been created and its file contents checked, but anonymous/public access has **not** been verified. Its owner must set `General access → Anyone with the link → Viewer` before citing it as a publicly accessible release. The raw executed notebooks (some with embedded subject faces) and row-level data are **not** in this folder and must not be made public.

**Executed-notebook status:** original Colab notebooks with saved outputs exist for historical N19, N20, N22 and N22b (source links in [notebook index](notebooks/README.md)); the GitHub mirrors intentionally contain only code. The final N23/N24 Colab outputs were executed in private Drive runs and their aggregate measurements are linked here, but the code-only GitHub `.ipynb` files do not contain captured Jupyter cell outputs. Do not interpret a blank execution counter as an experiment that was never run; conversely, do not treat a report of successful execution as a publicly replayed result.

## Privacy and execution integrity

Original faces, generated images, source-level predictions/paths, full evaluation rows, ONNX weights and private output receipts are **not for a public repository**. Uploading an executed notebook without checking cell outputs can expose them. See the [safe notebook import checklist](docs/notebook_import_checklist.md).

The legacy experiment of 120 images / 600 outputs belongs to **N07**, not the final N23/N24 held-out analysis. This distinction also applies to the neutral-target pilot (N17–N18), which is **not** the final same-expression prompt.

**Scope of claims:** evidence of a biometric similarity/FER trade-off using fixed evaluators; no face-identification gallery attacks, calibrated privacy thresholds, multi-seed final sensitivity study, or clinical validation.

## Restricted Visual Comparisons — Access by Request

[View the 108-source comparison archive](https://drive.google.com/drive/folders/1w4eKRqp5xhtAlVU94y78mnOY7Ui4_Euk)

The private Google Drive archive contains 108 triplets (324 images), each consisting of the original face and the generated outputs using guidance 4.5 and 5.5.

Access is restricted. Thesis supervisors and examiners may request Viewer access from the author. Original facial images are not publicly accessible.

## Supplementary expression-preservation analysis (N25)

The [executed N25 AU evaluation notebook](notebooks/03_heldout_au_evaluation_N25.ipynb) retains execution counts and text-only result outputs; widget and image outputs have been excluded from the GitHub copy. [Condition-level AU metrics](results/nb25_au_aggregate.csv), [paired bootstrap contrasts](results/nb25_au_paired_contrasts.csv), and [run status](results/nb25_au_run_status.json) are public aggregate artifacts. N25 evaluates 108 originals and 324 generated images with Py-Feat Detectorv2; 431/432 images yielded valid AU estimates and 107/108 source pairs per condition were valid. This is **post-hoc model-estimated AU evidence, not manually coded FACS or clinical validation**. Row-level outputs remain in private Google Drive.
