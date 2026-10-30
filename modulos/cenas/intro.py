from random import randint
import os
from modulos.cenas.biblioteca import z

x = 5
print(f"O valor de x é {x}")

for _ in range(5):
    y = randint(5,12)
    print(y)

    os.system("cls")

    x = y + z
    print (x)

    