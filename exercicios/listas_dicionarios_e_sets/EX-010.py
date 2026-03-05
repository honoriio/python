numeros = []

for i in range(6):
    num = float(input(f"Informe o {i+1} Número: "))
    numeros.append(num)

media = sum(numeros) / len(numeros)

print(f"Essa e a media da lista: {media:.2f}")
