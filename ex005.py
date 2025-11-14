# sistema de loja para classificacao de imposto de cada produto
# produto: 10% / livro: 5% / eletronicos: 20%

class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    @property
    def nome(self):
        return self._nome
        
    @property
    def preco(self):
        return self._preco

    def calcular_imposto(self):
        return self._preco * 0.10

class Livros(Produto):
    def calcular_imposto(self):
        return self._preco * 0.05

class Eletronicos(Produto):
    def calcular_imposto(self):
        return self._preco * 0.20

p = Produto("calçado", 200)
l = Livros("O Senhor dos Aneis", 100)
e = Eletronicos("Xiaomi Pad 2", 1200)

print(p.nome, p.calcular_imposto())
print(l.nome, l.calcular_imposto())
print(e.nome, e.calcular_imposto())