from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    """Marque um livro como indisponível."""
    emprestar = select(Livro).where(Livro.titulo == titulo)
    res = session.execute(emprestar).scalar_one_or_none()
    if res is None:
        print(f'livro "{titulo}" nao achado')
    elif not res.disponivel:
        print(f'livro "{titulo}" n ta disponivel')
    else:
        res.disponivel = False
        session.commit()
        print(f'Livro "{titulo}" emprestado com sucesso.')
    # TODO: busque o livro pelo título.
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver indisponível, exiba uma mensagem.
    # TODO: se estiver disponível, altere disponivel para False e faça commit.
    pass


def devolver_livro(session, titulo):
    """Marque um livro como disponível."""
    devolver = select(Livro).where(Livro.titulo == titulo)
    res = session.execute(devolver).scalar_one_or_none()
    if res is None:
        print(f'livro "{titulo}" nao achado')
    elif res.disponivel:
        print(f'livro "{titulo}" ja ta disponivel')
    else:
        res.disponivel = True
        session.commit()
        print(f'Livro "{titulo}" devolvido com sucesso.')
    # TODO: busque o livro pelo título.
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver disponível, exiba uma mensagem.
    # TODO: se estiver indisponível, altere disponivel para True e faça commit.
    pass
