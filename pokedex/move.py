import pokedex_object


class Move(pokedex_object.PokedexObject):
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
