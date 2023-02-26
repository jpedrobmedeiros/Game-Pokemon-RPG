#!/usr/bin/python3

import random

class Pokemon:
    def __init__(self, especie, nome=None, level=random.randint(1, 100)):
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

class PokemonAgua(Pokemon):
    tipo = "Água"

    def atacar(self, pokemon):
        print(f"{self} lançou um jato d'água em {pokemon}!")

class PokemonFogo(Pokemon):
    tipo = "Fogo"

    def atacar(self, pokemon):
        print(f"{self} lançou uma bola de fogo em {pokemon}!")

class PokemonPlanta(Pokemon):
    tipo = "Planta"

    def atacar(self, pokemon):
        print(f"{self} lançou folhas cortantes em {pokemon}!")