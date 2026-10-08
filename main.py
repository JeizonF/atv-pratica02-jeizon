from consultas import (
    buscar_livros_por_titulo,
    listar_livros,
    listar_livros_disponiveis,
    listar_livros_por_autor,
)
from database import criar_banco, nova_sessao
from operacoes import devolver_livro, emprestar_livro
from seed import popular_banco


criar_banco()

with nova_sessao() as session:
    popular_banco(session)

    print("\nTodos os livros:")
    listar_livros(session)

    print("\nLivros disponíveis:")
    listar_livros_disponiveis(session)

    print("\nBusca por parte do título:")
    buscar_livros_por_titulo(session, "livro3")

    print("\nLivros de um autor:")
    listar_livros_por_autor(session, "autor2")

    print("\nEmprestando um livro:")
    emprestar_livro(session, "livro2")

    print("\nDevolvendo um livro:")
    devolver_livro(session, "livro1")
