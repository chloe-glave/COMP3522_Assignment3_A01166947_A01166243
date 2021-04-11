from .pokedex_object import PokedexObject


class Pokemon(PokedexObject):
    def __init__(self, name: str, id: str, height: int, weight: int, stats: list, types: list, abilities: list,
                 moves: list):
        super().__init__(name, id)
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

    def __str__(self):
        return f"Pokemon:\n" \
               f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Height: {self.height}\n" \
               f"Weight: {self.weight}\n" \
               f"Stats: {self.stats}\n" \
               f"Type: {self.types}\n" \
               f"Abilities: {self.abilities}" \
               f"Moves: {self.moves}"
