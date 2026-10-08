from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    autor1 = Autor(nome="Autor 1", pais="País 1")
    autor2 = Autor(nome='autor2', pais='pais2')
    autor3 = Autor(nome='autor3', pais='pais3')
    livro1 = Livro(titulo='livro1', ano=2020, autor=autor1, disponivel=True)
    livro2 = Livro(titulo='livro2', ano=2021, autor=autor1, disponivel=False)
    livro3 = Livro(titulo='livro3', ano=2022, autor=autor2, disponivel=True)
    livro4 = Livro(titulo='livro4', ano=2023, autor=autor2, disponivel=False)
    livro5 = Livro(titulo='livro5', ano=2024, autor=autor3, disponivel=True)
    livro6 = Livro(titulo='livro6', ano=2025, autor=autor3, disponivel=False)
    session.add_all([autor1, autor2, autor3, livro1, livro2, livro3, livro4, livro5, livro6])
    session.commit()
    # TODO: crie pelo menos 3 autores.
    # TODO: crie pelo menos 6 livros.
    # TODO: inclua livros disponíveis e indisponíveis.
    # TODO: use session.add ou session.add_all e finalize com session.commit().
    pass
