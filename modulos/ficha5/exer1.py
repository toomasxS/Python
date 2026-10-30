aluno = {
    "Nome": "STASTAO",
    "Idade": 16,
    "Disciplinas": ["Matemática", "Física", "Informática"],
    "Notas": {
        "Matemática": 17,
        "Física": 17,
        "Informática": 19,
    },
}

aluno["Disciplinas"].append("Português")
aluno["Notas"]["Português"] = 16
aluno["Idade"] = 18

for disciplina, nota in aluno["Notas"].items():
    print(f"{disciplina}: {nota}")

media = sum(aluno["Notas"].values()) / len(aluno["Notas"])
print(f"Média das notas: {media}")