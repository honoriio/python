import sys
import os
import platform
import time

contas = []  

def menu():
    print("=" * 60)
    print("BANK".center(60))
    print("=" * 60)
    print("1 - Criar conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver contas")
    print("5 - Sair")
    print("-" * 60)

    opc = int(input("Escolha uma opção: "))
    return opc


def menu_criar_conta():
    print("=" * 60)
    print("CRIAR CONTA".center(60))
    print("=" * 60)


def cadastro():
    nome = input("Informe seu nome completo: ")
    nascimento = input("Informe a data de nascimento: ")
    cpf = input("Informe seu CPF: ")
    telefone = input("Informe seu telefone: ")
    email = input("Informe seu email: ")
    sexo = input("Informe seu sexo: ")
    cidade = input("Informe sua cidade: ")
    cep = input("Informe seu cep: ")
    rua = input("Informe sua rua: ")
    numero = input("Informe o numero da sua casa: ")
    bairro = input("Informe seu bairro: ")
    deposito_inicial = float(input("Informe o valor do deposito R$: "))

    cliente = [nome, nascimento, cpf, telefone, email, sexo, cidade, cep, rua, numero, bairro, deposito_inicial]

    contas.append(cliente)


def depositar():
    nome = input("Informe o nome do cliente: ")
    valor = float(input("Informe o valor do deposito: "))

    for cliente in contas:
        if cliente[0] == nome:
            cliente[11] += valor
            print("Deposito realizado com sucesso")
            return

    print("Conta não encontrada")


def sacar():
    nome = input("Informe o nome do cliente: ")
    valor = float(input("Informe o valor do saque: "))

    for cliente in contas:
        if cliente[0] == nome:
            if cliente[11] >= valor:
                cliente[11] -= valor
                print("Saque realizado com sucesso")
            else:
                print("Saldo insuficiente")
            return

    print("Conta não encontrada")


def ver_contas():
    if len(contas) == 0:
        print("Nenhuma conta cadastrada")
        return

    for cliente in contas:
        nome = cliente[0]
        saldo = cliente[11]
        print(f"Nome: {nome} | Saldo: R$ {saldo:.2f}")


def sair():
    sys.exit()


def limpar_tela():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


while True:
    time.sleep(2)
    limpar_tela()

    opc = menu()

    if opc == 1:
        menu_criar_conta()
        cadastro()

    elif opc == 2:
        depositar()

    elif opc == 3:
        sacar()

    elif opc == 4:
        ver_contas()

    elif opc == 5:
        sair()
