class Cliente:
    def __init__(self, conta, nome, cpf):
        self._conta = conta
        self._nome = nome
        self._cpf = cpf
        
class Conta:
    def __init__(self, numero, saldo):
        self._numero = numero
        self._saldo = saldo
        
    @property
    def saldo(self):
        return self._saldo
        
    @saldo.setter
    def saldo ( self, valor ):
        if valor >= 0:
            self._saldo = valor
        else:
            print('ERRO: o saldo nao pode ser negativo!')

conta = Conta(267, 500)
conta.saldo = 2000
print(conta.saldo)