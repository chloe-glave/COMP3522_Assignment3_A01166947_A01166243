from request import Request
from pokedex.pokedex_object import PokedexObject
from pokedex import ability, move, pokemon, stat
import aiohttp
import asyncio


class PokeRetriever:

    API_REQUEST_URL = "https://pokeapi.co/api/v2/{}/{}"

    async def get_request(self, mode, query_request) -> Request:
        """
        Get Pokemon data and return a request built with that data.
        :return: Request
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(PokeRetriever.API_REQUEST_URL.format(mode, query_request)) as response:
                    data = await response.json()
                    print(data)
                await session.close()
                # TODO: return a Request object with correctly parsed arguments
                # return Request()
        except Exception as e:
            print(e)

    async def execute_request(self, request: Request) -> PokedexObject:
        """
        Executes the request and returns a corresponding PokedexObject based on the request.
        :param request: Request
        :return: PokedexObject
        """
        return self.generate_pokedex_object(request)

    def generate_pokedex_object(self, request: Request) -> PokedexObject:
        """
        Creates a PokedexObject based on the request grabbed for it.
        :return: PokedexObject
        """
        if request.mode == "pokemon":
            return pokemon.Pokemon()
        elif request.mode == "ability":
            return ability.Ability()
        elif request.mode == "move":
            return move.Move()
        elif request.mode == "stat":
            return stat.Stat()


# for testing :)
async def main():
    poke = PokeRetriever()
    await poke.get_request("pokemon", 151)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

