nums = [2,5,8,11,7,9,13]

soma = sum(nums)
maior = max(nums)
menor = min(nums)
media = soma / len(nums)

# Imprimir a lista
print(nums)
# Imprimir um elemnto da lista
print(nums[2])
#Inserir um novo elemento no final da lista 
nums.append(17)
# Inserir vários elemntos no final da lista
nums.extend([12, 16])
# Inseriri numa posição específica
nums.insert(3, 29)

#Remover o elemnto final da lista
nums.pop()
#Remover um elemnto de uma posição específica da lista pelo índice
nums.pop(2)
#Remover um elemnto de uma poisção específica da lista pelo valor
nums.remove(17)
# Número de elementos da lista
total = len(nums) # 8

for n in nums: # Para cada elemento da minha lista
    if n <= 10:
        print(n, end=" ")

for indice in range(len(nums)):
    if nums[indice] <= 10:
        print(nums[indice], end=" ")

