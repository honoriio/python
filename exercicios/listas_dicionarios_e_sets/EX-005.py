pares = []

for i in range(10):
    numero = int(input(f"Informe o {i+1}º Número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else: 
        continue

if not pares:
    print("O usúario não informou nenhum número par.")
else:
    print(f"Os números pares informados são {pares}")
