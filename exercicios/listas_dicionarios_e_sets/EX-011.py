numeros = []
pares = []

for i in range(10):
    num = int(input(f"Informe o {i+1}º Número: "))
    numeros.append(num)
    if num %2 ==0:
        pares.append(num)

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / len(numeros)

print(f"O maior número da lista é: {maior}")
print(f"O Menor número da lista é: {menor}")
print(f"A soma da lista é: {soma}")
print(f"A media da lista é: {media}")
print(f"Na lista temos {len(pares)} Números pares.")
