#!/usr/bin/python3

class Pokemon:
    def __init__(self, tipo, especie, nome=None, level=1):
        self.tipo = tipo
        self.especie = especie
        if nome:
            self.nome = nome
        else:
            self.nome = especie
        self.level = level

    def __str__(self):
        return f"{self.nome} ({self.level})"

    def atacar(self, pokemon):
        print(f"{self} atacou {pokemon}!")

class PokemonAquatico(Pokemon):
    def atacar(self, pokemon):
        print(f"{self} lançou um jato d'água em {pokemon}")

    def molhar(self):
        print(f"{self} molhou tudo!")

meuPokemon = PokemonAquatico("Água", "Squirtle", "Taturu", "50")
pokemonAmigo = Pokemon("Planta", "Bulbasaur")

print(meuPokemon)
print(pokemonAmigo)

meuPokemon.atacar(pokemonAmigo)
pokemonAmigo.atacar(meuPokemon)

meuPokemon.molhar()