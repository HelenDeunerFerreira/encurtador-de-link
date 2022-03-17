import pickle
from math import floor


class Encurtador:
    def __init__(self):
        self.dic = {}
        self.nome_arq = 'urls.txt'
        self.__load_dic()
        self.indice = 1000 + len(self.dic)

    def __load_dic(self):
        # testar se arquivo existe
        if self.nome_arq == True:
            # carregar dicionario do arquivo .. variavel self.nome_arq >> fazer leitura
            arquivo = open('urls.txt', 'r')
            print(arquivo.read())
            return 'Arquivo existe'
        else:
            return 'Arquivo inexistente'

    def __save_dic(self):
        # salvar dicionario no arquivo .. variavel self.nome_arq
        arquivo = open('urls.txt', 'r')
        with open("urls.pkl", "wb") as tf:
            pickle.dump(arquivo, tf)
        arquivo.close()

    def toBase(self, num, b=62):  # queria saber o que são essas letras
        if b <= 0 or b > 62:
            return 0
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        r = num % b
        res = base[r]
        q = floor(num / b)
        while q:
            r = q % b
            q = floor(q / b)
            res = base[int(r)] + res
        return res

    def to10(self, num, b=62):  # não saquei o que seria o limite
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        limit = len(num)
        res = 0
        for i in range(limit):
            res = b * res + base.find(num[i])
        return res

    def encurtar(self, url):
        arquivo = open('urls.txt', 'w')
        # não to entendendo onde ficam armazenadas essas variáveis pra gente colocar aqui
        arquivo.write(f'{self.indice}: ({url_curta}, {url_original})')
        arquivo.close()
        self.indice += 1

        __save_dic(arquivo)  # descobri que n consigo implementar esse método
        # salvar no dicionario usando como chave o valor da variavel self.indice >> pega o indice p salvar
        # o valor a ser salvo é uma tupla onde a posicao 0 eh o indice convertido para string usando base62 e a posicao 1 eh a url original
        # nao esqueca de incrementar a variavel self.indice >> ++1
        # e por fim, chamar o metodo __save_dic para salvar o dicionario no arquivo em disco.

    def buscar(self, url_curta):
        indice = self.to10(url_curta)
        return self.dic[indice][1]  # retorna a 2a posicao da tupla

    def listar_urls(self):
        print(self.dic)


## TESTES ##
e = Encurtador()
e.encurtar(
    "https://imed.edu.br/Ensino/ciencia-da-computacao/graduacao/sobre-a-profissao/")

e.listar_urls()

# print(e.buscar('g8'))
