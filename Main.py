from random import randint
from time import sleep

gridSizeX = 1000
gridSizeY = 1000

attackSpawnRadiusMaxX = gridSizeX
attackSpawnRadiusMaxY = gridSizeY - 600
attackSpawnRadiusMinX = gridSizeX - gridSizeX
attackSpawnRadiusMinY = gridSizeY - gridSizeY
defenseSpawnRadiusMaxX = gridSizeX
defenseSpawnRadiusMaxY = gridSizeY
defenseSpawnRadiusMinX = gridSizeX - gridSizeX
defenseSpawnRadiusMinY = gridSizeY - 300

def attackPlayer1():
    attackPos1X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos1Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    print("Attack Player 1, X - " + str(attackPos1X) + ", Y - " + str(attackPos1Y))
def attackPlayer2():
    attackPos2X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos2Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    print("Attack Player 2, X - " + str(attackPos2X) + ", Y - " + str(attackPos2Y))
def attackPlayer3():
    attackPos3X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos3Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    print("Attack Player 3, X - " + str(attackPos3X) + ", Y - " + str(attackPos3Y))
def attackPlayer4():
    attackPos4X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos4Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    print("Attack Player 4, X - " + str(attackPos4X) + ", Y - " + str(attackPos4Y))
def attackPlayer5():
    attackPos5X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos5Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    print("Attack Player 5, X - " + str(attackPos5X) + ", Y - " + str(attackPos5Y))

def defensePlayer1():
    defensePos1X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos1Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Attack Player 1, X - " + str(defensePos1X) + ", Y - " + str(defensePos1Y))
def defensePlayer2():
    defensePos2X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos2Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Attack Player 2, X - " + str(defensePos2X) + ", Y - " + str(defensePos2Y))
def defensePlayer3():
    defensePos3X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos3Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Attack Player 3, X - " + str(defensePos3X) + ", Y - " + str(defensePos3Y))
def defensePlayer4():
    defensePos4X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos4Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Attack Player 4, X - " + str(defensePos4X) + ", Y - " + str(defensePos4Y))
def defensePlayer5():
    defensePos5X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos5Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Attack Player 5, X - " + str(defensePos5X) + ", Y - " + str(defensePos5Y))


print("Printing Attack Positions")
sleep(5)
attackPlayer1()
sleep(1)
attackPlayer2()
sleep(1)
attackPlayer3()
sleep(1)
attackPlayer4()
sleep(1)
attackPlayer5()
sleep(1)
print("Printing Defense Positions")
sleep(5)
defensePlayer1()
sleep(1)
defensePlayer2()
sleep(1)
defensePlayer3()
sleep(1)
defensePlayer4()
sleep(1)
defensePlayer5()
sleep(1)







