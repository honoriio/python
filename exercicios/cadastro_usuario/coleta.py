import re
from validacao import validar_cpf

def nome():
    while True:
        nome = input("Nome: ")

        if len(nome) >= 3:
            return nome
        else:
            print("O nome deve ter pelo menos 3 letras. ")


def idade():
    while True:
        try:
            idade = int(input("Idade: "))
            if idade > 0:
                return idade
            else:
                print("Idade Invalida.")
        except ValueError:
            print("Digite apenas números.")    


def pedir_email():
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    while True:
        email = input("Email: ").strip()

        if not email:
            print("O email não pode estar vazio.")
            continue

        if re.match(padrao, email):
            print("Email válido.")
            return email
        else:
            print("Email inválido.")


def cpf():
    while True:
        cpf = input("CPF: ")

        if validar_cpf(cpf):
            print("CPF válido")
            break
        else:
            print("CPF inválido")

