# Reproduction & completeness audit (2026-10-15)

This is a **status ledger**, not a claim that every historical notebook has been replayed from a fresh environment.

| Artifact | Code in this repo? | Existing execution evidence | Need to run now? | Public status |
| --- | --- | --- | --- | --- |
| N23 held-out generation | **Yes:** notebooks/01_heldout_generation_N23.ipynb | Completed private Drive run, 324/324 outputs and receipts | **No** | Source-only notebook + public run description |
| N24 held-out evaluation | **Yes:** notebooks/02_heldout_evaluation_N24.ipynb | Completed private Drive run, 324/324 metrics and 108/108 source FER replay | **No** | Source-only notebook + aggregate results |
| Limited manual QC | Public aggregate in results/ | 36 original/generated comparisons in private checklist | **No** | Review protocol + limited aggregate |
| N21 FER evaluator audit | Yes, notebooks/history/ | Private run artifact reported; original cell outputs absent from GitHub | **No**, unless specifically verifying a different environment | Historic source-only |
| N11–N18 evaluator development | Yes, selected sanitized source notebooks in notebooks/history/ | Some original notebooks contain executed cells; these imported versions were stripped of outputs | **No** for the final held-out conclusions | Historic code-only with provenance |
| N01–N07 initial experiments | Source remains at [thesis_notes](https://github.com/menychtak/thesis_notes/tree/main/Notebooks/current) | Previous development runs and private output folders | **No** for final NB24 claims | Linked historical source; not mirrored due to embedded private/large outputs |
| N19, N20, N22 | Not verified as canonical notebooks in this repo | Historical exports/protocol may exist; executed notebook bytes unverified | **Do not rerun solely to fill numbering** | **Outstanding artifact discovery** |

## Outstanding publication tasks

- [x] Rename final generation/evaluation notebooks to follow actual run order.
- [x] Separate historical experiments from final held-out code.
- [x] Mirror selected small historical evaluator notebooks after stripping outputs; preserve original N numbers in filenames.
- [x] Publish final aggregate results and a claim-level scientific audit.
- [x] Keep data-free tests / reusable implementation code distinct from notebooks.
- [ ] Retrieve and verify original **executed notebook files**, if publication of executed notebooks is desired. Private Drive *run folders* do not by themselves establish that an `.ipynb` with saved executed outputs is present.
- [ ] Safely extract large N01–N07 code if the thesis committee requires everything physically copied into a single GitHub repository. Avoid copying image-rich notebooks verbatim.
- [ ] Verify whether canonical N19/N20/N22 notebook files are available in Colab or private storage; do not fabricate missing notebooks.
- [ ] Obtain a private-data-safe independent end-to-end re-execution if requested by examiners. **Not required to report the already executed N23/N24 results.**

## How to cite / present

In the thesis, cite the experimental method in Chapter 6, the results CSVs in Chapter 7, and the claim-level audit / limits in Chapters 8–10. Include repository link and exact commit SHA in the thesis submission record if the supervisor requires immutable provenance. Source code should not be represented as an executed notebook when its Jupyter execution counts and outputs are empty.

**Privacy:** private AffectNet images, generated faces, private CSVs, source identifiers, weights and unsanitized executed notebook outputs should stay in access-controlled storage.
