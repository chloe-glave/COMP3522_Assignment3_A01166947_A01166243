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

        output_object = await generate_pokedex_object(self.poke_request, data)

        if self.poke_request.output_file:
            self.write_output_to_file(output_object)
        else:
            print(output_object)

    def write_output_to_file(self, pokedex_object):
        """
        File IO for writing output to a text file.
        :param pokedex_object: PokedexObject, the data to write to the file
        :return: None
        """
        try:
            output_text_file = open(self.poke_request.output_file, 'w', encoding='UTF-8')

            output_text_file.write(pokedex_object.__str__())

            output_text_file.close()
            print(f"Output written to {self.poke_request.output_file}. Have a nice day!")
        except IOError:
            print("Error with writing to text file, exiting program.")
        finally:
            exit(0)
