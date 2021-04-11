from .pokedex_object import PokedexObject


class Move(PokedexObject):
    def __init__(self, name: str, id: str, generation: str, accuracy: int, pp: int, power: int, type: str,
                 damage_class: str, effect_short: str):
        super().__init__(name, id)
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.type = type
        self.damage_class = damage_class
        self.effect_short = effect_short

    def __str__(self):
        return f"Pokemon:\n" \
               f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Height: {self.accuracy}\n" \
               f"Weight: {self.pp}\n" \
               f"Stats: {self.power}\n" \
               f"Type: {self.type}\n" \
               f"Abilities: {self.damage_class}" \
               f"Moves: {self.effect_short}"