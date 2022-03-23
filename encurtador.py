import pickle
from math import floor


class Encurtador:
    def __init__(self):
        self.dic = {}
        self.nome_arq = 'urls.dat'
        self.__load_dic()
        self.indice = 1000 + len(self.dic)

    def __load_dic(self):
        try:
            arquivo = open('urls.dat', 'r')
            print(arquivo.read())
            arquivo.close()
        except:
            print('O arquivo não existe!')

    def __save_dic(self):
        arquivo = open('urls.dat', 'wb')
        pickle.dump(self.dic, arquivo)
        arquivo.close()

    def toBase(self, num, b=62):
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

    def to10(self, num, b=62):
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        limit = len(num)
        res = 0
        for i in range(limit):
            res = b * res + base.find(num[i])
        return res

    def encurtar(self, url):
        url_curta = Encurtador().toBase(self.indice)

        self.dic[self.indice] = (url, url_curta)
        arquivo = open('urls.dat', 'wb')
        pickle.dump(self.dic, arquivo)
        arquivo.close()
        self.indice += 1

    def buscar(self, url_curta):
        indice = self.to10(url_curta)
        return self.dic[indice][1]

    def listar_urls(self):
        print(self.dic)


## TESTES ##
e = Encurtador()

e.encurtar(
    "https://imed.edu.br/Ensino/ciencia-da-computacao/graduacao/sobre-a-profissao/")
e.encurtar(
    "https://www.linkedin.com/feed/")


print('Dicionário:')
e.listar_urls()

print(e.buscar('g8'))
