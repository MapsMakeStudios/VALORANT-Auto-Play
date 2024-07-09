from random import randint
from time import sleep
import json
import os
import csv

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
defensePlayer1Dead = False
defensePlayer2Dead = False
defensePlayer3Dead = False
defensePlayer4Dead = False
defensePlayer5Dead = False
attackPlayer1Dead = False
attackPlayer2Dead = False
attackPlayer3Dead = False
attackPlayer4Dead = False
attackPlayer5Dead = False
defenseTeamDead = False
attackTeamDead = False
defensePlayer1DeadTo = "Alive"
defensePlayer2DeadTo = "Alive"
defensePlayer3DeadTo = "Alive"
defensePlayer4DeadTo = "Alive"
defensePlayer5DeadTo = "Alive"
attackPlayer1DeadTo = "Alive"
attackPlayer2DeadTo = "Alive"
attackPlayer3DeadTo = "Alive"
attackPlayer4DeadTo = "Alive"
attackPlayer5DeadTo = "Alive"
attackStep1Pos1X = 0
attackStep1Pos1Y = 0
attackStep1Pos2X = 0
attackStep1Pos2Y = 0
attackStep1Pos3X = 0
attackStep1Pos3Y = 0
attackStep1Pos4X = 0
attackStep1Pos4Y = 0
attackStep1Pos5X = 0
attackStep1Pos5Y = 0
defenseStep1Pos1X = 0
defenseStep1Pos1Y = 0
defenseStep1Pos2X = 0
defenseStep1Pos2Y = 0
defenseStep1Pos3X = 0
defenseStep1Pos3Y = 0
defenseStep1Pos4X = 0
defenseStep1Pos4Y = 0
defenseStep1Pos5X = 0
defenseStep1Pos5Y = 0
#For Test Push

for i in range(12):
    valueDenidedX = 1
    for i in range(100):
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1
valueDenidedY = 22
for i in range(12): #X
    valueDenidedX = 52
    for i in range(4): #Y
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
valueDenidedY = 90
for i in range(10):
    valueDenidedX = 1
    for i in range(100):
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1
valueDenidedY = 85
for i in range(4): #Y
    valueDenidedX = 1
    for i in range(46): #X
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1
valueDenidedY = 79
for i in range(10): #Y
    valueDenidedX = 62
    for i in range(40): #X
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1
valueDenidedY = 31
for i in range(13): #Y
    valueDenidedX = 62
    for i in range(8): #X
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1
valueDenidedY = 1
for i in range(100): #Y
    valueDenidedX = 93
    for i in range(7): #X
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1
valueDenidedY = 37
for i in range(8): #Y
    valueDenidedX = 1
    for i in range(11): #X
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1
valueDenidedY = 37
for i in range(7): #Y
    valueDenidedX = 22
    for i in range(8): #X
        listOfDenidedSpawns += [str(valueDenidedX) + "," + str(valueDenidedY)]
        valueDenidedX += 1
    valueDenidedY += 1




print(listOfDenidedSpawns)
def attackSpawnPlayer1():
    global attackSpawnPos1X
    global attackSpawnPos1Y
    attackSpawnPos1X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackSpawnPos1Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    global attackPos1
    attackPos1 = str(attackSpawnPos1X) + "," + str(attackSpawnPos1Y)
def attackSpawnPlayer2():
    global attackSpawnPos2X
    global attackSpawnPos2Y
    attackSpawnPos2X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackSpawnPos2Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    global attackPos2
    attackPos2 = str(attackSpawnPos2X) + "," + str(attackSpawnPos2Y)
def attackSpawnPlayer3():
    global attackSpawnPos3X
    global attackSpawnPos3Y
    attackSpawnPos3X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackSpawnPos3Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    global attackPos3
    attackPos3 = str(attackSpawnPos3X) + "," + str(attackSpawnPos3Y)
def attackSpawnPlayer4():
    global attackSpawnPos4X
    global attackSpawnPos4Y
    attackSpawnPos4X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackSpawnPos4Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    global attackPos4
    attackPos4 = str(attackSpawnPos4X) + "," + str(attackSpawnPos4Y)
def attackSpawnPlayer5():
    global attackSpawnPos5X
    global attackSpawnPos5Y
    attackSpawnPos5X = randint(attackSpawnRadiusMinX, attackSpawnRadiusMaxX)
    attackSpawnPos5Y = randint(attackSpawnRadiusMinY, attackSpawnRadiusMaxY)
    global attackPos5
    attackPos5 = str(attackSpawnPos5X) + "," + str(attackSpawnPos5Y)
def defenseSpawnPlayer1():
    global defenseSpawnPos1X
    global defenseSpawnPos1Y
    defenseSpawnPos1X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defenseSpawnPos1Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    global defensePos1
    defensePos1 = str(defenseSpawnPos1X) + "," + str(defenseSpawnPos1Y)

def defenseSpawnPlayer2():
    global defenseSpawnPos2X
    global defenseSpawnPos2Y
    defenseSpawnPos2X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defenseSpawnPos2Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    global defensePos2
    defensePos2 = str(defenseSpawnPos2X) + "," + str(defenseSpawnPos2Y)
def defenseSpawnPlayer3():
    global defenseSpawnPos3X
    global defenseSpawnPos3Y
    defenseSpawnPos3X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defenseSpawnPos3Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    global defensePos3
    defensePos3 = str(defenseSpawnPos3X) + "," + str(defenseSpawnPos3Y)
def defenseSpawnPlayer4():
    global defenseSpawnPos4X
    global defenseSpawnPos4Y
    defenseSpawnPos4X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defenseSpawnPos4Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    global defensePos4
    defensePos4 = str(defenseSpawnPos4X) + "," + str(defenseSpawnPos4Y)
def defenseSpawnPlayer5():
    global defenseSpawnPos5X
    global defenseSpawnPos5Y
    defenseSpawnPos5X = randint(defenseSpawnRadiusMinX, defenseSpawnRadiusMaxX)
    defenseSpawnPos5Y = randint(defenseSpawnRadiusMinY, defenseSpawnRadiusMaxY)
    global defensePos5
    defensePos5 = str(defenseSpawnPos5X) + "," + str(defenseSpawnPos5Y)

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
            print("Defense Player 1, X - " + str(defenseSpawnPos1X) + ", Y - " + str(defenseSpawnPos1Y))

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
            print("Defense Player 2, X - " + str(defenseSpawnPos2X) + ", Y - " + str(defenseSpawnPos2Y))
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
            print("Defense Player 3, X - " + str(defenseSpawnPos3X) + ", Y - " + str(defenseSpawnPos3Y))
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
            print("Defense Player 4, X - " + str(defenseSpawnPos4X) + ", Y - " + str(defenseSpawnPos4Y))
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
            print("Defense Player 5, X - " + str(defenseSpawnPos5X) + ", Y - " + str(defenseSpawnPos5Y))
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
            print("Attack Player 1, X - " + str(attackSpawnPos1X) + ", Y - " + str(attackSpawnPos1Y))
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
            print("Attack Player 2, X - " + str(attackSpawnPos2X) + ", Y - " + str(attackSpawnPos2Y))
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
            print("Attack Player 3, X - " + str(attackSpawnPos3X) + ", Y - " + str(attackSpawnPos3Y))
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
            print("Attack Player 4, X - " + str(attackSpawnPos4X) + ", Y - " + str(attackSpawnPos4Y))
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
            print("Attack Player 5, X - " + str(attackSpawnPos5X) + ", Y - " + str(attackSpawnPos5Y))


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


def attackStep1Player1():
    global attackStep1Pos1X
    global attackStep1Pos1Y
    attackStep1Pos1X = randint(minChangeX, maxChangeX)
    attackStep1Pos1Y = randint(minChangeY, maxChangeY)
    global attackPos1
    attackPos1 = str(attackStep1Pos1X) + "," + str(attackStep1Pos1Y)
def attackStep1Player2():
    global attackStep1Pos2X
    global attackStep1Pos2Y
    attackStep1Pos2X = randint(minChangeX, maxChangeX)
    attackStep1Pos2Y = randint(minChangeY, maxChangeY)
    global attackPos2
    attackPos2 = str(attackStep1Pos2X) + "," + str(attackStep1Pos2Y)
def attackStep1Player3():
    global attackStep1Pos3X
    global attackStep1Pos3Y
    attackStep1Pos3X = randint(minChangeX, maxChangeX)
    attackStep1Pos3Y = randint(minChangeY, maxChangeY)
    global attackPos3
    attackPos3 = str(attackStep1Pos3X) + "," + str(attackStep1Pos3Y)
def attackStep1Player4():
    global attackStep1Pos4X
    global attackStep1Pos4Y
    attackStep1Pos4X = randint(minChangeX, maxChangeX)
    attackStep1Pos4Y = randint(minChangeY, maxChangeY)
    global attackPos4
    attackPos4 = str(attackStep1Pos4X) + "," + str(attackStep1Pos4Y)
def attackStep1Player5():
    global attackStep1Pos5X
    global attackStep1Pos5Y
    attackStep1Pos5X = randint(minChangeX, maxChangeX)
    attackStep1Pos5Y = randint(minChangeY, maxChangeY)
    global attackPos5
    attackPos5 = str(attackStep1Pos5X) + "," + str(attackStep1Pos5Y)
def defenseStep1Player1():
    global defenseStep1Pos1X
    global defenseStep1Pos1Y
    defenseStep1Pos1X = randint(minChangeX, maxChangeX)
    defenseStep1Pos1Y = randint(minChangeY, maxChangeY)
    global defenseStep1Pos1
    defenseStep1Pos1 = str(defenseStep1Pos1X) + "," + str(defenseStep1Pos1Y)
def defenseStep1Player2():
    global defenseStep1Pos2X
    global defenseStep1Pos2Y
    defenseStep1Pos2X = randint(minChangeX, maxChangeX)
    defenseStep1Pos2Y = randint(minChangeY, maxChangeY)
    global defenseStep1Pos2
    defenseStep1Pos2 = str(defenseStep1Pos2X) + "," + str(defenseStep1Pos2Y)
def defenseStep1Player3():
    global defenseStep1Pos3X
    global defenseStep1Pos3Y
    defenseStep1Pos3X = randint(minChangeX, maxChangeX)
    defenseStep1Pos3Y = randint(minChangeY, maxChangeY)
    global defenseStep1Pos3
    defenseStep1Pos3 = str(defenseStep1Pos3X) + "," + str(defenseStep1Pos3Y)
def defenseStep1Player4():
    global defenseStep1Pos4X
    global defenseStep1Pos4Y
    defenseStep1Pos4X = randint(minChangeX, maxChangeX)
    defenseStep1Pos4Y = randint(minChangeY, maxChangeY)
    global defenseStep1Pos4
    defenseStep1Pos4 = str(defenseStep1Pos4X) + "," + str(defenseStep1Pos4Y)
def defenseStep1Player5():
    global defenseStep1Pos5X
    global defenseStep1Pos5Y
    defenseStep1Pos5X = randint(minChangeX, maxChangeX)
    defenseStep1Pos5Y = randint(minChangeY, maxChangeY)
    global defenseStep1Pos5
    defenseStep1Pos5 = str(defenseStep1Pos5X) + "," + str(defenseStep1Pos5Y)


def playerAttackAttackSideCheck1(playerNum):
    global isAttacked, attackPlayer1Dead, attackPlayer2Dead, attackPlayer3Dead, attackPlayer4Dead, attackPlayer5Dead
    global defensePlayer1Dead, defensePlayer2Dead, defensePlayer3Dead, defensePlayer4Dead, defensePlayer5Dead
    global attackPlayer1Dead, attackPlayer2Dead, attackPlayer3Dead, attackPlayer4Dead, attackPlayer5Dead

    isAttacked = False
    winChance = 0
    difference = 0

    differenceCalculationListX = [
        attackStep1Pos1X, defenseStep1Pos1X, attackStep1Pos2X, defenseStep1Pos2X, attackStep1Pos3X, defenseStep1Pos3X,
        attackStep1Pos4X, defenseStep1Pos4X, attackStep1Pos5X, defenseStep1Pos5X
    ]
    differenceCalculationListY = [
        attackStep1Pos1Y, defenseStep1Pos1Y, attackStep1Pos2Y, defenseStep1Pos2Y, attackStep1Pos3Y, defenseStep1Pos3Y,
        attackStep1Pos4Y, defenseStep1Pos4Y, attackStep1Pos5Y, defenseStep1Pos5Y
    ]
    deathCheckListDefense = [defensePlayer1Dead, defensePlayer2Dead, defensePlayer3Dead, defensePlayer4Dead,
                             defensePlayer5Dead]
    deathCheckListAttack = [attackPlayer1Dead, attackPlayer2Dead, attackPlayer3Dead, attackPlayer4Dead,
                            attackPlayer5Dead]
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
        if currentAttackPlayerNum < len(differenceCalculationListX) and defensePlayerNum < len(
                differenceCalculationListX):
            difference = differenceCalculationListX[currentAttackPlayerNum] - differenceCalculationListX[
                defensePlayerNum]

            if playerNum - 1 < len(deathCheckListAttack) and deathCheckListAttack[playerNum - 1]:
                print("Player dead not checking for attacker's death")
            if defensePlayerNumPrint - 1 < len(deathCheckListDefense) and deathCheckListDefense[
                defensePlayerNumPrint - 1]:
                print("Player dead not checking for defender's death")
            else:
                if difference <= 10:
                    isAttacked = True
                    print(f"Attacker {currentAttackPlayerNumPrint} v Defender {defensePlayerNumPrint}")
                    winChance = randint(1, 100)
                    if winChance >= 50:
                        globals()[f"attackPlayer{currentAttackPlayerNumPrint}Dead"] = True
                        globals()[f"defensePlayer{defensePlayerNumPrint}Dead"] = False
                        print(f"Attack player {currentAttackPlayerNumPrint} dead")
                        globals()[f"attackPlayer{currentAttackPlayerNumPrint}DeadTo"] = str("Defender " + str(defensePlayerNumPrint))
                    else:
                        globals()[f"attackPlayer{currentAttackPlayerNumPrint}Dead"] = False
                        globals()[f"defensePlayer{defensePlayerNumPrint}Dead"] = True
                        print(f"Defense player {defensePlayerNumPrint} dead")
                        globals()[f"defensePlayer{defensePlayerNumPrint}DeadTo"] = str("Attacker " + str(currentAttackPlayerNumPrint))
            defensePlayerNum += 2
            defensePlayerNumPrint += 1


def playerAttackDefenseSideCheck1(playerNum):
    global isAttacked, attackPlayer1Dead, attackPlayer2Dead, attackPlayer3Dead, attackPlayer4Dead, attackPlayer5Dead
    global defensePlayer1Dead, defensePlayer2Dead, defensePlayer3Dead, defensePlayer4Dead, defensePlayer5Dead
    global attackPlayer1Dead, attackPlayer2Dead, attackPlayer3Dead, attackPlayer4Dead, attackPlayer5Dead
    isAttacked = False
    winChance = 0
    difference = 0

    differenceCalculationListX = [
        attackStep1Pos1X, defenseStep1Pos1X, attackStep1Pos2X, defenseStep1Pos2X, attackStep1Pos3X, defenseStep1Pos3X,
        attackStep1Pos4X, defenseStep1Pos4X, attackStep1Pos5X, defenseStep1Pos5X
    ]
    differenceCalculationListY = [
        attackStep1Pos1Y, defenseStep1Pos1Y, attackStep1Pos2Y, defenseStep1Pos2Y, attackStep1Pos3Y, defenseStep1Pos3Y,
        attackStep1Pos4Y, defenseStep1Pos4Y, attackStep1Pos5Y, defenseStep1Pos5Y
    ]
    deathCheckListDefense = [defensePlayer1Dead, defensePlayer2Dead, defensePlayer3Dead, defensePlayer4Dead,
                             defensePlayer5Dead]
    deathCheckListAttack = [attackPlayer1Dead, attackPlayer2Dead, attackPlayer3Dead, attackPlayer4Dead,
                            attackPlayer5Dead]
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
        if currentDefensePlayerNum < len(differenceCalculationListX) and attackPlayerNum < len(
                differenceCalculationListX):
            difference = differenceCalculationListX[currentDefensePlayerNum] - differenceCalculationListX[
                attackPlayerNum]

            if playerNum - 1 < len(deathCheckListAttack) and deathCheckListAttack[playerNum - 1]:
                print("Player dead not checking for attacker's death")
            if currentDefensePlayerNumPrint - 1 < len(deathCheckListDefense) and deathCheckListDefense[
                currentDefensePlayerNumPrint - 1]:
                print("Player dead not checking for defender's death")
            else:
                if difference <= 10:
                    isAttacked = True
                    print(f"Defender {currentDefensePlayerNumPrint} v Attacker {attackPlayerNumPrint}")
                    winChance = randint(1, 100)
                    if winChance >= 50:
                        globals()[f"defensePlayer{currentDefensePlayerNumPrint}Dead"] = True
                        globals()[f"attackPlayer{attackPlayerNumPrint}Dead"] = False
                        print(f"Defense player {currentDefensePlayerNumPrint} dead")
                        globals()[f"attackPlayer{attackPlayerNumPrint}DeadTo"] = str("Defender " + str(currentDefensePlayerNumPrint))
                    else:
                        globals()[f"defensePlayer{currentDefensePlayerNumPrint}Dead"] = False
                        globals()[f"attackPlayer{attackPlayerNumPrint}Dead"] = True
                        print(f"Attack player {attackPlayerNumPrint} dead")
                        globals()[f"defensePlayer{currentDefensePlayerNumPrint}DeadTo"] = str("Attacker " + str(attackPlayerNumPrint))
            attackPlayerNum += 2
            attackPlayerNumPrint += 1


def attackStep1BondaryCheck1():
    spawnAccepted = False
    if attackPlayer1Dead == True:
        print("Player 1 Dead Not Moving")
    else:
        while spawnAccepted == False:
            attackStep1Player1()
            if attackPos1 in listOfDenidedSpawns:
                spawnAccepted = False
                print("Attack Move Denided")
            else:
                spawnAccepted = True
                print("Attack Move Accepted")
                print("Attack Player 1, X - " + str(attackStep1Pos1X) + ", Y - " + str(attackStep1Pos1Y))
        playerAttackAttackSideCheck1(1)
def attackStep1BondaryCheck2():
    spawnAccepted = False
    if attackPlayer2Dead == True:
        print("Player 2 Dead Not Moving")
    else:
        while spawnAccepted == False:
            attackStep1Player2()
            if attackPos1 in listOfDenidedSpawns:
                spawnAccepted = False
                print("Attack Move Denided")
            else:
                spawnAccepted = True
                print("Attack Move Accepted")
                print("Attack Player 2, X - " + str(attackStep1Pos2X) + ", Y - " + str(attackStep1Pos2Y))
        playerAttackAttackSideCheck1(2)
def attackStep1BondaryCheck3():
    spawnAccepted = False
    if attackPlayer3Dead == True:
        print("Player 3 Dead Not Moving")
    else:
        while spawnAccepted == False:
            attackStep1Player3()
            if attackPos1 in listOfDenidedSpawns:
                spawnAccepted = False
                print("Attack Move Denided")
            else:
                spawnAccepted = True
                print("Attack Move Accepted")
                print("Attack Player 3, X - " + str(attackStep1Pos3X) + ", Y - " + str(attackStep1Pos3Y))
        playerAttackAttackSideCheck1(3)
def attackStep1BondaryCheck4():
    spawnAccepted = False
    if attackPlayer4Dead == True:
        print("Player 4 Dead Not Moving")
    else:
        while spawnAccepted == False:
            attackStep1Player4()
            if attackPos1 in listOfDenidedSpawns:
                spawnAccepted = False
                print("Attack Move Denided")
            else:
                spawnAccepted = True
                print("Attack Move Accepted")
                print("Attack Player 4, X - " + str(attackStep1Pos4X) + ", Y - " + str(attackStep1Pos4Y))
        playerAttackAttackSideCheck1(4)
def attackStep1BondaryCheck5():
    spawnAccepted = False
    if attackPlayer5Dead == True:
        print("Player 5 Dead Not Moving")
    else:
        while spawnAccepted == False:
            attackStep1Player5()
            if attackPos1 in listOfDenidedSpawns:
                spawnAccepted = False
                print("Attack Move Denided")
            else:
                spawnAccepted = True
                print("Attack Move Accepted")
                print("Attack Player 5, X - " + str(attackStep1Pos5X) + ", Y - " + str(attackStep1Pos5Y))
        playerAttackAttackSideCheck1(5)
def defenseStep1BondaryCheck1():
    currentNumber = 1
    spawnAccepted = False
    if defensePlayer5Dead == True:
        print("Player 5 Dead Not Moving")
    else:
        while spawnAccepted == False:
            defenseStep1Player1()
            if defensePos1 in listOfDenidedSpawns:
                spawnAccepted = False
                print("Denfense Move Denided")
            else:
                spawnAccepted = True
                print("Denfense Move Accepted")
                print("Defense Player 1, X - " + str(defenseStep1Pos1X) + ", Y - " + str(defenseStep1Pos1Y))
        playerAttackDefenseSideCheck1(1)
def defenseStep1BondaryCheck2():
    currentNumber = 1
    spawnAccepted = False
    if defensePlayer5Dead == True:
        print("Player 5 Dead Not Moving")
    else:
        while spawnAccepted == False:
            defenseStep1Player2()
            if defensePos1 in listOfDenidedSpawns:
                spawnAccepted = False
                print("Denfense Move Denided")
            else:
                spawnAccepted = True
                print("Denfense Move Accepted")
                print("Defense Player 2, X - " + str(defenseStep1Pos2X) + ", Y - " + str(defenseStep1Pos2Y))
        playerAttackDefenseSideCheck1(2)
def defenseStep1BondaryCheck3():
    currentNumber = 1
    spawnAccepted = False
    if defensePlayer3Dead == True:
        print("Player 3 Dead Not Moving")
    else:
        while spawnAccepted == False:
            defenseStep1Player3()
            if defensePos1 in listOfDenidedSpawns:
                spawnAccepted = False
                print("Denfense Move Denided")
            else:
                spawnAccepted = True
                print("Denfense Move Accepted")
                print("Defense Player 3, X - " + str(defenseStep1Pos3X) + ", Y - " + str(defenseStep1Pos3Y))
        playerAttackDefenseSideCheck1(3)
def defenseStep1BondaryCheck4():
    currentNumber = 1
    spawnAccepted = False
    if defensePlayer4Dead == True:
        print("Player 4 Dead Not Moving")
    else:
        while spawnAccepted == False:
            defenseStep1Player4()
            if defensePos1 in listOfDenidedSpawns:
                spawnAccepted = False
                print("Denfense Move Denided")
            else:
                spawnAccepted = True
                print("Denfense Move Accepted")
                print("Defense Player 4, X - " + str(defenseStep1Pos4X) + ", Y - " + str(defenseStep1Pos4Y))
        playerAttackDefenseSideCheck1(4)
def defenseStep1BondaryCheck5():
    currentNumber = 1
    spawnAccepted = False
    if defensePlayer5Dead == True:
        print("Player 5 Dead Not Moving")
    else:
        while spawnAccepted == False:
            defenseStep1Player5()
            if defensePos1 in listOfDenidedSpawns:
                spawnAccepted = False
                print("Denfense Move Denided")
            else:
                spawnAccepted = True
                print("Denfense Move Accepted")
                print("Defense Player 5, X - " + str(defenseStep1Pos5X) + ", Y - " + str(defenseStep1Pos5Y))
        playerAttackDefenseSideCheck1(5)
def teamDefensesideCheck():

    if defensePlayer1Dead and defensePlayer2Dead and defensePlayer3Dead and defensePlayer4Dead and defensePlayer5Dead == True:
        print("Team Dead")
        defenseTeamDead = True
    else:
        defenseTeamDead = False
def teamAttacksideCheck():

    if attackPlayer1Dead and attackPlayer2Dead and attackPlayer3Dead and attackPlayer4Dead and attackPlayer5Dead == True:
        print("Team Dead")
        attackTeamDead = True
    else:
        attackTeamDead = False



print("Printing Attack Moves")
attackStep1BondaryCheck1()
attackStep1BondaryCheck2()
attackStep1BondaryCheck3()
attackStep1BondaryCheck4()
attackStep1BondaryCheck5()
teamAttacksideCheck()
print("Printing Defense Moves")
defenseStep1BondaryCheck1()
defenseStep1BondaryCheck2()
defenseStep1BondaryCheck3()
defenseStep1BondaryCheck4()
defenseStep1BondaryCheck5()
teamDefensesideCheck()

spawnPhaseLayout = (

    {
        "team": "Attack",
        "playerNum": "1",
        "posX": attackSpawnPos1X,
        "posY": attackSpawnPos1Y,
    },
    {
        "team": "Attack",
        "playerNum": "2",
        "posX": attackSpawnPos2X,
        "posY": attackSpawnPos2Y,
    },
    {
        "team": "Attack",
        "playerNum": "3",
        "posX": attackSpawnPos3X,
        "posY": attackSpawnPos3Y,
    },
    {
        "team": "Attack",
        "playerNum": "4",
        "posX": attackSpawnPos4X,
        "posY": attackSpawnPos4Y,
    },
    {
        "team": "Attack",
        "playerNum": "5",
        "posX": attackSpawnPos5X,
        "posY": attackSpawnPos5Y,
    },
    {
        "team": "Defense",
        "playerNum": "1",
        "posX": defenseSpawnPos1X,
        "posY": defenseSpawnPos1Y,
    },
    {
        "team": "Defense",
        "playerNum": "2",
        "posX": defenseSpawnPos2X,
        "posY": defenseSpawnPos2Y,
    },
    {
        "team": "Defense",
        "playerNum": "3",
        "posX": defenseSpawnPos3X,
        "posY": defenseSpawnPos3Y,
    },
    {
        "team": "Defense",
        "playerNum": "4",
        "posX": defenseSpawnPos4X,
        "posY": defenseSpawnPos4Y,
    },
    {
        "team": "Defense",
        "playerNum": "5",
        "posX": defenseSpawnPos5X,
        "posY": defenseSpawnPos5Y,
    },

)

with open("spawnPhase.json", "w") as f:
    json.dump(spawnPhaseLayout, f, indent=4)


round1Layout = (

    {
        "team": "Attack",
        "playerNum": "1",
        "posX": attackStep1Pos1X,
        "posY": attackStep1Pos1Y,
        "Dead": attackPlayer1Dead,
        "DeadTo": attackPlayer1DeadTo,
    },
    {
    "team": "Attack",
    "playerNum": "2",
    "posX": attackStep1Pos2X,
    "posY": attackStep1Pos2Y,
    "Dead": attackPlayer2Dead,
    "DeadTo": attackPlayer2DeadTo,
    },
    {
    "team": "Attack",
    "playerNum": "3",
    "posX": attackStep1Pos3X,
    "posY": attackStep1Pos3Y,
    "Dead": attackPlayer3Dead,
    "DeadTo": attackPlayer3DeadTo,
    },
    {
    "team": "Attack",
    "playerNum": "4",
    "posX": attackStep1Pos4X,
    "posY": attackStep1Pos4Y,
    "Dead": attackPlayer4Dead,
    "DeadTo": attackPlayer4DeadTo,
    },
    {
    "team": "Attack",
    "playerNum": "5",
    "posX": attackStep1Pos5X,
    "posY": attackStep1Pos5Y,
    "Dead": attackPlayer5Dead,
    "DeadTo": attackPlayer5DeadTo,
    },
    {
    "team": "Defense",
    "playerNum": "1",
    "posX": defenseStep1Pos1X,
    "posY": defenseStep1Pos1Y,
    "Dead": defensePlayer1Dead,
    "DeadTo": defensePlayer1DeadTo,
    },
    {
    "team": "Defense",
    "playerNum": "2",
    "posX": defenseStep1Pos2X,
    "posY": defenseStep1Pos2Y,
    "Dead": defensePlayer2Dead,
    "DeadTo": defensePlayer2DeadTo,
    },
    {
    "team": "Defense",
    "playerNum": "3",
    "posX": defenseStep1Pos3X,
    "posY": defenseStep1Pos3Y,
    "Dead": defensePlayer3Dead,
    "DeadTo": defensePlayer3DeadTo,
    },
    {
    "team": "Defense",
    "playerNum": "4",
    "posX": defenseStep1Pos4X,
    "posY": defenseStep1Pos4Y,
    "Dead": defensePlayer4Dead,
    "DeadTo": defensePlayer4DeadTo,
    },
    {
    "team": "Defense",
    "playerNum": "5",
    "posX": defenseStep1Pos5X,
    "posY": defenseStep1Pos5Y,
    "Dead": defensePlayer5Dead,
    "DeadTo": defensePlayer5DeadTo,
    },
    {
    "team": "Defense",
    "Dead": defenseTeamDead,
    },
    {
    "team": "Attack",
    "Dead": attackTeamDead,
    }
)

with open("round1Phase.json", "w") as f:
    json.dump(round1Layout, f, indent=4)
print("json file created")
print("json file created")

print("1.1 genorating")
#if attackTeamDead == False:
#    if defenseTeamDead == False:
#        print("Printing Attack Moves")
#        attackStep1BondaryCheck1()
#        attackStep1BondaryCheck2()
#        attackStep1BondaryCheck3()
#        attackStep1BondaryCheck4()
#        attackStep1BondaryCheck5()
#        teamAttacksideCheck()
#        print("Printing Defense Moves")
#        defenseStep1BondaryCheck1()
#        defenseStep1BondaryCheck2()
#        defenseStep1BondaryCheck3()
#        defenseStep1BondaryCheck4()
#        defenseStep1BondaryCheck5()
#        teamDefensesideCheck()

#    with open("round1.1Phase.json", "w") as f:
#        json.dump(round1Layout, f, indent=4)

#if attackTeamDead == True:
#    if defenseTeamDead == True:
#        print("Round Finished")




