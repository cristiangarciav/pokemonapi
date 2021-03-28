from flask_restful import Resource
from flask import request
from src.resources.pokemon import Pokemon, PokemonException, \
     get_moves_in_language, is_valid_language


def get_deal_damage(fighter: Pokemon, contender: Pokemon) -> int:
    max_damage = 0
    for f_type in fighter.types:
        damage_relations = fighter.get_damage_relations(f_type)
        multiplier = 1
        for d_type in damage_relations.keys():
            if d_type in contender.types:
                multiplier *= damage_relations[d_type]
        if multiplier > max_damage:
            max_damage = multiplier
    return max_damage


class ComparePokemon(Resource):
    def get(self) -> tuple:
        status_code = 405
        response = ({"Error": "method not allowed"}, status_code)
        return response

    def post(self) -> tuple:
        posted_data = request.get_json()
        if 'fighter' not in posted_data or 'contender' not in posted_data:
            status_code = 405
            response = ({"Error": "malformed request"}, status_code)
            return response

        fighter_id = str(posted_data['fighter'])
        contender_id = str(posted_data['contender'])

        try:
            fighter = Pokemon(fighter_id)
            contender = Pokemon(contender_id)
            status_code = 200

            response_data = {
                "fighter": {
                    "name": fighter.name,
                    "id": fighter.id,
                    "types": list(fighter.types),
                    "deal_damage": get_deal_damage(
                        fighter, contender),
                    "receive_damage": get_deal_damage(
                        contender, fighter),
                }
            }
            response = (response_data, status_code)
            return response
        except PokemonException as e:
            response_data = {"Error": e.message}
            status_code = 424
            response = (response_data, status_code)
            return response


class CommonMoves(Resource):
    def get(self) -> tuple:
        '''Function that process the get requests
        from CommonMoves API resource'''
        status_code = 405
        response = ({"Error": "method not allowed"}, status_code)
        return response

    def post(self) -> tuple:
        '''Function that process the post requests
        from CommonMoves API resource'''

        # Getting the json data from the post request
        posted_data = request.get_json()
        # Validating that mandatory variables have been passed
        # correctly in the expected format
        if ('pokemonList' not in posted_data) or (
            type(posted_data['pokemonList']) != list) or (
            ('limit' in posted_data) and (posted_data['limit'] != '*') and (
             not posted_data['limit'].isnumeric())
                ):
            status_code = 405
            response = ({"Error": "malformed request"}, status_code)
            return response
        # By default the language = 'en' and there is no limit
        language = 'en'
        limit = '*'
        if 'language' in posted_data:
            language = posted_data['language']
        if 'limit' in posted_data:
            limit = posted_data['limit']

        if language != 'en' and not is_valid_language(language):
            return ({"Error": "Invalid Language code"}, 405)

        pokemon_list = posted_data['pokemonList']

        try:
            moves_list = []
            for poke_id in pokemon_list:
                pokemon = Pokemon(poke_id)
                moves_list.append(pokemon.moves)

            common_moves = set.intersection(*moves_list)
            status_code = 200
            common_moves = list(common_moves)
            common_moves.sort()
            if limit != '*':
                limit = int(limit)
                print(f'limit: {limit}')
                common_moves = common_moves[:limit]

            if language != 'en':
                common_moves = get_moves_in_language(
                    common_moves, language)

            response_data = {
                "commonMoves": common_moves
            }
            response = (response_data, status_code)
            return response
        except PokemonException as e:
            response_data = {"Error": e.message}
            status_code = 424
            response = (response_data, status_code)
            return response
