"""Original N07 two-model FER ensemble — must replay before claiming N17 utility.

N07: softmax per ViT, canonicalize id2label, average class probabilities
across both frozen models, argmax ensemble. Preservation = predicted
generated emotion == human target (NOT agreement with original prediction).
"""
from __future__ import annotations

FER_MODELS = {
    "trpakov/vit-face-expression": "ef0bc6fc34241b6587e7e009e7711357be28c024",
    "mo-thecreator/vit-Facial-Expression-Recognition": "5aae4f09e1da247eb0f1c1e6f53271601fcafe09",
}
CANONICAL = {"anger":"angry","happiness":"happy","sadness":"sad",
             "surprised":"surprise","fearful":"fear","neutrality":"neutral",
             "disgusted":"disgust"}

def canonical_emotion(label: str) -> str:
    value = str(label).strip().lower()
    return CANONICAL.get(value, value)

def ensemble_distribution(per_model: dict[str,dict[str,float]]) -> dict[str,float]:
    if set(per_model) != set(FER_MODELS):
        raise ValueError("N07 requires BOTH exact frozen ViT evaluators")
    labels = sorted(set().union(*(set(dist) for dist in per_model.values())))
    return {label: sum(dist.get(label, 0.0) for dist in per_model.values()) / len(per_model)
            for label in labels}

def ensemble_prediction(per_model: dict[str,dict[str,float]]) -> str:
    distribution = ensemble_distribution(per_model)
    return max(distribution, key=distribution.get)

def load_frozen_ensemble(device="cpu"):
    from transformers import AutoImageProcessor, AutoModelForImageClassification
    result={}
    for model_id, revision in FER_MODELS.items():
        processor=AutoImageProcessor.from_pretrained(model_id,revision=revision)
        model=AutoModelForImageClassification.from_pretrained(model_id,revision=revision)
        model.eval().to(device)
        result[model_id]=(processor,model)
    return result

def predict_distribution(image, components, device="cpu"):
    import torch
    distributions={}
    for model_id, (processor, model) in components.items():
        inputs=processor(images=image,return_tensors="pt").to(device)
        with torch.inference_mode():
            probs=torch.softmax(model(**inputs).logits,dim=-1)[0]
        dist={}
        for index,probability in enumerate(probs):
            label=canonical_emotion(model.config.id2label[index])
            dist[label]=dist.get(label,0.0)+float(probability.item())
        distributions[model_id]=dist
    return ensemble_distribution(distributions)

def predict_path(path, components, device="cpu"):
    from PIL import Image
    with Image.open(path) as im:
        image=im.convert("RGB")
        dist=predict_distribution(image,components,device=device)
    return max(dist,key=dist.get),dist
