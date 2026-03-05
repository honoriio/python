numeros = []

pares = []

for i in range(10):
    num = int(input(f"Informe o {i+1}º Número: "))
    numeros.append(num)

for num in numeros:
    if num % 2 ==0:
        pares.append(num)

print(f"A lista completa contém: {numeros}")
print(f"A lista com números pares contem: {pares}")
