#!/usr/bin/env python
"""Imprime uma tabuada do 1 ao 10."""
__version__ = "0.1.2"
__authonr__ = "Geovane Dias"

def tabuada():
    n = int(input("Digite um número inteiro: "))
    print(f"A tabuada de {n} é:")
    for i in range(1,11):
        print(f" {n} x {i} = ", i*n)

tabuada()