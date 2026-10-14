import pytest
from face_privacy.fer import FER_MODELS, ensemble_prediction, ensemble_distribution

def test_mean_probabilities_not_majority_vote():
    a,b=list(FER_MODELS)
    d={a:{"happy":0.9,"sad":0.1},b:{"happy":0.2,"sad":0.8}}
    assert ensemble_prediction(d)=="happy"
    assert ensemble_distribution(d)["happy"]==pytest.approx(0.55)

def test_missing_secondary_classifier_is_blocker():
    a=list(FER_MODELS)[0]
    with pytest.raises(ValueError,match="BOTH"):
        ensemble_prediction({a:{"happy":1.0}})
