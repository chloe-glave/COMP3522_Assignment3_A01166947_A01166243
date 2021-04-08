from request import Request


class PokeRetriever:

    def get_request(self) -> Request:
        """
        Get Pokemon data and return a request built with that data.
        :return: Request
        """
        pass

    def execute_request(self, request: Request):
        """
        Executes the request and returns a corresponding PokedexObject based on the request.
        :param request: Request
        :return: PokedexObject
        """
        pass

    def generate_pokedex_object(self):
        """
        Creates a PokedexObject based on the request grabbed for it.
        :return: PokedexObject
        """
        pass
