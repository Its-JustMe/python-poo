#   EXERCÍCIOS PYTHON
'''
    Classe	 Funcionário:	 Implemente	 a	 classe	
    Funcionário.	 Um	 funcionário	 tem	 um	 nome	 
    e	 um	 salário.	 Escreva	 um	 construtor	 com	 
    dois	 parâmetros	(nome	 e	 salário)	 e	 o	 
    método	 aumentarSalario (porcentualDeAumento)	 
    que	 aumente	 o	 salário	 do	
    funcionário	 em	 uma	 certa	 porcentagem
'''
from index import menu

class Funcionario:
    def __init__ (self, nome, salario):
        self.nome_funcionario = nome
        self.salario_funcionario = salario
    
    def aumentarSalario (self, percentualDeAumento):
        percentualDeAumento /= 100
        self.salario_funcionario += (self.salario_funcionario * percentualDeAumento)
        print(f'O funcionário {self.nome_funcionario} agora possui um salário de R${self.salario_funcionario:.2f}')

menu('Cadastro de Novo Funcionário')

nome = str(input('Nome do funcionário: '))
salario = float(input('Salário do funcionário: '))

novoFuncionario = Funcionario(nome, salario)

res = str(input('Deseja aumentar o salário deste funcionário? [S/N] '))

if res == 's':
    while True:
        try:
            aumento = float(input('Informe o percentual de aumento: '))
        except ValueError:
            print('Digite um valor válido.')
        else:
            novoFuncionario.aumentarSalario(aumento)
            break
print('Cadastro finalizado.')