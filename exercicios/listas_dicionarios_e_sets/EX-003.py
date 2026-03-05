numeros = []

for i in range(5):
    numero = float(input(f"Informe o {i+1}º Número: "))
    numeros.append(numero)

menor = min(numeros)

print(f"O menor Número é: {menor}")
