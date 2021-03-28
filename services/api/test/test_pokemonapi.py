# from src.resources.pokemon import ComparePokemon
from src.app import app
from mock_data import read_resource_mock_data
import pytest
import responses
# import requests
from src.resources.pokemon import Pokemon, PokeResource
import json
from flask.testing import FlaskClient


@pytest.fixture
def client() -> FlaskClient:
    '''Gets the testing FlaskClient from the flask app instance'''
    return app.test_client()


# Testing GET methods:


def test_get_compare_damage(client: FlaskClient) -> None:
    '''Test the compare_damage endpoint. It should return 405 status code
        the get method is not allowed
    '''
    url = '/compare_damage'
    response = client.get(url)
    assert response.status_code == 405
    assert response.content_type == 'application/json'
    assert b'Error' in response.data


# Testing POST methods:


def test_get_common_moves(client: FlaskClient) -> None:
    '''Test the common_moves endpoint. It should return 405 status code
        the get method is not allowed
    '''
    url = '/common_moves'
    response = client.get(url)
    assert response.status_code == 405
    assert response.content_type == 'application/json'
    assert b'Error' in response.data


@responses.activate
def test_simulate_create_pokemon() -> None:
    '''Mock the pokeapi response in order to simulate
       the Pokemon class instance'''
    pokeid = 'pikachu'
    resource = PokeResource.pokemon
    api_url = 'https://pokeapi.co/api/v2'
    api_url += f'/{resource.name}/{pokeid}/'
    # Reading the mock data from a data file
    data = read_resource_mock_data(resource, pokeid)
    responses.add(
        responses.GET,
        api_url,
        json=data,
        status=200
    )
    fighter = Pokemon(pokeid)
    assert fighter.name == 'pikachu'
    assert fighter.id == 25
    assert 'electric' in fighter.types


def test_post_malformed_compare_damage_request(client: FlaskClient) -> None:
    '''Test a malformed request to the compare_damage endpoint
       by ommiting the "contender" variable
    '''
    data = {
        "fighter": "pikachu"
    }
    mime_type = "application/json"
    headers = {
        "Content-Type": mime_type,
        "Accept": mime_type
    }
    url = "/compare_damage"
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 405
    assert response.content_type == 'application/json'
    assert b'Error' in response.data


@responses.activate
def test_post_compare_damage_not_found(client: FlaskClient) -> None:
    ''' '''
    resource_id = 'pikachuasdf'
    resource = PokeResource.pokemon
    api_url = 'https://pokeapi.co/api/v2'
    api_url += f'/{resource.name}/{resource_id}/'
    response_data = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <title>Error</title>
        </head>
        <body>
        <pre>Cannot POST /api/v2/pokemon/pikachuasdf</pre>
        </body>
        </html>
    """
    responses.add(
        responses.GET,
        api_url,
        json=response_data,
        status=404
    )

    data = {
        "fighter": "pikachuasdf",
        "contender": "drapion"
    }
    mime_type = "application/json"
    headers = {
        "Content-Type": mime_type,
        "Accept": mime_type
    }
    url = "/compare_damage"
    response = client.post(url, data=json.dumps(data), headers=headers)
    json_data = json.loads(response.data)
    assert response.status_code == 424
    assert response.content_type == 'application/json'
    assert {"Error": "pikachuasdf is not a pokemon"} == json_data


@responses.activate
def test_post_compare_damage_request(client: FlaskClient) -> None:
    pokemon_list = ['pikachu', 'drapion']
    resource = PokeResource.pokemon
    for resource_id in pokemon_list:
        api_url = 'https://pokeapi.co/api/v2'
        api_url += f'/{resource.name}/{resource_id}/'
        resource_data = read_resource_mock_data(resource, resource_id)
        responses.add(
            responses.GET,
            api_url,
            json=resource_data,
            status=200
        )
    type_list = ['electric', 'dark', 'poison']
    resource = PokeResource.type
    for resource_id in type_list:
        api_url = 'https://pokeapi.co/api/v2'
        api_url += f'/{resource.name}/{resource_id}/'
        resource_data = read_resource_mock_data(resource, resource_id)
        responses.add(
            responses.GET,
            api_url,
            json=resource_data,
            status=200
        )

    expected_data = {
        "fighter": {
            "name": "pikachu",
            "id": 25,
            "types": [
                "electric"
            ],
            "deal_damage": 1,
            "receive_damage": 1
        }
    }
    data = {
        "fighter": "pikachu",
        "contender": "drapion"
    }
    mime_type = "application/json"
    headers = {
        "Content-Type": mime_type,
        "Accept": mime_type
    }
    url = "/compare_damage"
    response = client.post(url, data=json.dumps(data), headers=headers)
    json_data = json.loads(response.data)
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert expected_data == json_data
