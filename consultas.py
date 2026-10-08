from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    listar = select(Livro)
    livros = session.scalars(listar).all()
    for livro in livros:
        print(f'- {livro.titulo} por {livro.autor.nome}. disponivel: {livro.disponivel}')
    # TODO: use select(Livro) e acesse livro.autor.nome.


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    listar = select(Livro).where(Livro.disponivel == True)
    livros = session.scalars(listar).all()
    for livro in livros:
        print(f'- {livro.titulo}. disponivel: {livro.disponivel}')
    # TODO: filtre Livro.disponivel igual a True.
    


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    listar = select(Livro).where(Livro.titulo.contains(trecho))
    livros = session.scalars(listar).all()
    for livro in livros:
        print(f'- {livro.titulo}. disponivel: {livro.disponivel}')
    # TODO: use contains ou like no título.
    


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    listar = select(Autor).where(Autor.nome == nome_autor)
    autor = session.scalars(listar).first()
    if autor:
        for livro in autor.livros:
            print(f'- {livro.titulo} por {autor.nome}. disponivel: {livro.disponivel}')
    else:
        print(f"Autor '{nome_autor}' não encontrado.")
    # TODO: busque o autor e navegue por autor.livros.
    
