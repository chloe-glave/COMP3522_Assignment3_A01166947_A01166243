import pokedex_object


class Stat(pokedex_object.PokedexObject):
    def __init__(self, name: str, id: str, is_battle_only: bool):
        super().__init__(name, id)
        self.is_battle_only = is_battle_only
