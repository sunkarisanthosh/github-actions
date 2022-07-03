

import os
import sys

import pytest
from airflow.models import DagBag

sys.path.append(os.path.join(os.path.dirname(__file__), "../dags"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../dags/utilities"))



@pytest.fixture(params=["../dags/"])
def dag_bag(request):
    return DagBag(dag_folder=request.param, include_examples=False)





def test_desc_len_greater_than_fifteen():
    for dag_id, dag in dag_bag.dags.items():
        assert len(dag.description) > 100


