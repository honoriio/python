# Crie uma função que receba 3 notas e retorne a média.
#Depois mostre se o aluno está:
#Aprovado (média ≥ 7)
#Recuperação (média entre 5 e 6.9)
#Reprovado (média < 5)

notas = []

def media(*numeros):
    nota_media = sum(numeros) / len(numeros)
    return nota_media

for i in range(3):
    nota = float(input("Informe as notas: "))
    notas.append(nota)

notas_media = media(*notas)

if notas_media >= 7:
    print(f"A sua media e {notas_media}, e voce esta Aprovado.")
elif notas_media >= 5 and notas_media <= 6.9:
    print(f"A sua media e {notas_media}, voce esta de recuperação.")
else:
    print(f"A sua media e {notas_media}, e voce esta reprovado.")
