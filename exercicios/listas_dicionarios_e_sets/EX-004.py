numeros = []

for i in range(5):
    numero = float(input(f"Informe o {i+1}º Número: "))
    numeros.append(numero)

soma = sum(numeros)

print(f"A soma dos números são: {soma}")
