#Crie uma função que receba um número e retorne se ele é PAR ou ÍMPAR.

def par_ou_impar(numero):
    if numero % 2 != 0:
        print("O número e Impar")
    else:
        print("O número e Par")



numero = int(input("Informe o número: "))
par_ou_impar(numero)