from random import randint
from time import sleep

gridSizeX = 1000
gridSizeY = 1000

attackSpawnRadiusMaxX = gridSizeX - 700
attackSpawnRadiusMaxY = gridSizeY - 600


def attackEnemy1():
    attackPos1X = randint(0, attackSpawnRadiusMaxX)
    attackPos1Y = randint(0, attackSpawnRadiusMaxY)
    print("Attack Player 1, X - " + str(attackPos1X) + ", Y - " + str(attackPos1Y))
def attackEnemy2():
    attackPos2X = randint(0, attackSpawnRadiusMaxX)
    attackPos2Y = randint(0, attackSpawnRadiusMaxY)
    print("Attack Player 2, X - " + str(attackPos2X) + ", Y - " + str(attackPos2Y))
def attackEnemy3():
    attackPos3X = randint(0, attackSpawnRadiusMaxX)
    attackPos3Y = randint(0, attackSpawnRadiusMaxY)
    print("Attack Player 3, X - " + str(attackPos3X) + ", Y - " + str(attackPos3Y))
def attackEnemy4():
    attackPos4X = randint(0, attackSpawnRadiusMaxX)
    attackPos4Y = randint(0, attackSpawnRadiusMaxY)
    print("Attack Player 4, X - " + str(attackPos4X) + ", Y - " + str(attackPos4Y))
def attackEnemy5():
    attackPos5X = randint(0, attackSpawnRadiusMaxX)
    attackPos5Y = randint(0, attackSpawnRadiusMaxY)
    print("Attack Player 5, X - " + str(attackPos5X) + ", Y - " + str(attackPos5Y))

print("Printing Debug text")
sleep(5)
attackEnemy1()
sleep(1)
attackEnemy2()
sleep(1)
attackEnemy3()
sleep(1)
attackEnemy4()
sleep(1)
attackEnemy5()





