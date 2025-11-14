class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b
        
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if b == 0:
            return "Erro: não é possível dividir por zero."
        return a / b
        
print(Calculadora.somar(10, 15))
print(Calculadora.dividir(10, 0))