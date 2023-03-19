#   EXERCÍCIOS POO PYTHON
''' 
    Classe	Triangulo:	Crie	uma	classe	que	modele	
    um	triangulo:		
    - Atributos:	LadoA,	LadoB,	LadoC
    - Métodos:	calcular	Perímetro,	getMaiorLado;		
    Crie	um	programa	que	uFlize	esta	classe.	Ele	deve	
    pedir	ao	usuário	que	informe	as	medidas	de	um	
    triangulo.	Depois,	deve	criar	um	objeto	com	as	
    medidas	e	imprimir	sua	área	e	maior	lado.
'''

from index import menu

class Triangulo:
    def __init__ (self, a, b, c):
        self.ladoA = a
        self.ladoB = b
        self.ladoC = c

    # Método Getter
    def getMaiorLado (self):
        return max(self.ladoA, self.ladoB, self.ladoC)

    # Métodos
    def perimetro (self):
        return self.ladoA + self.ladoB + self.ladoC
    
    # Métodos Extras
    def tipoTriangulo (self):
        if self.ladoA == self.ladoB and ladoA == self.ladoC:
            return 'Triângulo Equilátero'
        elif self.ladoA != self.ladoB and self.ladoB != self.ladoC:
            return 'Triângulo Escaleno'
        else:
            return 'Triângulo Isóceles'
        
    
    def infoTriangulo (self):
        return {
            'Tipo de Triângulo': self.tipoTriangulo(),
            'Medida dos lados': f'{self.ladoA}, {self.ladoB}, {self.ladoC}',
            'Perímetro': self.perimetro(),
            'Maior lado': self.getMaiorLado()
        }
    
menu('Gerador de Triângulos')

while True:
    try:
        ladoA = float(input('Informe a medida do lado A: '))
        ladoB = float(input('Informe a medida do lado B: '))
        ladoC = float(input('Informe a medida do lado C: '))
    except:
        print('Erro. Digite valores válidos.')
    else:
        break

novoTriangulo = Triangulo(ladoA, ladoB, ladoC)

while True:
    print('*' * 35)
    
    print({
        'Calcular Perímetro': 1,
        'Verificar tipo de Triângulo': 2,
        'Informações Gerais': 3,
        'Maior lado': 4,
        'Sair': 5
    })

    try:
        escolha = int(input('O que deseja fazer? '))
    except ValueError:
        print('Erro: opção inválida.')
    else:
        if escolha == 1:
            print(novoTriangulo.perimetro())
        elif escolha == 2:
            print(novoTriangulo.tipoTriangulo())
        elif escolha == 3:
            print(novoTriangulo.infoTriangulo())
        elif escolha == 4:
            print(novoTriangulo.getMaiorLado())
        elif escolha == 5:
            break
        else:
            print('Opção inválida. Tente novamente.')

print('Obrigado por usar nosso gerador de triângulos! Encerrando...')