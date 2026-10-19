from random import randint

notas = []

for _ in range(15):
    nota = randint(0, 20)
    notas.append(nota)

aprovados = 0
reprovados = 0
notasAltas = 0

somaNotas = sum(notas)
notaMaxima = max(notas)
notaMinima = min(notas)
mediaNotas = somaNotas / len(notas)
percentagem = 0

for nota in notas:
    if nota >= 10:
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1

    if nota >= 16:
        notasAltas = notasAltas + 1

percentagem = (aprovados / len(notas)) * 100

print("Tem", aprovados, "alunos aprovados e", reprovados, "alunos reprovados.")
print("Tem", notasAltas, "alunos com nota maior ou igual a 16.")
print("A maior nota é", notaMaxima)
print("A menor nota é", notaMinima)
print("A média é de", mediaNotas)
print("A percentagem de aprovados é de", percentagem, "%")