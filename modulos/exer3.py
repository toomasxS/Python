from random import randint
import os
#x = randint
resposta = 'S'
pontuacoes = [100, 80, 60, 40, 30, 20, 10]
pontuacao = 0
while resposta == 'S':
    os.system("clear")
    #declarar ....
    tentativas = 0
    numGerado = randint(1,100)
    print(numGerado)
    #Ciclo de Tentativas
    while tentativas < 7:
        
        meuNum = int(input("Tente o valor: "))
        while meuNum < 1 or meuNum > 100:
             print("Impossível! O número deve estar entre 1 e 100!")
             meuNum = int(input("Tente denovo: "))
             os.system("clear")
        if meuNum == numGerado:
            pontuacao = pontuacoes[tentativas]
            print(f"Boa, acertou o número em {tentativas + 1} tentativas e fez {pontuacao} pontos.")
            break
        tentativas = tentativas + 1
        if meuNum < numGerado:
            print("O número que você quer descobrir é maior!")
        else:
                print("O número que você quer descobrir é menor!")
    if tentativas >= 7:
         print(f"Sinto muito! O número gerado foi {numGerado}")
    resposta = (input("Deseja jogar denovo? (S/N)")).upper()