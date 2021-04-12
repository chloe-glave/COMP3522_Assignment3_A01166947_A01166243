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
        return generate_pokedex_object(self.poke_request, data)
