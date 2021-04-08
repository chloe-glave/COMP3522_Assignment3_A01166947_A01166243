import abc


class PokedexObject(abc.ABC):
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
