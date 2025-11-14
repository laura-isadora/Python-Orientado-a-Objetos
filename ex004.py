class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario
        
    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario
    
    def calcular_bonus(self):
        return self.salario * 0.10
    
class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20

class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.05


f = Funcionario("Joao", 2500)
g = Gerente("Maria", 5000)
e = Estagiario("Fernando", 1800)

print(f.nome, f.calcular_bonus())
print(g.nome, g.calcular_bonus())
print(e.nome, e.calcular_bonus())
