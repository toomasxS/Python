tarefas = ["Tarefa 1", "Tarefa 2", "Tarefa 3"]

# Adicionar uma tarefa ao final da lista
tarefas.append("Estudar Python")

# Adicionar várias tarefas ao final da lista
tarefas.extend(["Fazer exercícios", "Ler um livro"])

# Inserir uma tarefa numa posição específica
tarefas.insert(1, "Rever a matéria")

# Remover uma tarefa pelo nome
tarefas.remove("Tarefa 2")

# Remover a última tarefa
tarefa_removida = tarefas.pop()
print("Tarefa removida:", tarefa_removida)

# Remover uma tarefa numa posição específica
tarefa_removida = tarefas.pop(1)
print("Tarefa removida:", tarefa_removida)

# Contar quantas vezes uma tarefa aparece na lista
tarefa = "Estudar Python"
ocorrencias = tarefas.count(tarefa)
print(f'"{tarefa}" aparece {ocorrencias} vez(es).')

# Encontrar o índice da primeira ocorrência de uma tarefa
tarefa = "Estudar Python"
indice = tarefas.index(tarefa)
print(f'"{tarefa}" está no índice {indice}.')

# Ordenar as tarefas em ordem alfabética
tarefas.sort()
print("Tarefas em ordem alfabética:", tarefas)

# Inverter a ordem atual das tarefas
tarefas.reverse()
print("Tarefas em ordem inversa:", tarefas)

# Criar uma cópia independente da lista de tarefas
tarefas_copia = tarefas.copy()

# Remover todas as tarefas
tarefas.clear()

print("Lista original:", tarefas)
print("Cópia independente:", tarefas_copia)