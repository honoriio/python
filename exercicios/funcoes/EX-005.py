# Crie uma função que receba um número e mostre a tabuada dele de 1 a 10.

def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

n1 = int(input("Informe um Numero: "))
tabuada(n1)
