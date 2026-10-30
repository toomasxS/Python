lista = [1,2,3,4,5,6,7,8,9,10]

pares = []
for num in lista:
    if num % 2 == 0:
        pares.append(num)
print (pares)

quadrados = []
for num in lista:
    quadrados.append(num ** 2)
print (quadrados)

palavras = ["jogar", "correr", "nadar", "pedalar"]
for palavra in palavras:
    print(palavra, len(palavra))

listanums = []
for num in range(5,11):
    listanums.append(num)
print(listanums)

nome = 'MarcelO ViEiRa amorIM'
letrasM = []
for letra in nome:
    if letra == letra.upper() and " " != letra.upper():
        letrasM.append(letra)
print(letrasM)

listamult = [mult*2 if mult % 3 == 0 else mult for mult in lista]
print(listamult)

nomes = ["Ana", "Bruno", "alice", "Andreia", "Carlos"]
nomesA = [nome.upper() for nome in nomes if nome.upper().startswith("A")]
print(nomesA)

frutas = ["banana", "uva", "laranja", "pera", "abacaxi"]
comprimentos = [len(fruta) if len(fruta) > 5 else 0 for fruta in frutas]
print(comprimentos)