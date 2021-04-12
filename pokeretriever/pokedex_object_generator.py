from .pokedex.pokedex_object import PokedexObject
from .pokedex.ability import Ability
from .pokedex.pokemon import Pokemon
from .pokedex.move import Move
from .pokedex.stat import Stat


def generate_pokedex_object(request_mode, data) -> PokedexObject:
    """
    Creates a PokedexObject based on the request grabbed for it.
    :param request_mode: string representing the object to create.
    :param data: JSON object containing Pokedex data from API.
    :return: PokedexObject
    """
    if request_mode == "pokemon":
        return generate_pokemon(data)
    elif request_mode == "ability":
        return generate_ability(data)
    elif request_mode == "move":
        return generate_move(data)
    elif request_mode == "stat":
        return generate_stat(data)


def generate_pokemon(data):
    return Pokemon(height=data["height"],
                   weight=data["weight"],
                   stats=data["stats"],
                   types=[types["type"]["name"] for types in data["types"]],
                   abilities=data["abilities"],
                   moves=[moves["move"] for moves in data["moves"]],
                   id=data["id"],
                   name=data["name"])


def generate_ability(data):
    return Ability(generation=data["generation"]["name"],
                   effect=data["effect_entries"][1]["effect"],
                   effect_short=data["effect_entries"][1]["short_effect"],
                   pokemon=[pokemon["pokemon"]["name"] for pokemon in data["pokemon"]],
                   id=data["id"],
                   name=data["name"])


def generate_move(data):
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
    return Stat(id=data["id"],
                name=data["name"],
                is_battle_only=data["is_battle_only"])
