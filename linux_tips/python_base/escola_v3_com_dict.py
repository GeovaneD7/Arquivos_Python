#!/usr/bin/env python3
"""Exibe relatório de crianças por atividades.

-De cada sala da escola, quanas crianças estão matriculadas em cada atividade?
Imprimir a lista de criança agrupadas por sala que frequenta cada uma das atividades.
"""
__version__ = "0.1.3"
__author__ = "Bruno Rocha"

# Dados
alunos = {
"sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
"sala2": [ "Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Musica": ["Erik", "Carlos", "Maria"], 
    "Dança": ["Gustavo", "Sofia", "Antonio", "Joana"]
}

# LIstar alunos em cada atividade por sala
print()
print("#" * 40)

for atividade in atividades:

    print(f"\nAlunos da atividade {atividade}\n")
    print("-" * 40)
    
    # salas que tem interseção com a atividade
    atividade_sala1 = set(alunos['sala1']) & set(atividades[atividade])
    atividade_sala2 = set(alunos['sala2']) & set(atividades[atividade])

    print("sala 1: ", atividade_sala1)
    print("sala 2: ", atividade_sala2)
    
    print()
    print("#" * 40)
