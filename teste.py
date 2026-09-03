class aluno:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def apresentar(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Email:", self.email)



aluno1 = aluno("Leticia", 16, None)

aluno1.apresentar()

class livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}"

    def adicionar_paginas
