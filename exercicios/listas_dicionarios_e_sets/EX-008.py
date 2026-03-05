numeros = []

for i in range(5):
    num = float(input(f"Informe o {i+1}º Número: "))
    numeros.append(num)

print(f"A lista Normal: {numeros}")
print(f"A lista invertida: {numeros.reverse()}")
