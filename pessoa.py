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
        if self.pokemons:
            print(f"Pokemons de {self}:")
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f"{self} não possui Pokemons!")

class Jogador(Pessoa):
    tipo = "Jogador"

    def capturarPokemon(self, pokemon):
        self.pokemons.append(pokemon)

class Inimigo(Pessoa):
    tipo = "Inimigo"

jogador = Jogador("João Pedro")

jogador.mostrarPokemons()

pokemonSelvagem = PokemonAgua("Squirtle")

jogador.capturarPokemon(pokemonSelvagem)

jogador.mostrarPokemons()