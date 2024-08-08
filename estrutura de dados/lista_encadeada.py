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
    
    # Função para remover dados
    def remove(self, valor):
        # Verifica se o item a ser removido é o head
        if self.head and self.head.data == valor:
            self.head = self.head.next
        else:
            # Detecta a posição do elemento
            before = None
            navegar = self.head
            # Navega pela lista para encontrar o elemento
            while navegar and navegar.data != valor:
                before = navegar
                navegar = navegar.next
            
            # Remove o item se ele for encontrado
            if navegar:
                before.next = navegar.next
