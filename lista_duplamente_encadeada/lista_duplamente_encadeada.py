from no import No

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.cursor = None
        self.quantidade = 0

    def inserirComoPrimeiro(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = self.cursor = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no
        self.quantidade += 1

    def inserirComoUltimo(self, valor):
        novo_no = No(valor)
        if self.cauda is None:
            self.cabeca = self.cauda = self.cursor = novo_no
        else:
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no
        self.quantidade += 1

    def inserirAntesDoAtual(self, valor):
        if self.cursor is None:
            return
        novo_no = No(valor)
        novo_no.proximo = self.cursor
        novo_no.anterior = self.cursor.anterior
        if self.cursor.anterior is not None:
            self.cursor.anterior.proximo = novo_no
        self.cursor.anterior = novo_no
        if self.cursor == self.cabeca:
            self.cabeca = novo_no
        self.quantidade += 1
        
    def inserirAposAtual(self, valor):
        if self.cursor is None:
            return
        novo_no = No(valor)
        novo_no.anterior = self.cursor
        novo_no.proximo = self.cursor.proximo
        if self.cursor.proximo is not None:
            self.cursor.proximo.anterior = novo_no
        self.cursor.proximo = novo_no
        if self.cursor == self.cauda:
            self.cauda = novo_no
        self.quantidade += 1

    def inserirNaPosicao(self, k, valor):
        if k == 0:
            self.inserirComoPrimeiro(valor)
            return
        self.cursor = self.cabeca
        for i in range(k):
            if self.cursor is None:
                return
            self.cursor = self.cursor.proximo
        self.inserirAntesDoAtual(valor)
        self.quantidade += 1

    def ExcluirAtual(self):
        if self.cursor is None:
            return
        if self.cursor.anterior is not None:
            self.cursor.anterior.proximo = self.cursor.proximo
        if self.cursor.proximo is not None:
            self.cursor.proximo.anterior = self.cursor.anterior
        if self.cursor == self.cabeca:
            self.cabeca = self.cursor.proximo
        if self.cursor == self.cauda:
            self.cauda = self.cursor.anterior
        self.cursor = None
        self.quantidade -= 1

    def ExcluirPrim(self):
        if self.cabeca is None:
            return
        self.cursor = self.cabeca
        self.ExcluirAtual()
        self.quantidade -= 1

    def ExcluirUlt(self):
        if self.cauda is None:
            return
        self.cursor = self.cauda
        self.ExcluirAtual()
        self.quantidade -= 1

    def ExcluirElem(self, chave):
        self.cursor = self.cabeca
        while self.cursor is not None:
            if self.cursor.valor == chave:
                self.ExcluirAtual()
                return
            self.cursor = self.cursor.proximo
        self.quantidade -= 1        
    
    def ExcluirDaPos(self, k):
        self.cursor = self.cabeca
        for i in range(k):
            if self.cursor is None:
                return
            self.cursor = self.cursor.proximo
        self.ExcluirAtual()
        self.quantidade -= 1

    def Buscar(self, chave):
        self.cursor = self.cabeca
        while self.cursor is not None:
            if self.cursor.valor == chave:
                return True
            self.cursor = self.cursor.proximo
        return False

    def acessarAtual(self):
        if self.cursor is None:
            return None
        return self.cursor.valor

    def avancarKPosicoes(self, k):
        for i in range(k):
            if self.cursor is None:
                return
            self.cursor = self.cursor.proximo

    def retrocederKPosicoes(self, k):
        for i in range(k):
            if self.cursor is None:
                return
            self.cursor = self.cursor.anterior

    def irParaPrimeiro(self):
        self.cursor = self.cabeca

    def irParaUltimo(self):
        self.cursor = self.cauda

    def Vazia(self):
        return self.cabeca is None

    def Cheia(self):
        return False

    def posicaoDe(self, chave):
        self.cursor = self.cabeca
        pos = 0
        while self.cursor is not None:
            if self.cursor.valor == chave:
                return pos
            self.cursor = self.cursor.proximo
            pos += 1
        return -1
    
    def quantidade(self):
        return self.quantidade
    
    def imprimir(self):
        if self.cabeca is None:
            print('Lista está vazia!')
        else:
            ponteiro = self.cabeca
            while ponteiro:
                print(ponteiro.valor)
                ponteiro = ponteiro.proximo
            print(f'Tamanho da lista: {self.quantidade}')