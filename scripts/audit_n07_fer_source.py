"""Extract the exact N07 FER inference code for a human-verifiable provenance audit.

N07 notebook embeds large outputs. Run in Colab (network enabled) or locally.
Print only code; do not upload images or per-person predictions.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import urllib.request
from pathlib import Path

URL = "https://raw.githubusercontent.com/menychtak/thesis_notes/main/Notebooks/current/07_affectnet_final_multi_image_evaluation.ipynb"
TERMS = re.compile(r"trpakov|emotion_model|original_predicted_class|AutoImageProcessor|AutoModelForImageClassification|ViTImageProcessor|id2label|image_processor|\.logits|softmax|FER", re.I)

def run(notebook_path: Path | None = None, out: Path | None = None):
    if notebook_path:
        data = notebook_path.read_bytes()
        origin = str(notebook_path)
    else:
        req = urllib.request.Request(URL, headers={"User-Agent":"thesis-fer-audit/1.0"})
        with urllib.request.urlopen(req,timeout=120) as response:
            data = response.read()
        origin = URL
    nb = json.loads(data)
    report = {
        "source": origin,
        "notebook_sha256": hashlib.sha256(data).hexdigest(),
        "cell_count": len(nb["cells"]),
        "candidate_cells": [],
    }
    for index, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        source = "".join(cell["source"])
        matches = list(TERMS.finditer(source))
        if matches:
            report["candidate_cells"].append({
                "cell_index": index,
                "matched_terms": sorted(set(m.group().lower() for m in matches)),
                "source": source,
            })
    print("N07 SHA-256:", report["notebook_sha256"])
    print("Relevant cells:", len(report["candidate_cells"]))
    for cell in report["candidate_cells"]:
        print(f"\n{'='*40} CELL {cell['cell_index']} {'='*40}")
        print(cell["source"][:25000])
    if out:
        out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(json.dumps(report,indent=2,ensure_ascii=False))
        print("Code-only local audit file:",out)
    print("\nGATE: EXTRACTED FOR SOURCE REVIEW; not yet proven identical to N20.")

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--notebook",type=Path,help="Local N07 notebook (optional)")
    p.add_argument("--out",type=Path,help="Local code-only audit JSON")
    a=p.parse_args()
    run(a.notebook,a.out)
