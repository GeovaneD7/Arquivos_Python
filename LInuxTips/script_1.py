import random
def embaralha(nome):
    a = list(nome)
    random.shuffle(a)
    a = ''.join(a)
    print(a.upper())

nome = input('Digite uma palavra: ')
embaralha(nome)