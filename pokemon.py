#!/usr/bin/python3

class Pokemon:
    def __init__(self, tipo, especie):
        self.tipo = tipo
        self.especie = especie

    def __str__(self):
        return f"{self.especie} ({self.tipo})"

meuPokemon = Pokemon("Água", "Squirtle")
pokemonAmigo = Pokemon("Planta", "Bulbasaur")

print(meuPokemon)
print(pokemonAmigo)