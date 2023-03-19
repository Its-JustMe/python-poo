#   EXERCÍCIOS PYTHON
'''
    Implemente uma classe Aluno,	que deve ter os
    seguintes atributos:	nome,	curso,	tempoSemDormir
    (em horas).		Essa classe deverá ter os seguintes
    métodos:	
    - estudar	(que recebe como parâmetro	a	qtd	de	horas de	
    estudo	e	acrescenta tempoSemDormir)	
    - Dormir	(que recebe como parâmetro	a	qtd	de	horas de	
    sono	e	reduz tempoSemDormir	)	
    Crie	um	código	de	teste	da	classe,	criando	um	objeto
    da	classe aluno	e	usando os métodos estudar e dormir.	 
    Ao	final	imprima quanto	tempo	o	aluno está sem
    dormir
'''

class Aluno:
    def __init__ (self, nome, curso, tempoSemDormir):
        self.nome_aluno = nome
        self.curso_aluno = curso
        self.tempo_sem_dormir = tempoSemDormir

    # Métodos Getters
    def get_nome_aluno (self):
        return self.nome_aluno
    def get_curso_aluno (self):
        return self.curso_aluno
    def get_tempo_sem_dormir (self):
        return self.tempo_sem_dormir
    
    # Métodos da Classe
    def estudar (self, horasEstudo):
        print(f'{self.get_nome_aluno()} estudou {horasEstudo} horas hoje.')
        self.tempo_sem_dormir += horasEstudo

    def dormir (self, horasSono):
        print(f'{self.get_nome_aluno()} dormiu {horasSono} horas de sono hoje.')
        self.tempo_sem_dormir -= horasSono

novoAluno = Aluno('Arthur', 'Informática Para Internet', 0)

diasDaSemana = {
    'Segunda-feira': novoAluno.estudar(6),
    'Terça-feira': novoAluno.estudar(8),
    'Quarta-feira': novoAluno.estudar(10),
    'Quinta-feira': novoAluno.dormir(4),
    'Sexta-feira': novoAluno.estudar(5),
    'Sábado': novoAluno.dormir(9),
    'Domingo': novoAluno.dormir(4)
}

print(f'O aluno {novoAluno.get_nome_aluno()} do curso {novoAluno.get_curso_aluno()} está {novoAluno.get_tempo_sem_dormir()} horas sem dormir.')