# Reproduction & completeness audit (2026-10-15)

This is a **status ledger**, not a claim that every historical notebook has been replayed from a fresh environment.

| Artifact | Code in this repo? | Existing execution evidence | Need to run now? | Public status |
| --- | --- | --- | --- | --- |
| N23 held-out generation | **Yes:** notebooks/01_heldout_generation_N23.ipynb | Completed private Drive run, 324/324 outputs and receipts | **No** | Source-only notebook + public run description |
| N24 held-out evaluation | **Yes:** notebooks/02_heldout_evaluation_N24.ipynb | Completed private Drive run, 324/324 metrics and 108/108 source FER replay | **No** | Source-only notebook + aggregate results |
| Limited manual QC | Public aggregate in results/ | 36 original/generated comparisons in private checklist | **No** | Review protocol + limited aggregate |
| N21 FER evaluator audit | Yes, notebooks/history/ | Private run artifact reported; original cell outputs absent from GitHub | **No**, unless specifically verifying a different environment | Historic source-only |
| N10–N18 evaluator development | Yes, selected sanitized source notebooks in notebooks/history/ | Some original notebooks contain executed cells; these imported versions were stripped of outputs | **No** for the final held-out conclusions | Historic code-only with provenance |
| N01–N07 initial experiments | Source remains at [thesis_notes](https://github.com/menychtak/thesis_notes/tree/main/Notebooks/current) | Previous development runs and private output folders | **No** for final NB24 claims | Linked historical source; not mirrored due to embedded private/large outputs |
| N19, N20, N22, N22b | **Yes:** verified source-only copies in notebooks/history/ | Original Colab files found with saved execution metadata; N19 initial attempt incomplete, patched N19 executed; N22 includes sensitive visual outputs | **No** for final NB24 claims | Source provenance resolved; cell outputs intentionally private |

## Outstanding publication tasks

- [x] Rename final generation/evaluation notebooks to follow actual run order.
- [x] Separate historical experiments from final held-out code.
- [x] Mirror selected small historical evaluator notebooks after stripping outputs; preserve original N numbers in filenames.
- [x] Publish final aggregate results and a claim-level scientific audit.
- [x] Keep data-free tests / reusable implementation code distinct from notebooks.
- [ ] Retrieve and verify original **executed notebook files**, if publication of executed notebooks is desired. Private Drive *run folders* do not by themselves establish that an `.ipynb` with saved executed outputs is present.
- [ ] Safely extract large N01–N07 code if the thesis committee requires everything physically copied into a single GitHub repository. Avoid copying image-rich notebooks verbatim.
- [x] Locate original N19/N20/N22/N22b notebook files in Colab and publish source-only copies. N19 initial failed/incomplete attempt remains linked but not duplicated.
- [ ] Obtain a private-data-safe independent end-to-end re-execution if requested by examiners. **Not required to report the already executed N23/N24 results.**

## How to cite / present

In the thesis, cite the experimental method in Chapter 6, the results CSVs in Chapter 7, and the claim-level audit / limits in Chapters 8–10. Include repository link and exact commit SHA in the thesis submission record if the supervisor requires immutable provenance. Source code should not be represented as an executed notebook when its Jupyter execution counts and outputs are empty.

**Privacy:** private AffectNet images, generated faces, private CSVs, source identifiers, weights and unsanitized executed notebook outputs should stay in access-controlled storage.

## Verified existing private Drive evidence locations

- [N19 output folder](https://drive.google.com/drive/folders/15Ue0AeJaVM_beET4K5nqfkEPWrqUSLEP) — biometrics evaluation outputs, **not** an executed ipynb.
- [N20 output folder](https://drive.google.com/drive/folders/1NZ_TBCKhCx6wEfdX-0-EQfMowVI5lUke) — exact N07 FER replay and audit exports, **not** an executed ipynb.
- [N21 output folder](https://drive.google.com/drive/folders/1XUibLwJ4nVIGHypNeHa5j_og60E1tgYv).
- [N23 final generated images/receipts](https://drive.google.com/drive/folders/1KxDi4nMPp1NHFZjXIW6ZYC5Ra_7QeETf).
- [N24 final metrics/results](https://drive.google.com/drive/folders/1QWD9rYEPQvXKTq-VZpSMiX2_Ofg3TTgn).
- [May historical N01–N03 original notebook directory](https://drive.google.com/drive/folders/1wFo30IZiNIjkQil_IFpFUmkGDuUqot-Y) (older filenames and snapshots; inspect before associating one-to-one with canonical N-series).
- [June historical N01–N06 notebook directory](https://drive.google.com/drive/folders/1TTc6n5S_-TGrRokTNYzmZuERE9_4FquF) (some `.ipynb` files are multi-megabyte with embedded outputs; **contains other sensitive files** and must not be shared or mirrored wholesale).

Drive folder search did not locate exported `.ipynb` for N23–N24; **original Colab files for N19/N20/N22/N22b were subsequently supplied and verified**. A run folder proves there are output artifacts, but **not** that the notebook file itself has a saved executed state. The original Colab notebook is the appropriate place to export the executed `.ipynb` if one is needed by examiners.

## Original Colab artifacts found on 2026-10-15

- [N19 initial incomplete attempt](https://colab.research.google.com/drive/1qAcSZRxxrcYdNhP_XcwYhKGIt1tRrz9s).
- [N19 corrected executed version](https://colab.research.google.com/drive/1eZ4Gs2pvxGhZGR16YZdo9TpQm0J0_iSO).
- [N20 executed replay/provenance notebook](https://colab.research.google.com/drive/1aLijvkD01S49PqPe0QkVykSDtG8W7QTc).
- [N22 historical private manual-alignment QC](https://colab.research.google.com/drive/1SE_i4IK8KZpq7sFR7v6MZRMUQi50PaXL) (**24 historic pairing cases**, contains embedded face imagery).
- [N22b provisional AI-assisted QC](https://colab.research.google.com/drive/1hCe1m19eJ0qTjBDEdZTO3UvzKx4ToDw8) (not the final NB24 human QC).

Their safe source-only notebook copies live in [notebooks/history](../notebooks/history/). Original Colab execution cells were not replicated on the public repository. Do not conflate N22's historic pairs with the final 36-image NB24 human-review sample.
