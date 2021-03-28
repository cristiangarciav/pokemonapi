from src.resources.pokemon import PokeResource
from mock_data import write_resource_mock_data


if __name__ == '__main__':
    '''
    pokemon_list = ['pikachu', 'grumpig', 'drapion', 'charmander', 'arceus']
    for pokemon_id in pokemon_list:
        write_resource_mock_data(PokeResource.pokemon, pokemon_id)

    type_list = ['electric', 'dark', 'poison']
    for type_id in type_list:
        write_resource_mock_data(PokeResource.type, type_id)
    move_list = ['attract', 'brick-break', 'bulldoze']
    for move_id in move_list:
        write_resource_mock_data(PokeResource.move, move_id)
    '''
    lang_id = 'es'
    write_resource_mock_data(PokeResource.language, lang_id)
