numeros = []

for i in range(8):
    num = int(input(f"Informe o {i+1}º Número: "))
    if num > 10:
        numeros.append(num)
    else:
        continue

print(f"Existem {len(numeros)} Número Maiores que 10.")
