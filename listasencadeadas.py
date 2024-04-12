# Implementação de lista encadeada
class Caixa:
    
    # Construtor
    def __init__(self, valor) -> None:
        self.valor = valor # Valor do nó
        self.proximo = None # Ponteiro para o próximo nó
        
# Lista encadeada
class List:
    def __init__(self) -> None:
        self.head = None # Cabeça da lista
        
    # Inserir um novo nó
    def inserir(self, valor):
        
        # Se a lista estiver vazia
        if not self.head:
            self.head = Caixa(valor) # Cria um novo nó
            
        else: # Se a lista não estiver vazia
            temp = self.head # Cria um nó temporário
            while temp.proximo: # Enquanto houver um próximo nó
                temp = temp.proximo # Avança para o próximo nó
            temp.proximo = Caixa(valor) # Cria um novo nó
            
    def inserir_inicio(self, valor):
        novo_no = Caixa(valor)
        novo_no.proximo = self.head
        self.head = novo_no
    
    def inserir_fim(self, valor):
        novo_no = Caixa(valor)
        temp = self.head
        while temp.proximo:
            temp = temp.proximo
        temp.proximo = novo_no 
        
    def inserir_na_posicao(self, valor, posicao):
        novo_no = Caixa(valor)
        temp = self.head
        for i in range(posicao - 1):
            temp = temp.proximo
        novo_no.proximo = temp.proximo
        temp.proximo = novo_no
        
    def inserir_antes_de(self, valor, valor_referencia):
        novo_no = Caixa(valor)
        temp = self.head
        while temp.proximo:
            if temp.proximo.valor == valor_referencia:
                novo_no.proximo = temp.proximo
                temp.proximo = novo_no
                return
            temp = temp.proximo
        
            
    def inserir_depois_de(self, valor, valor_referencia):
        novo_no = Caixa(valor)
        temp = self.head
        while temp:
            if temp.valor == valor_referencia:
                novo_no.proximo = temp.proximo
                temp.proximo = novo_no
                return
            temp = temp.proximo
            
    def remover_inicio(self):
        if self.head:
            self.head = self.head.proximo
        
    def remover_fim(self):
        temp = self.head
        while temp.proximo.proximo:
            temp = temp.proximo
        temp.proximo = None
        
    def remover_na_posicao(self, posicao):
        temp = self.head
        for i in range(posicao - 1):
            temp = temp.proximo
        temp.proximo = temp.proximo.proximo
        
    def remover_elemento(self, valor):
        temp = self.head
        if temp.valor == valor:
            self.head = temp.proximo
            return
        while temp.proximo:
            if temp.proximo.valor == valor:
                temp.proximo = temp.proximo.proximo
                return
            temp = temp.proximo
            
    def acessa_primeiro(self):
        return self.head.valor
    
    def acessa_ultimo(self):
        temp = self.head
        while temp.proximo:
            temp = temp.proximo
        return temp.valor
    
    def acessa_posicao(self, posicao):
        temp = self.head
        for i in range(posicao):
            temp = temp.proximo
        return temp.valor       
    
    # Imprimir a lista
    def print_list(self):
        temp = self.head # Nó temporário
        while temp: # Enquanto houver um nó
            print(temp.valor) # Imprime o valor do nó
            temp = temp.proximo # Avança para o próximo nó
            
    def remover(self, valor): # Remover um nó
        temp = self.head # Nó temporário
        if temp.valor == valor: # Se o valor do nó for igual ao valor a ser removido
            self.head = temp.proximo # A cabeça da lista aponta para o próximo nó
            return # Retorna
        while temp.proximo:# Enquanto houver um próximo nó
            if temp.proximo.valor == valor: # Se o valor do próximo nó for igual ao valor a ser removido
                temp.proximo = temp.proximo.proximo # O próximo nó aponta para o próximo nó
                return 
            temp = temp.proximo # Avança para o próximo nó
            
    # Remover todos os nós com um determinado valor
    def remover_todos(self, valor):
        temp = self.head # Nó temporário
        while temp and temp.valor == valor: # Enquanto houver um nó e o valor do nó for igual ao valor a ser removido
            self.head = temp.proximo # A cabeça da lista aponta para o próximo nó
            temp = self.head # O nó temporário aponta para a cabeça da lista
        while temp and temp.proximo: # Enquanto houver um nó e um próximo nó
            if temp.proximo.valor == valor: # Se o valor do próximo nó for igual ao valor a ser removido
                temp.proximo = temp.proximo.proximo # O próximo nó aponta para o próximo nó
            else: # Se o valor do próximo nó não for igual ao valor a ser removido
                temp = temp.proximo # Avança para o próximo nó
                
# Teste
lista = List() # Cria uma lista
lista.inserir(1) # Insere um nó
lista.inserir(2) # Insere um nó
lista.inserir(3) # Insere um nó
lista.inserir(4) # Insere um nó
lista.print_list() # Imprime a lista
lista.remover(3) # Remove um nó
lista.print_list() # Imprime a lista

