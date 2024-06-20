def tabuada():
    n = int(input('Digite um número inteiro: '))
    print(f'A tabuada de {n} é:')
    for i in range(1,11):
        print(i*n)

tabuada()