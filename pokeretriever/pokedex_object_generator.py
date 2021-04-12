import aiohttp

from .pokedex.pokedex_object import PokedexObject
from .pokedex.ability import Ability
from .pokedex.pokemon import Pokemon
from .pokedex.move import Move
from .pokedex.stat import Stat


async def generate_pokedex_object(poke_request, data) -> PokedexObject:
    """
    Creates a PokedexObject based on the request grabbed for it.
    :param poke_request: Request representing the object to create.
    :param data: JSON object containing Pokedex data from API.
    :return: PokedexObject
    """
    if poke_request.mode == "pokemon":
        return await generate_pokemon(poke_request, data)  # currently only pokemon support expanded mode
    elif poke_request.mode == "ability":
        return generate_ability(data)
    elif poke_request.mode == "move":
        return generate_move(data)
    elif poke_request.mode == "stat":
        return generate_stat(data)


async def generate_pokemon(poke_request, data):
    """
    Generate a Pokemon object based on API data.
    :param poke_request: Request, used to determine expanded mode status
    :param data: JSON object containing API data
    :return: Pokemon
    """

    list_of_abilities = []
    list_of_stats = []
    list_of_moves = [moves["move"]["name"]for moves in data["moves"]]
    if poke_request.is_expanded:
        try:
            for ability in data["abilities"]:
                async with aiohttp.ClientSession() as session:
                    async with session.get(ability["ability"]["url"]) as response:
                        ability_data = await response.json()
                        new_ability = generate_ability(ability_data)
                        list_of_abilities.append(new_ability.__str__())
                    await session.close()
        except Exception as e:
            print(e)

        try:
            for stat in data["stats"]:
                async with aiohttp.ClientSession() as session:
                    async with session.get(stat["stat"]["url"]) as response:
                        stat_data = await response.json()
                        new_stat = generate_stat(stat_data)
                        list_of_stats.append(new_stat.__str__())
                    await session.close()
        except Exception as e:
            print(e)
    else:
        list_of_abilities = [ability["ability"]["name"] for ability in data["abilities"]]
        list_of_stats = {stat["stat"]["name"]: str(stat["base_stat"]) for stat in data["stats"]}

    return Pokemon(height=data["height"],
                   weight=data["weight"],
                   stats=list_of_stats,
                   types=[types["type"]["name"] for types in data["types"]],
                   abilities=list_of_abilities,
                   moves=list_of_moves,
                   id=data["id"],
                   name=data["name"])


def generate_ability(data):
    """
    Generate an Ability object based on API data.
    :param data: JSON object containing API data
    :return: Ability
    """
    return Ability(generation=data["generation"]["name"],
                   effect=data["effect_entries"][1]["effect"],
                   effect_short=data["effect_entries"][1]["short_effect"],
                   pokemon=[pokemon["pokemon"]["name"] for pokemon in data["pokemon"]],
                   id=data["id"],
                   name=data["name"])


def generate_move(data):
    """
    Generate a Move object based on API data.
    :param data: JSON object containing API data
    :return: Move
    """
    return Move(id=data["id"],
                name=data["name"],
                generation=data["generation"]["name"],
                accuracy=data["accuracy"],
                pp=data["pp"],
                power=data["power"],
                type=data["type"]["name"],
                damage_class=data["damage_class"]["name"],
                effect_short=data["effect_entries"][0]["short_effect"])


def generate_stat(data):
    """
    Generate a Stat object based on API data.
    :param data: JSON object containing API data
    :return: Stat
    """
    return Stat(id=data["id"],
                name=data["name"],
                is_battle_only=data["is_battle_only"])
