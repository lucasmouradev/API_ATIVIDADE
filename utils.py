from models import Pessoas


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


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoas()
    excluir_pessoas()
    consulta_pessoas()
