#!/usr/bin/python3

import pytest
from api.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_recommend(client):
    response = client.get('/recommend/1?n=2')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 2
