import os
import sys

import pytest
from airflow.models import DagBag

def test_desc_len_greater_than_fifteen(dag_bag):
    for dag_id, dag in dag_bag.dags.items():
        assert len(dag.description) > 15
