from random import randint
from time import sleep

gridSizeX = 100
gridSizeY = 100

listOfDenidedSpawns = ["1,1","1,1"]
valueDenidedX = 2
valueDenidedY = 1

attackSpawnRadiusMaxX = gridSizeX
attackSpawnRadiusMaxY = gridSizeY - 30
attackSpawnRadiusMinX = gridSizeX - gridSizeX
attackSpawnRadiusMinY = gridSizeY - gridSizeY
defenseSpawnRadiusMaxX = gridSizeX
defenseSpawnRadiusMaxY = gridSizeY
defenseSpawnRadiusMinX = gridSizeX - gridSizeX
defenseSpawnRadiusMinY = gridSizeY - 50



for i in range(12):
    valueDenidedX = 1
    for i in range(100):
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1
valueDenidedY = 22
for i in range(12):
    valueDenidedX = 52
    for i in range(4):
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1

print(listOfDenidedSpawns)
def attackPlayer1():
    attackPos1X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos1Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    print("Attack Player 1, X - " + str(attackPos1X) + ", Y - " + str(attackPos1Y))
    attackPos1 = str(attackPos1X) + "," + str(attackPos1Y)
    return attackPos1
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
    print("Defense Player 1, X - " + str(defensePos1X) + ", Y - " + str(defensePos1Y))
    global defensePos1
    defensePos1 = str(defensePos1X) + "," + str(defensePos1Y)

def defensePlayer2():
    defensePos2X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos2Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Defense Player 2, X - " + str(defensePos2X) + ", Y - " + str(defensePos2Y))
    global defensePos2
    defensePos2 = str(defensePos2X) + "," + str(defensePos2Y)
def defensePlayer3():
    defensePos3X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos3Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Defense Player 3, X - " + str(defensePos3X) + ", Y - " + str(defensePos3Y))
    global defensePos3
    defensePos3 = str(defensePos3X) + "," + str(defensePos3Y)
def defensePlayer4():
    defensePos4X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos4Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Defense Player 4, X - " + str(defensePos4X) + ", Y - " + str(defensePos4Y))
    global defensePos4
    defensePos4 = str(defensePos4X) + "," + str(defensePos4Y)
def defensePlayer5():
    defensePos5X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos5Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Defense Player 5, X - " + str(defensePos5X) + ", Y - " + str(defensePos5Y))
    global defensePos5
    defensePos5 = str(defensePos5X) + "," + str(defensePos5Y)

def defenseBondaryCheck1():
    spawnAccepted = False
    while spawnAccepted == False:
        defensePlayer1()
        if defensePos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Spawn Denided")
        else:
            spawnAccepted = True
            print("Denfense Spawn Accepted")
        sleep(1)
def defenseBondaryCheck2():
    spawnAccepted = False
    while spawnAccepted == False:
        defensePlayer2()
        if defensePos2 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Spawn Denided")
        else:
            spawnAccepted = True
            print("Denfense Spawn Accepted")
        sleep(1)
def defenseBondaryCheck3():
    spawnAccepted = False
    while spawnAccepted == False:
        defensePlayer3()
        if defensePos3 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Spawn Denided")
        else:
            spawnAccepted = True
            print("Denfense Spawn Accepted")
        sleep(1)
def defenseBondaryCheck4():
    spawnAccepted = False
    while spawnAccepted == False:
        defensePlayer4()
        if defensePos4 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Spawn Denided")
        else:
            spawnAccepted = True
            print("Denfense Spawn Accepted")
        sleep(1)
def defenseBondaryCheck5():
    spawnAccepted = False
    while spawnAccepted == False:
        defensePlayer5()
        if defensePos5 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Spawn Denided")
        else:
            spawnAccepted = True
            print("Denfense Spawn Accepted")
        sleep(1)







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
defenseBondaryCheck1()
sleep(1)
defenseBondaryCheck2()
sleep(1)
defenseBondaryCheck3()
sleep(1)
defenseBondaryCheck4()
sleep(1)
defenseBondaryCheck5()
sleep(1)







