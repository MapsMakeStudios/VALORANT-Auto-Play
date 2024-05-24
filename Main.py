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
maxChangeX = 50
maxChangeY = 50
minChangeX = 5
minChangeY = 5

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
attackSpawnBondaryCheck1()
attackSpawnBondaryCheck2()
attackSpawnBondaryCheck3()
attackSpawnBondaryCheck4()
attackSpawnBondaryCheck5()
print("Printing Defense Positions")
defenseSpawnBondaryCheck1()
defenseSpawnBondaryCheck2()
defenseSpawnBondaryCheck3()
defenseSpawnBondaryCheck4()
defenseSpawnBondaryCheck5()

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


def attackRound1Player1():
    global attackPos1X
    global attackPos1Y
    attackPos1X = randint(minChangeX, maxChangeX)
    attackPos1Y = randint(minChangeY, maxChangeY)
    global attackPos1
    attackPos1 = str(attackPos1X) + "," + str(attackPos1Y)
def attackRound1Player2():
    global attackPos2X
    global attackPos2Y
    attackPos2X = randint(minChangeX, maxChangeX)
    attackPos2Y = randint(minChangeY, maxChangeY)
    global attackPos2
    attackPos2 = str(attackPos2X) + "," + str(attackPos2Y)
def attackRound1Player3():
    global attackPos3X
    global attackPos3Y
    attackPos3X = randint(minChangeX, maxChangeX)
    attackPos3Y = randint(minChangeY, maxChangeY)
    global attackPos3
    attackPos3 = str(attackPos3X) + "," + str(attackPos3Y)
def attackRound1Player4():
    global attackPos4X
    global attackPos4Y
    attackPos4X = randint(minChangeX, maxChangeX)
    attackPos4Y = randint(minChangeY, maxChangeY)
    global attackPos4
    attackPos4 = str(attackPos4X) + "," + str(attackPos4Y)
def attackRound1Player5():
    global attackPos5X
    global attackPos5Y
    attackPos5X = randint(minChangeX, maxChangeX)
    attackPos5Y = randint(minChangeY, maxChangeY)
    global attackPos5
    attackPos5 = str(attackPos5X) + "," + str(attackPos5Y)
def defenseRound1Player1():
    global defensePos1X
    global defensePos1Y
    attackPos1X = randint(minChangeX, maxChangeX)
    attackPos1Y = randint(minChangeY, maxChangeY)
    global defensePos1
    defensePos1 = str(defensePos1X) + "," + str(defensePos1Y)
def defenseRound1Player2():
    global defensePos2X
    global defensePos2Y
    attackPos2X = randint(minChangeX, maxChangeX)
    attackPos2Y = randint(minChangeY, maxChangeY)
    global defensePos2
    defensePos2 = str(defensePos2X) + "," + str(defensePos2Y)
def defenseRound1Player3():
    global defensePos3X
    global defensePos3Y
    attackPos3X = randint(minChangeX, maxChangeX)
    attackPos3Y = randint(minChangeY, maxChangeY)
    global defensePos3
    defensePos3 = str(defensePos3X) + "," + str(defensePos3Y)
def defenseRound1Player4():
    global defensePos4X
    global defensePos4Y
    attackPos4X = randint(minChangeX, maxChangeX)
    attackPos4Y = randint(minChangeY, maxChangeY)
    global defensePos4
    defensePos4 = str(defensePos4X) + "," + str(defensePos4Y)
def defenseRound1Player5():
    global defensePos5X
    global defensePos5Y
    attackPos5X = randint(minChangeX, maxChangeX)
    attackPos5Y = randint(minChangeY, maxChangeY)
    global defensePos5
    defensePos5 = str(defensePos5X) + "," + str(defensePos5Y)
def playerAttackAttackSideCheck(playerNum):
    global isAttacked, attackPlayer1Dead, attackPlayer2Dead, attackPlayer3Dead, attackPlayer4Dead, attackPlayer5Dead
    global defensePlayer1Dead, defensePlayer2Dead, defensePlayer3Dead, defensePlayer4Dead, defensePlayer5Dead

    isAttacked = False
    winChance = 0
    difference = 0

    differenceCalculationListX = [
        attackPos1X, defensePos1X, attackPos2X, defensePos2X, attackPos3X, defensePos3X,
        attackPos4X, defensePos4X, attackPos5X, defensePos5X
    ]
    differenceCalculationListY = [
        attackPos1Y, defensePos1Y, attackPos2Y, defensePos2Y, attackPos3Y, defensePos3Y,
        attackPos4Y, defensePos4Y, attackPos5Y, defensePos5Y
    ]

    # Debugging prints
    for i in range(len(differenceCalculationListX)):
        print(differenceCalculationListX[i])
    for i in range(len(differenceCalculationListY)):
        print(differenceCalculationListY[i])

    currentAttackPlayerNumPrint = 0

    if playerNum == 1:
        currentAttackPlayerNum = 0
        currentAttackPlayerNumPrint = 1
    elif playerNum == 2:
        currentAttackPlayerNum = 2
        currentAttackPlayerNumPrint = 2
    elif playerNum == 3:
        currentAttackPlayerNum = 4
        currentAttackPlayerNumPrint = 3
    elif playerNum == 4:
        currentAttackPlayerNum = 6
        currentAttackPlayerNumPrint = 4
    elif playerNum == 5:
        currentAttackPlayerNum = 8
        currentAttackPlayerNumPrint = 5

    defensePlayerNum = 1
    defensePlayerNumPrint = 1

    for i in range(0, 10, 2):
        if currentAttackPlayerNum < len(differenceCalculationListX) and defensePlayerNum < len(differenceCalculationListX):
            print(int(currentAttackPlayerNum))
            print(int(defensePlayerNum))
            difference = differenceCalculationListX[currentAttackPlayerNum] - differenceCalculationListX[defensePlayerNum]

            if difference <= 10:
                isAttacked = True
                print(f"Attacker {currentAttackPlayerNumPrint} v Defender {defensePlayerNumPrint}")
                winChance = randint(1, 100)
                if winChance >= 50:
                    globals()[f"attackPlayer{currentAttackPlayerNumPrint}Dead"] = True
                    globals()[f"defensePlayer{defensePlayerNumPrint}Dead"] = False
                    print(f"attack player {currentAttackPlayerNumPrint} dead")
                else:
                    globals()[f"attackPlayer{currentAttackPlayerNumPrint}Dead"] = False
                    globals()[f"defensePlayer{defensePlayerNumPrint}Dead"] = True
                    print(f"defense player {defensePlayerNumPrint} dead")
        defensePlayerNum += 2
        defensePlayerNumPrint += 1

def playerAttackDefenseSideCheck(playerNum):
    global isAttacked, attackPlayer1Dead, attackPlayer2Dead, attackPlayer3Dead, attackPlayer4Dead, attackPlayer5Dead
    global defensePlayer1Dead, defensePlayer2Dead, defensePlayer3Dead, defensePlayer4Dead, defensePlayer5Dead

    isAttacked = False
    winChance = 0
    difference = 0

    differenceCalculationListX = [
        attackPos1X, defensePos1X, attackPos2X, defensePos2X, attackPos3X, defensePos3X,
        attackPos4X, defensePos4X, attackPos5X, defensePos5X
    ]
    differenceCalculationListY = [
        attackPos1Y, defensePos1Y, attackPos2Y, defensePos2Y, attackPos3Y, defensePos3Y,
        attackPos4Y, defensePos4Y, attackPos5Y, defensePos5Y
    ]

    # Debugging prints
    for i in range(len(differenceCalculationListX)):
        print(differenceCalculationListX[i])
    for i in range(len(differenceCalculationListY)):
        print(differenceCalculationListY[i])

    currentDefensePlayerNum = playerNum
    currentDefensePlayerNumPrint = 0

    if currentDefensePlayerNum == 1:
        currentDefensePlayerNum = 1
        currentDefensePlayerNumPrint = 1
    elif currentDefensePlayerNum == 2:
        currentDefensePlayerNum = 3
        currentDefensePlayerNumPrint = 2
    elif currentDefensePlayerNum == 3:
        currentDefensePlayerNum = 5
        currentDefensePlayerNumPrint = 3
    elif currentDefensePlayerNum == 4:
        currentDefensePlayerNum = 7
        currentDefensePlayerNumPrint = 4
    elif currentDefensePlayerNum == 5:
        currentDefensePlayerNum = 9
        currentDefensePlayerNumPrint = 5

    attackPlayerNum = 0
    attackPlayerNumPrint = 1

    for i in range(0, 10, 2):
        if currentDefensePlayerNum < len(differenceCalculationListX) and attackPlayerNum < len(differenceCalculationListX):
            difference = differenceCalculationListX[currentDefensePlayerNum] - differenceCalculationListX[attackPlayerNum]
            if difference <= 10:
                isAttacked = True
                print(f"Defender {currentDefensePlayerNumPrint} v Attacker {attackPlayerNumPrint}")
                winChance = randint(1, 100)
                if winChance >= 50:
                    globals()[f"defensePlayer{currentDefensePlayerNumPrint}Dead"] = True
                    globals()[f"attackPlayer{attackPlayerNumPrint}Dead"] = False
                    print(f"defense player {currentDefensePlayerNumPrint} dead")
                else:
                    globals()[f"defensePlayer{currentDefensePlayerNumPrint}Dead"] = False
                    globals()[f"attackPlayer{attackPlayerNumPrint}Dead"] = True
                    print(f"attack player {attackPlayerNumPrint} dead")
        attackPlayerNum += 2
        attackPlayerNumPrint += 1


def attackRound1BondaryCheck1():
    spawnAccepted = False
    while spawnAccepted == False:
        attackRound1Player1()
        if attackPos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Attack Move Denided")
        else:
            spawnAccepted = True
            print("Attack Move Accepted")
            print("Attack Player 1, X - " + str(attackPos1X) + ", Y - " + str(attackPos1Y))
    playerAttackAttackSideCheck(1)
def attackRound1BondaryCheck2():
    spawnAccepted = False
    while spawnAccepted == False:
        attackRound1Player2()
        if attackPos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Attack Move Denided")
        else:
            spawnAccepted = True
            print("Attack Move Accepted")
            print("Attack Player 2, X - " + str(attackPos2X) + ", Y - " + str(attackPos2Y))
    playerAttackAttackSideCheck(2)
def attackRound1BondaryCheck3():
    spawnAccepted = False
    while spawnAccepted == False:
        attackRound1Player3()
        if attackPos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Attack Move Denided")
        else:
            spawnAccepted = True
            print("Attack Move Accepted")
            print("Attack Player 3, X - " + str(attackPos3X) + ", Y - " + str(attackPos3Y))
    playerAttackAttackSideCheck(3)
def attackRound1BondaryCheck4():
    spawnAccepted = False
    while spawnAccepted == False:
        attackRound1Player4()
        if attackPos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Attack Move Denided")
        else:
            spawnAccepted = True
            print("Attack Move Accepted")
            print("Attack Player 4, X - " + str(attackPos4X) + ", Y - " + str(attackPos4Y))
    playerAttackAttackSideCheck(4)
def attackRound1BondaryCheck5():
    spawnAccepted = False
    while spawnAccepted == False:
        attackRound1Player5()
        if attackPos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Attack Move Denided")
        else:
            spawnAccepted = True
            print("Attack Move Accepted")
            print("Attack Player 5, X - " + str(attackPos5X) + ", Y - " + str(attackPos5Y))
    playerAttackAttackSideCheck(5)
def defenseRoundBondaryCheck1():
    currentNumber = 1
    spawnAccepted = False
    while spawnAccepted == False:
        defenseRound1Player1()
        if defensePos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Move Denided")
        else:
            spawnAccepted = True
            print("Denfense Move Accepted")
            print("Defense Player 1, X - " + str(defensePos1X) + ", Y - " + str(defensePos1Y))
    playerAttackDefenseSideCheck(1)
def defenseRoundBondaryCheck2():
    currentNumber = 1
    spawnAccepted = False
    while spawnAccepted == False:
        defenseRound1Player2()
        if defensePos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Move Denided")
        else:
            spawnAccepted = True
            print("Denfense Move Accepted")
            print("Defense Player 2, X - " + str(defensePos2X) + ", Y - " + str(defensePos2Y))
    playerAttackDefenseSideCheck(2)
def defenseRoundBondaryCheck3():
    currentNumber = 1
    spawnAccepted = False
    while spawnAccepted == False:
        defenseRound1Player3()
        if defensePos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Move Denided")
        else:
            spawnAccepted = True
            print("Denfense Move Accepted")
            print("Defense Player 3, X - " + str(defensePos3X) + ", Y - " + str(defensePos3Y))
    playerAttackDefenseSideCheck(3)
def defenseRoundBondaryCheck4():
    currentNumber = 1
    spawnAccepted = False
    while spawnAccepted == False:
        defenseRound1Player4()
        if defensePos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Move Denided")
        else:
            spawnAccepted = True
            print("Denfense Move Accepted")
            print("Defense Player 4, X - " + str(defensePos4X) + ", Y - " + str(defensePos4Y))
    playerAttackDefenseSideCheck(4)
def defenseRoundBondaryCheck5():
    currentNumber = 1
    spawnAccepted = False
    while spawnAccepted == False:
        defenseRound1Player5()
        if defensePos1 in listOfDenidedSpawns:
            spawnAccepted = False
            print("Denfense Move Denided")
        else:
            spawnAccepted = True
            print("Denfense Move Accepted")
            print("Defense Player 5, X - " + str(defensePos5X) + ", Y - " + str(defensePos5Y))
    playerAttackDefenseSideCheck(5)

print("Printing Attack Moves")
attackRound1BondaryCheck1()
attackRound1BondaryCheck2()
attackRound1BondaryCheck3()
defenseRoundBondaryCheck4()
defenseRoundBondaryCheck5()
print("Printing Defense Moves")
defenseRoundBondaryCheck1()
defenseRoundBondaryCheck2()
defenseRoundBondaryCheck3()
defenseRoundBondaryCheck4()
defenseRoundBondaryCheck5()

round1Layout = (

    {
        "team": "Attack",
        "playerNum": "1",
        "posX": attackPos1X,
        "posY": attackPos1Y,
        "Dead": attackPlayer1Dead,
    },
    {
    "team": "Attack",
    "playerNum": "2",
    "posX": attackPos2X,
    "posY": attackPos2Y,
    "Dead": attackPlayer2Dead,
    },
    {
    "team": "Attack",
    "playerNum": "3",
    "posX": attackPos3X,
    "posY": attackPos3Y,
    "Dead": attackPlayer3Dead,
    },
    {
    "team": "Attack",
    "playerNum": "4",
    "posX": attackPos4X,
    "posY": attackPos4Y,
    "Dead": attackPlayer4Dead,
    },
    {
    "team": "Attack",
    "playerNum": "5",
    "posX": attackPos5X,
    "posY": attackPos5Y,
    "Dead": attackPlayer5Dead,
    },
    {
    "team": "Defense",
    "playerNum": "1",
    "posX": defensePos1X,
    "posY": defensePos1Y,
    "Dead": defensePlayer1Dead,
    },
    {
    "team": "Defense",
    "playerNum": "2",
    "posX": defensePos2X,
    "posY": defensePos2Y,
    "Dead": defensePlayer2Dead,
    },
    {
    "team": "Defense",
    "playerNum": "3",
    "posX": defensePos3X,
    "posY": defensePos3Y,
    "Dead": defensePlayer3Dead,
    },
    {
    "team": "Defense",
    "playerNum": "4",
    "posX": defensePos4X,
    "posY": defensePos4Y,
    "Dead": defensePlayer4Dead,
    },
    {
    "team": "Defense",
    "playerNum": "5",
    "posX": defensePos5X,
    "posY": defensePos5Y,
    "Dead": defensePlayer5Dead,
    }
)

with open("round1Phase.json", "w") as f:
    json.dump(round1Layout, f, indent=4)