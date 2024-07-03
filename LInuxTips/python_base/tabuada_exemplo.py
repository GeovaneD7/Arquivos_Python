#!/usr/bin/env python
"""Imprime uma tabuada do 1 ao 10."""
__version__ = "0.1.3"
__author__ = "Geovane Dias"

def tabuada():
    print()
    n = int(input("Digite um número inteiro: "))
    print()
    print("{:-^20}".format(f"Tabuada de {n}:"))
    for i in range(1,11):
        resultado = n * i
        print("{:-^20}".format(f" {n} x {i} = {resultado}"))
    print("~" * 20)
tabuada()