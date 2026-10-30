from random import randint

nums = []

for _ in range(30):
    i = randint(1, 100)
    nums.append(i)

soma = sum(nums)
maior = max(nums)
menor = min(nums)
media = soma / len(nums)

nPares = 0
nImpares = 0
nMaioresMedia = 0
listaMaiorMedia = []

for num in nums:
    if num % 2 == 0:
        nPares = nPares + 1
    else:
        nImpares = nImpares + 1
    if num > media:
        nMaioresMedia = nMaioresMedia + 1
        listaMaiorMedia.append(num)

print("A lista é ", nums)
print("A soma da lista é ", soma)
print("O número maior é ", maior)
print("O número menor é ", menor)
print("A média da lista é ", media)
print("A lista tem ", nPares, " números pares e tem ", nImpares, " números impares")
print("A lista tem ", nMaioresMedia, " números maiores que a média")
print("A lista com os números maiores que a média ", listaMaiorMedia)
