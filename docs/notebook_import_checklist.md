# Notebook import checklist (private Drive → public GitHub)

This project uses **actual execution evidence**, not simulated Jupyter execution counts.

1. Open the original notebook in Colab/Drive, verify it is the **same run** referenced in the thesis (source selection, output folder, models, seed, notebook ID).
2. Record whether code was executed: existing code cells alone are **not** evidence of an executed run; prefer original metadata, logs, receipts, and run status.
3. Before GitHub upload, **remove all embedded face images, image previews, personal/source identifiers, private Drive paths, authentication credentials, weight blobs, identifiable predictions, and row-level personal data**. Preserve only code and genuinely public aggregate tables/plots. Be aware output sanitization will remove some visible evidence; do not mislabel the redacted export as identical to the private original.
4. Match the canonical name and stage; do not reuse a filename for a different algorithm.
5. Link the final chapter/table and the corresponding public result CSV or status JSON.
6. Mark accurately as `source-only`, `executed (private artifact)`, or `public executed output verified`.

The [canonical notebook map](../notebooks/README.md) is the authoritative index. For N23/N24, the public source is sufficient while the original private Drive runs already substantiate the recorded aggregates.

**Missing artifacts:** if the executed notebook is only in the user's Google Colab or private Drive, it cannot be manufactured from the public repo. Provide the actual original Colab/Drive link or an exported `.ipynb`; then review and import it, preserving the original notebook ID in provenance.
