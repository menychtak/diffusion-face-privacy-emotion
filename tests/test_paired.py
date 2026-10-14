import pandas as pd
import pytest
from face_privacy.paired import strict_pair, cluster_bootstrap_delta
from face_privacy.provenance import require_exact_fer_provenance

def test_pair_is_1_to_1():
    a=pd.DataFrame({"source_id":["a","b"],"seed":[42,42],"value":[1,2]})
    b=pd.DataFrame({"source_id":["b","a"],"seed":[42,42],"metric":[3,4]})
    assert len(strict_pair(a,b,columns=["metric"])) == 2

def test_pair_refuses_duplicate():
    a=pd.DataFrame({"source_id":["a","a"],"seed":[42,42]})
    with pytest.raises(ValueError, match="duplicate"):
        strict_pair(a,a,columns=[])

def test_source_cluster_bootstrap_deterministic():
    d=pd.DataFrame({"source_id":["a","a","b","b"],"seed":[42,123]*2,"delta":[1.,1.,3.,3.]})
    assert cluster_bootstrap_delta(d,"delta",draws=100,seed=12)==cluster_bootstrap_delta(d,"delta",draws=100,seed=12)

def test_incomplete_fer_blocks_release():
    with pytest.raises(ValueError):
        require_exact_fer_provenance(pd.DataFrame())
