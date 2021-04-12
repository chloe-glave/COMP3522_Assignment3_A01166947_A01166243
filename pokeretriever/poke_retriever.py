from .request import Request
from .pokedex_object_generator import *
import aiohttp


class PokeRetriever:

    API_REQUEST_URL = "https://pokeapi.co/api/v2/{}/{}"

    def __init__(self):
        self.poke_request = Request()
        print(self.poke_request)  # todo: for testing, remove later

    async def execute_request(self) -> PokedexObject:
        """
        Executes the request and returns a corresponding PokedexObject based on the request.
        :return: PokedexObject
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(PokeRetriever.API_REQUEST_URL.format(self.poke_request.mode,
                                                                            self.poke_request.input_data)) as response:
                    data = await response.json()
                await session.close()
        except Exception as e:
            print(e)
        return generate_pokedex_object(self.poke_request.mode, data)
        return self.generate_pokedex_object(data)

    def generate_pokedex_object(self, data) -> PokedexObject:
        """
        Creates a PokedexObject based on the request grabbed for it.
        :return: PokedexObject
        """
        if self.poke_request.mode == "pokemon":

            return Pokemon(height=data["height"],
                           weight=data["weight"],
                           stats=data["stats"],
                           types=[types["type"]["name"] for types in data["types"]],
                           abilities=[abilities if self.poke_request.is_expanded
                                      else abilities["ability"]["name"] for abilities in data["abilities"]],
                           moves=[moves["move"] if self.poke_request.is_expanded else moves["move"]["name"]
                                  for moves in data["moves"]],
                           id=data["id"],
                           name=data["name"])
        elif self.poke_request.mode == "ability":
            return Ability(generation=data["generation"]["name"],
                           effect=data["effect_entries"][1]["effect"],
                           effect_short=data["effect_entries"][1]["short_effect"],
                           pokemon=[pokemon["pokemon"]["name"] for pokemon in data["pokemon"]],
                           id=data["id"],
                           name=data["name"])
        elif self.poke_request.mode == "move":
            return Move(id=data["id"],
                        name=data["name"],
                        generation=data["generation"]["name"],
                        accuracy=data["accuracy"],
                        pp=data["pp"],
                        power=data["power"],
                        type=data["type"]["name"],
                        damage_class=data["damage_class"]["name"],
                        effect_short=data["effect_entries"][0]["short_effect"])
        elif self.poke_request.mode == "stat":
            return Stat(id=data["id"],
                        name=data["name"],
                        is_battle_only=data["is_battle_only"])
