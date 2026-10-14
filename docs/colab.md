# Colab / Drive execution contract

Do **not** rerun the 600 N07 images or the 24 N17 diffusion images by
default. Read existing paths in `/content/drive/MyDrive/thesis_all/outputs/runs`.

In Colab:
```python
from google.colab import drive
drive.mount('/content/drive')
!pip -q install 'git+https://github.com/menychtak/diffusion-face-privacy-emotion.git'
from pathlib import Path
import pandas as pd
from face_privacy.provenance import verify_generation_receipts
root=Path('/content/drive/MyDrive/thesis_all/outputs/runs')
n17=root/'nb17v2_neutral_expression_12sources_2seeds_sd3pinned'
verify_generation_receipts(pd.read_csv(n17/'private_execution_receipts.csv'))
print('Verified: 24 archived generated images, no generation performed')
```

The full FER release gate stays closed until its original classifier artifact
and preprocessing have been verified. Do not use a substitute pretrained
emotion model or infer labels from the prompt.
