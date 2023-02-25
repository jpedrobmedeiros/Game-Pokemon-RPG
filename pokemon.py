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

meuPokemon = Pokemon("Água", "Squirtle", "Taturu", "50")
pokemonAmigo = Pokemon("Planta", "Bulbasaur")

print(meuPokemon)
print(pokemonAmigo)

meuPokemon.atacar(pokemonAmigo)
pokemonAmigo.atacar(meuPokemon)