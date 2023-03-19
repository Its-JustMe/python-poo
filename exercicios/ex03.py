#   EXERCÍCIOS PYTHON
'''
    Crie uma classe Livro que possui os
    atributos nome,	qtdPaginas,	autor	e	preço.	
    - Crie os métodos getPreco para obter	o	valor	
    do	preco	e	o	método setPreco para setar
    um	novo	valor	do	preco.	
'''

class Livro:
    def __init__ (self, nome:str, paginas:int, autor:str, preco:float):
        self.titulo_livro = nome
        self.qtd_paginas = paginas
        self.autor_livro = autor
        self.preco_livro = preco

    # Métodos Getter
    def get_titulo_livro (self):
        return self.titulo_livro
    
    def get_qtd_paginas (self):
        return self.qtd_paginas
    
    def get_autor_livro (self):
        return self.autor_livro
    
    def get_preco_livro (self):
        return self.preco_livro
    
    def set_titulo_livro (self, titulo):
        self.titulo_livro = titulo
    
    def set_qtd_paginas (self, paginas):
        self.qtd_paginas = paginas

    def set_autor_livro (self, autor):
        self.autor_livro = autor
    
    def set_preco_livro (self, preco):
        self.preco_livro = preco


livros = [
    Livro('Livro Legal', 350, 'Anônimo', 200),
    Livro('Livro Bonito', 600, 'Alguém Aí', 450),
    Livro('Livro Interessante', 125, 'Outro Alguém', 120)
]

livraria = {
    'Livro 0': livros[0].get_titulo_livro(),
    'Livro 1': livros[1].get_titulo_livro(),
    'Livro 2': livros[2].get_titulo_livro()
}

while True:
    print('*' * 65)

    print(livraria)

    acao = int(input('1- Consultar preço / 2- Alterar Preço / 3- Sair '))
    if acao == 1:
        acao = int(input('Digite o número do livro que deseja ver: [0, 1, 2] '))
        print(f'{livraria["Livro " + str(acao)]}: R${livros[acao].get_preco_livro():.2f}')
    elif acao == 2:
        acao = int(input('Digite o número do livro que deseja alterar o preço: [0, 1, 2] '))
        novoPreco = float(input('Insira o novo preço: '))

        livros[acao].set_preco_livro(novoPreco)
    else:
        break
    
print('Programa encerrado.')