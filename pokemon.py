#!/usr/bin/python3

class Pokemon:
    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie

meuPokemon = Pokemon("Água", "Squirtle")
pokemonAmigo = Pokemon("Planta", "Bulbasaur")

print(meuPokemon.tipo, meuPokemon.especie)
print(pokemonAmigo.tipo, pokemonAmigo.especie)