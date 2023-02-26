#!/usr/bin/python3

import random

from pokemon import *

NOMES = [
    "João", "Ingrid", "Maria", "Paulo", "Joaquina", "Gerson", "Gary", "Gerônimo", "Claudia", "Jeremias", "Pedro", "Marcos", "Matheus", "Camila", "Yuri"
]

class Pessoa:
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

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

print(f"Jogador: {jogador}")

inimigo = Inimigo()

print(f"Inimigo: {inimigo}")