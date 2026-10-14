# Diffusion Face Privacy & Emotion Preservation

A reproducible Master's thesis research implementation for **diffusion-based facial identity obfuscation** while evaluating retention of facial-expression/emotion information, with potential healthcare research applications.

## Status (14 October 2026)

- **Generation**: Frozen N07 larger AffectNet experiment, 120 sources / 600 generated images. Frozen N17 v2 neutral-target ablation, 12 sources × 2 seeds = 24/24 images.
- **Biometrics**: N12 V3 corrected ArcFace / AuraFace for N07; N19 evaluated 24/24 N17 v2 outputs using the frozen weight hashes and geometry.
- **Image statistics**: N16 + N18/N19 NIQE evaluated. Pilot differences are exploratory (12 independent sources).
- **Emotion**: N07 FER historical scores exist. **N17 v2 exact FER evaluation is still pending**, not imputed.
- **Manual checks**: N17 visual validity and alignment review not yet completed. No calibrated identity re-identification risk or clinical utility claim.

## Getting started

```bash
git clone https://github.com/menychtak/diffusion-face-privacy-emotion.git
cd diffusion-face-privacy-emotion
python -m pip install -e '.[test]'
pytest -q
```

For a Colab Drive hash-verification smoke test, see [docs/colab.md](docs/colab.md). For experimental lineage and limitations see [docs/evidence.md](docs/evidence.md). The currently verified aggregate pilot numbers are in [results/nb19_public_summary.csv](results/nb19_public_summary.csv).

## Scientific integrity

No participant face images, raw biometric rows, checkpoints, or potentially identifying manifests are stored in this public repository. Private evidence remains in the original Google Drive output directories. ArcFace/AuraFace cosines are similarities, not re-identification probabilities; NIQE is not a measure of expression preservation. Claims remain gated on frozen evaluator provenance and actual executed outputs.

## Historical research

Exploration and executed Colab notebooks: [menychtak/thesis_notes](https://github.com/menychtak/thesis_notes). This repository is the clean implementation and validated evidence layer, not an assertion that every experiment has been reproduced from scratch.
