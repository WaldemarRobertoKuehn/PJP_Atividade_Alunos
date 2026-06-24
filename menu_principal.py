from modelos import Aluno, listar_alunos

def exibir_menu():
    print("\n===================")
    print("MENU DE ALUNOS")
    print("0 - Sair")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("===================\n")

def cadastrar():
    nome_aluno = input("Digite o nome: ")
    media_aluno = float(input("Digite a média: "))   

    aluno = Aluno(nome_aluno, media_aluno)
    aluno.salvar()
    print("Aluno cadastrado com sucesso!")

def mostrar():
    for aluno in listar_alunos():
        aluno.exibir()


while True:    
    exibir_menu()
    opcao = input("Digite uma opção: ")

    if opcao == "0":
        break
    elif opcao == "1":
        cadastrar()
    elif opcao == "2":
        mostrar()
    else:
        print("Opção Inválida! Tente novamente.")