class ItemLista:
    # __init__ método construtor da lista
    # self permite que o método acesse os atributos e outros métodos da instância.
    # data e nextItem são parâmetros iniciais e finais dessa lista
    def __init__(self, data=None, nextItem=None):
        self.data = data
        self.next = nextItem
    def __repr__(self):
        return '%s => %s' % (self.data, self.next)

class ListaEncadeada:
    def __init__(self):
        self.head = None
          
    def __repr__(self):
        return "%s" % (self.head)
    
    # Função para inserir novos dados
    def insere(lista, data):    
        item = ItemLista(data)  # cria um objeto para armazenar um novo item da lista 
        item.next = lista.head  # o head é apontado como próximo item
        lista.head = item       # o item atual se torna o head
    
    def remove(lista, valor):
        # Verifica se o item a ser removido é o head
        if lista.head and lista.head.data == valor:
            lista.head = lista.head.next
            print(f"Nó com valor {valor} removido (era o head da lista)")
        else:
            before = None
            navegar = lista.head
            # Percorre a lista até encontrar o valor ou chegar ao final
            while navegar and navegar.data != valor:
                before = navegar
                navegar = navegar.next
            
            # Se o nó foi encontrado, 'navegar' não será None
            if navegar:
                before.next = navegar.next  # Pula o nó atual, efetivamente removendo-o
                print(f"Nó com valor {valor} removido")
            else:
                print("Valor não encontrado na lista")