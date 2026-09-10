class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

        def ler(self):
            return "Estou lendo um livro."

        class Romance(Livro):
            def ler(self):
                return "Estou lendo um romance."

        class Terror(livro):
            def ler(self):
                return "Estou lendo um livro de terror."

        class ficcao(Livro):
                def ler(self):
                    return "Estou lendo um livro de ficção."


        livro1 = Romance("Orgulho e Preconceito", "Jane Austen")
        livro2 = Terror("O Iluminado", "Stephen King")
        livro3 = ficcao("Duna", "Frank Herbert")


        livros = [livro1, livro2, livro3]

        for livro in livros:
            print("titulo:", livro.titulo)
            print("autor:", livro.autor)
            print(livro.ler())
            print()