#!/usr/bin/python3

from pokemon import *

class Pessoa:
    def __init__(self, nome, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = "Anônimo"

        self.pokemons = pokemons
    
    def __str__(self):
        return self.nome

    def mostrarPokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)

class Jogador(Pessoa):
    tipo = "Jogador"

class Inimigo(Pessoa):
    tipo = "Inimigo"

pokemon1 = PokemonAgua("Squirtle")
pokemon2 = PokemonPlanta("Bulbasaur")

eu = Jogador("João Pedro")

print(eu)
eu.mostrarPokemons()