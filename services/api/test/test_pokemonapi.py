# from src.resources.pokemon import ComparePokemon
from src.app import app
import pytest
# import json


@pytest.fixture
def client():
    return app.test_client()


def test_compare(client):
    '''Testing the compare end point. It should return de comparation list'''
    url = '/compare'
    response = client.get(url)
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert b'message' in response.data
