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
    def insere(self, data):    
        item = ItemLista(data)  # cria um objeto para armazenar um novo item da lista 
        item.next = self.head  # o head é apontado como próximo item
        self.head = item
        
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

# Exemplo de uso
lista = ListaEncadeada()
lista.insere(3)
lista.insere(2)
lista.insere(1)
print("Lista após inserções:", lista)

lista.remove(2)
print("Lista após remoção do 2:", lista)

lista.remove(1)
print("Lista após remoção do 1:", lista)