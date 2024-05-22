from random import randint
from time import sleep

gridSizeX = 100
gridSizeY = 100

listOfDenidedSpawns = ["1,1","1,1"]
valueDenidedX = 2
valueDenidedY = 1

attackSpawnRadiusMaxX = 100
attackSpawnRadiusMaxY = 100
attackSpawnRadiusMinX = 1
attackSpawnRadiusMinY = 50
defenseSpawnRadiusMaxX = 100
defenseSpawnRadiusMaxY = 40
defenseSpawnRadiusMinX = 1
defenseSpawnRadiusMinY = 1


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
def attackSpawnPlayer1():
    attackPos1X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos1Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    print("Attack Player 1, X - " + str(attackPos1X) + ", Y - " + str(attackPos1Y))
    global attackPos1
    attackPos1 = str(attackPos1X) + "," + str(attackPos1Y)
def attackSpawnPlayer2():
    attackPos2X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos2Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    print("Attack Player 2, X - " + str(attackPos2X) + ", Y - " + str(attackPos2Y))
    global attackPos2
    attackPos2 = str(attackPos2X) + "," + str(attackPos2Y)
def attackSpawnPlayer3():
    attackPos3X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos3Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    print("Attack Player 3, X - " + str(attackPos3X) + ", Y - " + str(attackPos3Y))
    global attackPos3
    attackPos3 = str(attackPos3X) + "," + str(attackPos3Y)
def attackSpawnPlayer4():
    attackPos4X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos4Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    print("Attack Player 4, X - " + str(attackPos4X) + ", Y - " + str(attackPos4Y))
    global attackPos4
    attackPos4 = str(attackPos4X) + "," + str(attackPos4Y)
def attackSpawnPlayer5():
    attackPos5X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos5Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    print("Attack Player 5, X - " + str(attackPos5X) + ", Y - " + str(attackPos5Y))
    global attackPos5
    attackPos5 = str(attackPos5X) + "," + str(attackPos5Y)
def defenseSpawnPlayer1():
    defensePos1X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos1Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Defense Player 1, X - " + str(defensePos1X) + ", Y - " + str(defensePos1Y))
    global defensePos1
    defensePos1 = str(defensePos1X) + "," + str(defensePos1Y)

def defenseSpawnPlayer2():
    defensePos2X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos2Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Defense Player 2, X - " + str(defensePos2X) + ", Y - " + str(defensePos2Y))
    global defensePos2
    defensePos2 = str(defensePos2X) + "," + str(defensePos2Y)
def defenseSpawnPlayer3():
    defensePos3X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos3Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Defense Player 3, X - " + str(defensePos3X) + ", Y - " + str(defensePos3Y))
    global defensePos3
    defensePos3 = str(defensePos3X) + "," + str(defensePos3Y)
def defenseSpawnPlayer4():
    defensePos4X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos4Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Defense Player 4, X - " + str(defensePos4X) + ", Y - " + str(defensePos4Y))
    global defensePos4
    defensePos4 = str(defensePos4X) + "," + str(defensePos4Y)
def defenseSpawnPlayer5():
    defensePos5X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos5Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    print("Defense Player 5, X - " + str(defensePos5X) + ", Y - " + str(defensePos5Y))
    global defensePos5
    defensePos5 = str(defensePos5X) + "," + str(defensePos5Y)

def defenseSpawnBondaryCheck1():
    spawnAccepted = False
    while spawnAccepted == False:
        defenseSpawnPlayer1()
        if defensePos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Spawn Denided")
        else:
            spawnAccepted = True
            print("Denfense Spawn Accepted")
def defenseSpawnBondaryCheck2():
    spawnAccepted = False
    while spawnAccepted == False:
        defenseSpawnPlayer2()
        if defensePos2 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Spawn Denided")
        else:
            spawnAccepted = True
            print("Denfense Spawn Accepted")
def defenseSpawnBondaryCheck3():
    spawnAccepted = False
    while spawnAccepted == False:
        defenseSpawnPlayer3()
        if defensePos3 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Spawn Denided")
        else:
            spawnAccepted = True
            print("Denfense Spawn Accepted")
def defenseSpawnBondaryCheck4():
    spawnAccepted = False
    while spawnAccepted == False:
        defenseSpawnPlayer4()
        if defensePos4 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Spawn Denided")
        else:
            spawnAccepted = True
            print("Denfense Spawn Accepted")
def defenseSpawnBondaryCheck5():
    spawnAccepted = False
    while spawnAccepted == False:
        defenseSpawnPlayer5()
        if defensePos5 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Spawn Denided")
        else:
            spawnAccepted = True
            print("Denfense Spawn Accepted")
def attackSpawnBondaryCheck1():
    spawnAccepted = False
    while spawnAccepted == False:
        attackSpawnPlayer1()
        if attackPos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Attack Spawn Denided")
        else:
            spawnAccepted = True
            print("Attack Spawn Accepted")
def attackSpawnBondaryCheck2():
    spawnAccepted = False
    while spawnAccepted == False:
        attackSpawnPlayer2()
        if attackPos2 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Attack Spawn Denided")
        else:
            spawnAccepted = True
            print("Attack Spawn Accepted")
def attackSpawnBondaryCheck3():
    spawnAccepted = False
    while spawnAccepted == False:
        attackSpawnPlayer3()
        if attackPos3 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Attack Spawn Denided")
        else:
            spawnAccepted = True
            print("Attack Spawn Accepted")
def attackSpawnBondaryCheck4():
    spawnAccepted = False
    while spawnAccepted == False:
        attackSpawnPlayer4()
        if attackPos4 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Attack Spawn Denided")
        else:
            spawnAccepted = True
            print("Attack Spawn Accepted")
def attackSpawnBondaryCheck5():
    spawnAccepted = False
    while spawnAccepted == False:
        attackSpawnPlayer5()
        if attackPos5 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Attack Spawn Denided")
        else:
            spawnAccepted = True
            print("Attack Spawn Accepted")

print("Printing Attack Positions")
sleep(1)
attackSpawnBondaryCheck1()
sleep(0.5)
attackSpawnBondaryCheck2()
sleep(0.5)
attackSpawnBondaryCheck3()
sleep(0.5)
attackSpawnBondaryCheck4()
sleep(0.5)
attackSpawnBondaryCheck5()
sleep(0.5)
print("Printing Defense Positions")
sleep(1)
defenseSpawnBondaryCheck1()
sleep(0.5)
defenseSpawnBondaryCheck2()
sleep(0.5)
defenseSpawnBondaryCheck3()
sleep(0.5)
defenseSpawnBondaryCheck4()
sleep(0.5)
defenseSpawnBondaryCheck5()
sleep(0.5)
