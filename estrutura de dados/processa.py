import lista_encadeada as le
# Cria o objeto
lista = le.ListaEncadeada()

print("Conteúdo da lista: "), lista # lista está vazia

le.ListaEncadeada.insere(lista, "shampoo")
le.ListaEncadeada.insere(lista, "biscoito")
le.ListaEncadeada.insere(lista, "detergente") 
le.ListaEncadeada.insere(lista, "abobrinha ")
le.ListaEncadeada.insere(lista, "banana")

print(lista)

le.ListaEncadeada.remove(lista, "abobrinha")

print("Conteúdo da lista deletada: "), lista