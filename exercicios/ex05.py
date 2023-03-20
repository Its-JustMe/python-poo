#   EXERCÍCIOS PYTHON
'''
    Crie uma classe Aluno,	que possui como atributo	
    um	nome	e	cpf.	Crie outra classe chamada 
    Equipe,	que possui como atributo uma lista	de	
    participantes	do	Fpo Aluno	e	outro	
    atributo chamado projeto.	
    Crie uma terceira classe chamada GerenciadorEquipes. Essa
    classe possui como atributo uma lista	de	todas	as	equipes
    formadas.	Ela deverá possuir	o	método criarEquipe,	que recebe
    uma lista	de	alunos	de	uma equipe	e	diz	se	a	
    equipe pode ser formada ou não.	Caso não haja nenhum aluno	
    da	equipe	a	ser formada em uma outra equipe	com	o 
    mesmo projeto,	então	a equipe é criada	e	acrescentada 
    à lista.	Caso contrário é
    informada que	a	equipe não pode ser criada.
'''

class Aluno:
    def __init__ (self, nome, cpf):
        self.nome_aluno = nome
        self.cpf_aluno = cpf

    # Getters e Setters

    @property
    def nome_aluno(self):
        return self._nome_aluno

    @nome_aluno.setter
    def nome_aluno(self, novo_nome):
        self._nome_aluno = novo_nome

    @property
    def cpf_aluno(self):
        return self._cpf_aluno

    @cpf_aluno.setter
    def cpf_aluno(self, novo_cpf):
        self._cpf_aluno = novo_cpf

class Equipe:
    def __init__(self, projeto):
        self.lista_participantes = []
        self.nome_projeto = projeto

    # Getters e Setters

    @property
    def lista_participantes (self):
        return self.lista_participantes
    
    @property
    def nome_projeto (self):
        return self.nome_projeto
    
    @lista_participantes.setter
    def lista_participantes (self, participante):
        if participante in self.lista_participantes:
            return False
        self.lista_participantes.append(participante)
    
    @nome_projeto.setter
    def nome_projeto (self, novoNomeProjeto):
        self.nome_projeto = novoNomeProjeto

class Gerenciador:
    def __init__ (self):
        self.lista_equipes = []

    # Getter e Setter
    @property
    def lista_equipes (self):
        return self.lista_equipes
    
    @lista_equipes.setter
    def set_lista_equipes (self, equipe):
        if equipe in self.lista_equipes:
            return False
        self.lista_equipes.append(equipe)

    # Métodos
    def criarEquipe (self, listaAlunos:list):
        permissao = True

        for aluno in listaAlunos:
            if aluno in self.lista_equipes:
                permissao = False
                break

        if permissao:
            self.lista_equipes.append(listaAlunos)
            return 'Equipe formada.'
        else:
            return 'A equipe não pode ser formada.'