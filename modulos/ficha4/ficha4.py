aluno = {
    "Nome": "Ana Silva",
    "Idade": 17,
    "Disciplinas": ["Matemática", "Física", "Informática"],
    "Notas": {
        "Matemática": 18,
        "Física": 17,
        "Informática": 19
    }
}

# Adicionar Português e a respetiva nota
aluno["Disciplinas"].append("Português")
aluno["Notas"]["Português"] = 16

# Atualizar a idade
aluno["Idade"] = 18

# Imprimir disciplinas e notas
for disciplina, nota in aluno["Notas"].items():
    print(f"{disciplina}: {nota}")

# Calcular e imprimir a média
media = sum(aluno["Notas"].values()) / len(aluno["Notas"])
print(f"Média das notas: {media}")

def contar_caracteres(texto):
    frequencias = {}

    for caractere in texto:
        frequencias[caractere] = frequencias.get(caractere, 0) + 1

    return frequencias

resultado = contar_caracteres("banana")
print(resultado)

