from src.resources.pokemon import get_resource, PokeResource
import json
import os


# Generic functinons necessary to read and write some json data
# from the Poke Api.

def get_path() -> str:
    try:
        path = os.environ['PYTHONPATH'].split(os.pathsep)[0]
    except KeyError:
        path = ''
    mock_path = os.path.join(path, "test/mock_data")
    return mock_path


def write_resource_mock_data(resource: PokeResource, resource_id: str) -> None:
    file_path = get_path()
    filename = f'{file_path}/{resource.name}_{resource_id}_mock.json'
    mock_data = get_resource(resource, resource_id)
    with open(filename, 'w') as outfile:
        json.dump(mock_data, outfile)


def read_resource_mock_data(resource: PokeResource, resource_id: str) -> dict:
    file_path = get_path()
    filename = f'{file_path}/{resource.name}_{resource_id}_mock.json'
    with open(filename) as json_file:
        data = json.load(json_file)
        return data
