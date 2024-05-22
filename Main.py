from random import randint
from time import sleep
import json
import os

gridSizeX = 100
gridSizeY = 100

listOfDenidedSpawns = ["1,1","1,1"]
valueDenidedX = 2
valueDenidedY = 1

currentNumber = 1
attackSpawnRadiusMaxX = 100
attackSpawnRadiusMaxY = 100
attackSpawnRadiusMinX = 1
attackSpawnRadiusMinY = 72
defenseSpawnRadiusMaxX = 100
defenseSpawnRadiusMaxY = 40
defenseSpawnRadiusMinX = 1
defenseSpawnRadiusMinY = 1

#For Test Push

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
valueDenidedY = 13
for i in range(10):
    valueDenidedX = 1
    for i in range(44):
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1
valueDenidedY = 13
for i in range(8):
    valueDenidedX = 73
    for i in range(27):
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1
valueDenidedY = 24
for i in range(7):
    valueDenidedX = 2
    for i in range(29):
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1


print(listOfDenidedSpawns)
def attackSpawnPlayer1():
    global attackPos1X
    global attackPos1Y
    attackPos1X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos1Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    global attackPos1
    attackPos1 = str(attackPos1X) + "," + str(attackPos1Y)
def attackSpawnPlayer2():
    global attackPos2X
    global attackPos2Y
    attackPos2X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos2Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    global attackPos2
    attackPos2 = str(attackPos2X) + "," + str(attackPos2Y)
def attackSpawnPlayer3():
    global attackPos3X
    global attackPos3Y
    attackPos3X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos3Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    global attackPos3
    attackPos3 = str(attackPos3X) + "," + str(attackPos3Y)
def attackSpawnPlayer4():
    global attackPos4X
    global attackPos4Y
    attackPos4X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos4Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    global attackPos4
    attackPos4 = str(attackPos4X) + "," + str(attackPos4Y)
def attackSpawnPlayer5():
    global attackPos5X
    global attackPos5Y
    attackPos5X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackPos5Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    global attackPos5
    attackPos5 = str(attackPos5X) + "," + str(attackPos5Y)
def defenseSpawnPlayer1():
    global defensePos1X
    global defensePos1Y
    defensePos1X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos1Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    global defensePos1
    defensePos1 = str(defensePos1X) + "," + str(defensePos1Y)

def defenseSpawnPlayer2():
    global defensePos2X
    global defensePos2Y
    defensePos2X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos2Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    global defensePos2
    defensePos2 = str(defensePos2X) + "," + str(defensePos2Y)
def defenseSpawnPlayer3():
    global defensePos3X
    global defensePos3Y
    defensePos3X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos3Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    global defensePos3
    defensePos3 = str(defensePos3X) + "," + str(defensePos3Y)
def defenseSpawnPlayer4():
    global defensePos4X
    global defensePos4Y
    defensePos4X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos4Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    global defensePos4
    defensePos4 = str(defensePos4X) + "," + str(defensePos4Y)
def defenseSpawnPlayer5():
    global defensePos5X
    global defensePos5Y
    defensePos5X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defensePos5Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    global defensePos5
    defensePos5 = str(defensePos5X) + "," + str(defensePos5Y)

def defenseSpawnBondaryCheck1():
    currentNumber = 1
    spawnAccepted = False
    while spawnAccepted == False:
        defenseSpawnPlayer1()
        if defensePos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Spawn Denided")
        else:
            spawnAccepted = True
            print("Denfense Spawn Accepted")
            print("Defense Player 1, X - " + str(defensePos1X) + ", Y - " + str(defensePos1Y))

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
            print("Defense Player 2, X - " + str(defensePos2X) + ", Y - " + str(defensePos2Y))
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
            print("Defense Player 3, X - " + str(defensePos3X) + ", Y - " + str(defensePos3Y))
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
            print("Defense Player 4, X - " + str(defensePos4X) + ", Y - " + str(defensePos4Y))
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
            print("Defense Player 5, X - " + str(defensePos5X) + ", Y - " + str(defensePos5Y))
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
            print("Attack Player 1, X - " + str(attackPos1X) + ", Y - " + str(attackPos1Y))
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
            print("Attack Player 2, X - " + str(attackPos2X) + ", Y - " + str(attackPos2Y))
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
            print("Attack Player 3, X - " + str(attackPos3X) + ", Y - " + str(attackPos3Y))
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
            print("Attack Player 4, X - " + str(attackPos4X) + ", Y - " + str(attackPos4Y))
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
            print("Attack Player 5, X - " + str(attackPos5X) + ", Y - " + str(attackPos5Y))

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

spawnPhaseLayout = (

    {
        "team": "Attack",
        "playerNum": "1",
        "posX": attackPos1X,
        "posY": defensePos1Y,
    },
    {
        "team": "Attack",
        "playerNum": "2",
        "posX": attackPos2X,
        "posY": defensePos2Y,
    },
    {
        "team": "Attack",
        "playerNum": "3",
        "posX": attackPos3X,
        "posY": defensePos3Y,
    },
    {
        "team": "Attack",
        "playerNum": "4",
        "posX": attackPos4X,
        "posY": defensePos4Y,
    },
    {
        "team": "Attack",
        "playerNum": "5",
        "posX": attackPos5X,
        "posY": defensePos5Y,
    },
    {
        "team": "Defense",
        "playerNum": "1",
        "posX": defensePos1X,
        "posY": defensePos1Y,
    },
    {
        "team": "Defense",
        "playerNum": "2",
        "posX": defensePos2X,
        "posY": defensePos2Y,
    },
    {
        "team": "Defense",
        "playerNum": "3",
        "posX": defensePos3X,
        "posY": defensePos3Y,
    },
    {
        "team": "Defense",
        "playerNum": "4",
        "posX": defensePos4X,
        "posY": defensePos1Y,
    },
    {
        "team": "Defense",
        "playerNum": "5",
        "posX": defensePos5X,
        "posY": defensePos5Y,
    },

)

with open("spawnPhaseExample.json", "w") as f:
    json.dump(spawnPhaseLayout, f, indent=4)
