from .pokedex_object import PokedexObject


class Stat(PokedexObject):
    def __init__(self, name: str, id: str, is_battle_only: bool):
        super().__init__(name, id)
        self.is_battle_only = is_battle_only

    def __str__(self):
        return f"Stat:\n" \
               f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Is battle only?: {self.is_battle_only}\n"
