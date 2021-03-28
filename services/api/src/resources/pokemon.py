import requests
from enum import Enum


class PokeResource(Enum):
    """
    Enumeration for the supported API resources
    """
    pokemon = 1
    type = 2
    move = 3
    language = 4


class PokemonException(Exception):
    """Exception raised for errors related to the Pokemon Class.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="Error in the Pokemon class") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'PokemonException: {self.message}'


class Pokemon:
    def __init__(self, pokeid: str) -> None:
        if pokeid != "" and pokeid is not None:
            result = self.get_pokemon(pokeid)
            self.name = result['name']
            self.id = result['id']
            self.types = self.get_resource_names(
                PokeResource.type, result['types'])
            self.moves = self.get_resource_names(
                PokeResource.move, result['moves'])
        else:
            error_msg = "Pokemon name/id cannot be an empty string."
            raise PokemonException(error_msg)

    def get_pokemon(self, pokeid: str) -> dict:
        '''Simple wrapper for get_resource '''
        return get_resource(PokeResource.pokemon, pokeid)

    def get_resource_names(self, resource: PokeResource,
                           result_types: list) -> dict:
        """
        Returns the pokemon's "resources" as a set of strings
        based on the API result
        """
        return {str(item[resource.name]['name']) for item in result_types}

    def get_damage_relations(self, type_id: str) -> dict:
        multiplier_damage = {
            'no_damage_to': 0,
            'half_damage_to': 0.5,
            'double_damage_to': 2
        }
        dmg_rel = {}
        result_type = get_resource(PokeResource.type, type_id)
        relations = result_type['damage_relations']
        for rel in relations:
            if rel in multiplier_damage:
                for p_type in relations[rel]:
                    rel_type = p_type['name']
                    dmg_rel[rel_type] = multiplier_damage[rel]
        return dmg_rel


def get_resource(resource_type: PokeResource, id_type: str) -> dict:
    """
    A wrapper for request.get to validate the response
    """
    if type(id_type) == str:
        id_type = id_type.lower()
    api_url = 'https://pokeapi.co/api/v2'
    request_str = api_url + f'/{resource_type.name}/{id_type}/'
    try:
        result = requests.get(request_str)
    except requests.exceptions.RequestException as e:
        print(e)
        error = "Error while trying to connect to the PokeApi"
        raise PokemonException(error)

    if result.ok:
        return result.json()
    else:
        error_msg = f'{id_type} is not a {resource_type.name}'
        raise PokemonException(error_msg)


def get_moves_in_language(moves: list, lang: str) -> list:
    translated_moves = []
    for move_id in moves:
        result_names = get_resource(PokeResource.move, move_id)['names']
        for name in result_names:
            if name['language']['name'] == lang:
                translated_moves.append(name['name'])
    return translated_moves


def is_valid_language(lang_id: str) -> bool:
    try:
        get_resource(PokeResource.language, lang_id)
        return True
    except PokemonException:
        return False
