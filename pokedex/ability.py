import pokedex_object


class Ability(pokedex_object.PokedexObject):
    def __init__(self, name: str, id: str, generation: str, effect: str, effect_short: str, pokemon: list):
        super().__init__(name, id)
        self.generation: generation
        self.effect: effect
        self.effect_short: effect_short
        self.pokemon: pokemon
