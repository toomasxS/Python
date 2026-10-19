from random import randint

nums = []

for _ in range(30):
    i= randint(1, 100)
    nums.append(i)

soma = sum(nums)
maior = max(nums)
menor = min(nums)
media = soma / len(nums)

numPares = 0
numImpares = 0
numsMaioreMedia = 0

for num in nums:
    if num % 2 == 0:
        numPares = numPares + 1
    else:
        numImpares = numImpares + 1
    



print (nums)
print (soma)
print (maior)
print (menor)
print (media)
print (numPares)
print (numImpares)