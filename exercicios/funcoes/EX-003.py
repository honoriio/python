# Crie uma função que receba 3 números e retorne o maior deles.
numeros = []

def maior(*numero):
    maior = max(numero)

    return maior



for i in range(3):
    num = int(input("Informe o Numero: "))
    numeros.append(num)

numero_maior = maior(*numeros)
print(f"O maior Número é: {numero_maior}")
