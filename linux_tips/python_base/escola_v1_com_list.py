#!/usr/bin/env python3
"""Exibe relatório de crianças por atividades.

-De cada sala da escola, quanas crianças estão matriculadas em cada atividade?
Imprimir a lista de criança agrupadas por sala que frequenta cada uma das atividades.
"""
__version__ = "0.1.0"
__author__ = "Bruno Rocha"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = [ "Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Antonio", "Joana"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Musica", aula_musica), 
    ("Dança", aula_danca)
]

# LIstar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f"\nAlunos da atividade {nome_atividade}\n")
    print("-" * 40)
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
            
    print("sala 1: ", atividade_sala1)
    print("sala 2: ", atividade_sala2)
    
    print()
    print("#" * 40)
