# Facial Identity Obfuscation with Pretrained Diffusion Models

**MSc Thesis · University of Piraeus · Python / Google Colab**

This research investigates whether a pretrained image-editing model can modify facial identity while preserving information relevant to facial emotion recognition. It examines the **privacy–utility–quality trade-off** using FlowEdit with Stable Diffusion 3 Medium, without additional training of the generative model.

The study measures changes in biometric face representations, facial emotion recognition, and image quality. It does not claim guaranteed anonymity or clinical suitability.

## Research approach

The experimental workflow has three stages:

1. **Face editing:** FlowEdit generates alternative facial appearances using source/target text prompts and controlled guidance settings.
2. **Identity assessment:** ArcFace and AuraFace compare biometric embeddings of original and edited faces.
3. **Expression and quality assessment:** A fixed two-ViT emotion classifier, NIQE, a limited visual review, and supplementary facial Action Unit (AU) estimates examine what changes beyond identity.

The final evaluation uses **108 AffectNet+ source images**, excluding 12 sources used during development. Three editing conditions were applied to each source with seed 42, producing **324 synthetic images**.

## Main results

| Editing condition | ArcFace cosine ↓ | AuraFace cosine ↓ | Emotion accuracy ↑ | NIQE ↓ |
| --- | ---: | ---: | ---: | ---: |
| Emotion prompt · guidance 4.5 | 0.6557 | 0.6539 | 57.41% | 7.7020 |
| Emotion prompt · guidance 5.5 | 0.4565 | 0.4763 | 62.04% | 7.6126 |
| Same-expression prompt · guidance 4.5 | 0.5955 | 0.5903 | 16.67% | 7.8309 |

Higher guidance (5.5) reduced mean biometric similarity relative to 4.5. Emotion accuracy was 4.63 percentage points higher, but the paired 95% confidence interval (**−2.78 to +12.04 percentage points**) did not establish a statistically reliable improvement.

A supplementary evaluation of 20 facial AUs found valid estimates for 431 of 432 original and synthetic images, with 107 valid source-output pairs per condition. A separate visual review examined 36 generated images from 12 sources.

**Interpretation:** Lower biometric cosine similarity indicates an embedding change, not a measured re-identification probability. Matching an emotion category does not necessarily mean preserving the source's precise facial expression.

## Code and results

| Resource | Description |
| --- | --- |
| [Generation notebook (N23)](notebooks/01_heldout_generation_N23.ipynb) | Final FlowEdit generation protocol |
| [Evaluation notebook (N24)](notebooks/02_heldout_evaluation_N24.ipynb) | Biometric, emotion, and image-quality evaluation |
| [AU evaluation notebook (N25)](notebooks/03_heldout_au_evaluation_N25.ipynb) | Supplementary expression analysis |
| [Executed results report](notebooks/03_executed_public_results_report.ipynb) | Recalculates descriptive summaries from published aggregates |
| [Results](results/README.md) | Aggregate results, paired comparisons, baseline and AU summaries |
| [Notebook index](notebooks/README.md) | Development history and mapping of experiments to thesis chapters |
| [Scientific audit](docs/final_scientific_audit_nb24.md) | Methodological assumptions, evidence and interpretation limits |

The main experimental results are available in [condition-level aggregates](results/nb24_heldout_aggregate_by_condition.csv) and [paired contrasts](results/nb24_heldout_paired_contrasts.csv). Additional files include the [original-image FER baseline](results/original_fer_baseline_120_and_108.csv), [visual review aggregates](results/nb24_manual_qc_aggregate.csv), and [AU analysis](results/nb25_au_aggregate.csv).

## Repository layout

```text
notebooks/          Final experiment notebooks and historical research notebooks
results/            Aggregate metrics and statistical summaries
src/face_privacy/   Reusable evaluation and provenance utilities
tests/              Data-independent unit tests
scripts/            Research support scripts
docs/               Protocols, experiment records, and scientific audits
```

### Environment and execution

The reusable package and its lightweight tests can be installed and run without private images or a GPU:

```bash
python -m pip install -e '.[test]'
pytest -q
```

Full experiment execution requires appropriately licensed AffectNet+ data, compatible model checkpoints, and a suitable GPU/Colab environment. The N23 and N24 experiments were executed in the research environment; their public notebooks contain source code without embedded image outputs. The executed public results report reproduces *aggregate calculations*, not image generation or model inference.

For environment guidance and detailed execution status, see [Colab setup](docs/colab.md) and [reproduction status](docs/reproduction_status.md).

## Data availability and research scope

AffectNet+ is subject to its own data-use agreement. This repository does **not** distribute the original face images, generated facial images, identifiable source mappings, or subject-level evaluation records. Publicly released results are aggregated. A separate [aggregate evidence folder](https://drive.google.com/drive/folders/1_2d0dJM4aUOxOEtR_bPsbM87gD_HptRF) provides convenience copies of selected N24 summaries.

The study evaluates a selected set of static facial images and fixed pretrained evaluators. It does not include calibrated face re-identification attacks, external clinical validation, or multi-seed sensitivity analysis of the final 108-source experiment. Further methodological details and limitations are documented in the [scientific audit](docs/final_scientific_audit_nb24.md).
