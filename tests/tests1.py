
import os
import sys

import pytest
from airflow.models import DagBag

def test_desc_len_greater_than_fifteen(dag_id):
    
        assert len(dag.description) > 15
