#!/usr/bin/python3

from pessoa import *
from pokemon import *

def escolherPokemonInicial(jogador):
    print(f"Olá {jogador}, Escolha um pokemon inicial:")

    bulbasaur = PokemonPlanta("Bulbasaur", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)
    charmander = PokemonFogo("Charmander", level=1)

    print(f"1 - {bulbasaur}")
    print(f"2 - {squirtle}")
    print(f"3 - {charmander}")

    while True:
        escolha = input("Escolha o seu Pokemon: ")

        if escolha == "1":
            jogador.capturarPokemon(bulbasaur)
            break
        elif escolha == "2":
            jogador.capturarPokemon(squirtle)
            break
        elif escolha == "3":
            jogador.capturarPokemon(charmander)
            break
        else:
            print("Escolha inválida!")

jogador = Jogador("João Pedro")

escolherPokemonInicial(jogador)

jogador.mostrarPokemons()