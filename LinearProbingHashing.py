class LinearProbingHashing:
    def __init__(self):
        self.vet = [None]*16
        self.qt_items = 0

    def __hash(self, char):
        return ord(char[0]) % 16

    def put(self, char):
        if self.qt_items == 16:
            print('Tabela lotada!')
        else:    
            posicao = self.__hash(char)
            if self.vet[posicao] is None:
                self.vet[posicao] = char
            else:                
                while self.vet[posicao] is not None:                    
                    posicao += 1
                    if posicao == 16:
                        posicao = 0
                    
                self.vet[posicao] = char

    def get(self, char):
        posicao = self.__hash(char)
        posicao_inicial = posicao
        
        while self.vet[posicao] != char:
            if posicao == 16:
                posicao = 0
                
            if self.vet[posicao] is None:
                return None

            if posicao+1 == posicao_inicial:
                return None
                                            
            posicao += 1                
            
        return self.vet[posicao]
    
    def show_vet(self):
        print(self.vet)
        
tabela = LinearProbingHashing()
tabela.put('K')
tabela.put('A')
tabela.put('X')
tabela.put('g')
tabela.put('G')
tabela.show_vet()
print(tabela.get('G'))









