from models import Pessoas, Usuarios


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Lorenzo', idade=7)
    print(pessoa)
    pessoa.save()


# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Lorenzo').first()
    print(pessoa.idade)


# Altera dados na tabela pessoa
def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Lorenzo').first()
    pessoa.nome = 'Felipe'
    pessoa.save()


# Exclui dados na tabela pessoa
def excluir_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Lorenzo').first()
    pessoa.delete()


def insere_usuarios(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)




if __name__ == '__main__':
    insere_usuarios('lorenzo', '1234')
    insere_usuarios('lucas', '4321')
    consulta_todos_usuarios()
    # insere_pessoas()
    # altera_pessoas()
    #excluir_pessoas()
    #consulta_pessoas()
