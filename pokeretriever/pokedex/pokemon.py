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
        if type(self.stats) is dict:
            stats_string = "\n-------\n" + '\n'.join(': '.join((key,val)) for (key,val) in self.stats.items()) \
                           + "\n-------"
        else:
            stats_string = "\n-------\n" + "\n".join(self.stats) + "\n-------"

        abilities_string = "\n-------\n" + "\n".join(self.abilities) + "\n-------"

        moves_string = "\n-------\n" + "\n".join(self.moves) + "\n-------"

        types_string = ", ".join(self.types)

        return f"Pokemon:\n" \
               f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Height: {self.height}\n" \
               f"Weight: {self.weight}\n" \
               f"Types: {types_string}\n" \
               f"Stats: {stats_string}\n" \
               f"Abilities: {abilities_string}\n" \
               f"Moves: {moves_string}"
