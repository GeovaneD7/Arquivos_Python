class Vertice: 
# Vertice de Arvore Binária 
    def __init__(self, dado): 
    # dado propriamente dito, conteúdo do vértice 
        self.dado = dado 
        # filho da esquerda e da direita 
        self.esquerda = None
        self.direita = None 

    def __str__(self): 
        return str(self.dado) 

    def representacao_com_parenteses(self): 
    # Retorna a representação da árvore com aninhamento por parênteses  
        if self.esquerda:
        # recursividade 
            esq = self.esquerda.representacao_com_parenteses() 
        else: 
            esq = None
            
        if self.direita: 
        # recursividade 
            dir = self.direita.representacao_com_parenteses() 
        else: 
            dir =  None

        return format(str(self), esq, dir) 

    def representacao_com_recuo(self, numero_de_espacos=0): 
        if self.esquerda: 
            esq = self.esquerda.representacao_com_recuo(numero_de_espacos + 4) 
        else: 
            esq =  None

        if self.direita: 
            dir = self.direita.representacao_com_recuo(numero_de_espacos + 4)
        else: 
            dir =  None

        return format( 
            espacos=' '*numero_de_espacos, 
            self=str(self), 
            esq=esq, 
            dir=dir, 
        ) 
        # Percorre a árvore em ordem simétrica (esquerda, vértice, direita) 
        # e imprime o dado do vértice 
        
    def imprimir_percurso_em_ordem(self): 
        if self.esquerda: 
    # recursividade: executa o mesmo atributo para seu filho esquerdo 
            self.esquerda.imprimir_percurso_em_ordem() 
    # imprime o dado do vértice 
            print(self) 
        if self.direita: 
        # recursividade: executa o mesmo atributo para seu filho direito 
            self.direita.imprimir_percurso_em_ordem() 


    
    def imprimir_percurso_pre_ordem(self): 
        # Percorre a árvore em pré ordem (vértice, esquerda, direita) 
        # e imprime o dado do vértice 
         
        print(self) # imprime o dado do vértice 
        
        if self.esquerda: 
        # recursividade: executa o mesmo atributo para seu filho esquerdo 
            self.esquerda.imprimir_percurso_pre_ordem() 
        if self.direita: 
        # recursividade: executa o mesmo atributo para seu filho direito 
            self.direita.imprimir_percurso_pre_ordem() 

    def imprimir_percurso_pos_ordem(self): 
        # Percorre a árvore em pré ordem (esquerda, direita, vértice) 
        #e imprime o dado do vértice 
        if self.esquerda: 
        # recursividade: executa o mesmo atributo para seu filho esquerdo 
            self.esquerda.imprimir_percurso_pos_ordem() 
        if self.direita: 
        # recursividade: executa o mesmo atributo para seu filho direito 
            self.direita.imprimir_percurso_pos_ordem() 

        print(self) # imprime o dado do vértice 
