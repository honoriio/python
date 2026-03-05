numeros = []

for i in range(5):
    numero = float(input(f"Informe o {i+1}º Número: "))
    numeros.append(numero)

maior = max(numeros)

print(f"O maior Número é: {maior}")
