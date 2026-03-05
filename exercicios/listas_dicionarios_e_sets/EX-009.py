numeros = []

for i in range(10):
    num = float(input(f"Informe o {i+1}º Número: "))
    numeros.append(num)

positiva = [x for x in numeros if x >= 0]

print(f"Essa e lista normal: {numeros}")
print(f"Esta e a lista Positiva: {positiva}")
