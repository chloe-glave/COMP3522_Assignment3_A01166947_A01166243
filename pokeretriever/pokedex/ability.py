from .pokedex_object import PokedexObject


class Ability(PokedexObject):
    def __init__(self, name: str, id: str, generation: str, effect: str, effect_short: str, pokemon: list):
        super().__init__(name, id)
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon

    def __str__(self):
        return f"Ability:\n" \
               f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect Short: {self.effect_short}\n" \
               f"Pokemon: {self.pokemon}\n"
