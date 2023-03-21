#   EXERCÍCIOS PYTHON
'''
    Crie uma classe que modele uma pessoa:
    a. Atributos: nome, idade, peso e altura
    b. Métodos: Envelhercer, engordar, emagrecer, 
    crescer. Obs: Por padrão, a cada ano que nossa pessoa 
    envelhece, sendo a idade dela menor que 21 anos, 
    ela deve crescer 0,5 cm.
'''

class Pessoa:
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    # Métodos da Classe
    def envelhecer (self):
        self.idade += 1
        if self.idade <= 25:
            self.altura += 0.5

    def engordar (self, quilos):
        self.peso += quilos

    def emagrecer (self, quilos):
        self.peso -= quilos

    def crescer (self, centimetros):
        self.altura += centimetros