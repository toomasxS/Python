def saudacao(nome, curso="GPSI"):
    print(f"Bem-vindo ao curso de {curso}, {nome}!")

saudacao("Carlos")

def criar_lista(*alunos):
    lista = []
    for aluno in alunos:
        lista.append(aluno)
    return lista

x =  criar_lista("Ana","Joao")
y = criar_lista("Rui","Maria","Fernando","Joana","Isa")
z = ["A1","A2","A3","A4"]

nova_lista = criar_lista(*z)
print(x,y, nova_lista)

def config(**configuracoes):
    for chave, valor in configuracoes:
        print(f"{chave}: {valor}")

config(memoria="16GB",disco = "SSD 256GB", sistemas="Windows 11")

dicionario = { "memoria": "8GB", "disco": "SSD 512GB", "sistema": "Ubuntu"}
config(**dicionario)

def maiores_dois_valores(n1,n2,n3):
    maior = n1
    maior2 = 0
    if n2 > maior and n2 > n3:
        maior = n2
        if n1 > n3:
            maior2 = n1
        else:
            maior2 = n3

    return (maior, maior2)
