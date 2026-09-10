class funcionario:
    def __init__(self, nome, salário):
        self.nome = nome
        self.salario = salário
        calcular_salario()

class gerente:
    def __init__(self, nome, salário):
        self.nome = nome 
        self.salario = salário 
        calcular_salario()

class estagiario:
    def __init__(self, nome, salário):
        self.nome = nome 
        self.salario = salário
        calcular_salario()

def mostrar_salario(funcionario):
    print(f'O salário do funcinário {funcionario.nome} é {funcionario.salario}.')





