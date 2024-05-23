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


def attackRound1Player1():
    global attackPos1X
    global attackPos1Y
    attackPos1X = randint(mixChangeX, maxChangeX)
    attackPos1Y = randint(minChangeY, maxChangeY)
    global attackPos1
    attackPos1 = str(attackPos1X) + "," + str(attackPos1Y)
def attackRound1Player2():
    global attackPos2X
    global attackPos2Y
    attackPos2X = randint(mixChangeX, maxChangeX)
    attackPos2Y = randint(minChangeY, maxChangeY)
    global attackPos2
    attackPos2 = str(attackPos2X) + "," + str(attackPos2Y)
def attackRound1Player3():
    global attackPos3X
    global attackPos3Y
    attackPos3X = randint(mixChangeX, maxChangeX)
    attackPos3Y = randint(minChangeY, maxChangeY)
    global attackPos3
    attackPos3 = str(attackPos3X) + "," + str(attackPos3Y)
def attackRound1Player4():
    global attackPos4X
    global attackPos4Y
    attackPos4X = randint(mixChangeX, maxChangeX)
    attackPos4Y = randint(minChangeY, maxChangeY)
    global attackPos4
    attackPos4 = str(attackPos4X) + "," + str(attackPos4Y)
def attackRound1Player5():
    global attackPos5X
    global attackPos5Y
    attackPos5X = randint(mixChangeX, maxChangeX)
    attackPos5Y = randint(minChangeY, maxChangeY)
    global attackPos5
    attackPos5 = str(attackPos5X) + "," + str(attackPos5Y)
def defenseRound1Player1():
    global defensePos1X
    global defensePos1Y
    attackPos1X = randint(mixChangeX, maxChangeX)
    attackPos1Y = randint(minChangeY, maxChangeY)
    global defensePos1
    defensePos1 = str(defensePos1X) + "," + str(defensePos1Y)
def defenseRound1Player2():
    global defensePos2X
    global defensePos2Y
    attackPos2X = randint(mixChangeX, maxChangeX)
    attackPos2Y = randint(minChangeY, maxChangeY)
    global defensePos2
    defensePos2 = str(defensePos2X) + "," + str(defensePos2Y)
def defenseRound1Player3():
    global defensePos3X
    global defensePos3Y
    attackPos3X = randint(mixChangeX, maxChangeX)
    attackPos3Y = randint(minChangeY, maxChangeY)
    global defensePos3
    defensePos3 = str(defensePos3X) + "," + str(defensePos3Y)
def defenseRound1Player4():
    global defensePos4X
    global defensePos4Y
    attackPos4X = randint(mixChangeX, maxChangeX)
    attackPos4Y = randint(minChangeY, maxChangeY)
    global defensePos4
    defensePos4 = str(defensePos4X) + "," + str(defensePos4Y)
def defenseRound1Player5():
    global defensePos5X
    global defensePos5Y
    attackPos5X = randint(mixChangeX, maxChangeX)
    attackPos5Y = randint(minChangeY, maxChangeY)
    global defensePos5
    defensePos5 = str(defensePos5X) + "," + str(defensePos5Y)
def playerAttackAttackSideCheck(playerNum):
    global isAttacked
    global attackPlayer1Dead
    global attackPlayer2Dead
    global attackPlayer3Dead
    global attackPlayer4Dead
    global attackPlayer5Dead
    global defensePlayer1Dead
    global defensePlayer2Dead
    global defensePlayer3Dead
    global defensePlayer4Dead
    global defensePlayer5Dead
    isAttacked = False
    winChance = 0
    differnce = 0

    if playerNum == "1":
        difference = attackPos1X - defensePos1X
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer1Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer1Dead = true
                print("defense player 1 dead")

        difference = defensePos1X - attackPos1X
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer1Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer1Dead = true
                print("defense player 1 dead")
        difference = attackPos1X - defensePos2X
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer2Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer2Dead = true
                print("defense player 2 dead")
        difference = defensePos2X - attackPos1X
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer2Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer2Dead = true
                print("defense player 2 dead")
        difference = attackPos1X - defensePos3X
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer3Dead = false
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer3Dead = true
                print("defense player 3 dead")
        difference = defensePos3X - attackPos1X
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer3Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer3Dead = true
                print("defense player 3 dead")
        difference = attackPos1X - defensePos4X
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer4Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer4Dead = true
                print("defense player 4 dead")
        difference = defensePos4X - attackPos1X
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer4Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer4Dead = true
                print("defense player 4 dead")
        difference = attackPos1X - defensePos5X
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer5Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer5Dead = true
                print("defense player 5 dead")
        difference = defensePos5X - attackPos1X
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer5Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer5Dead = true
                print("defense player 5 dead")
        difference = attackPos1Y - defensePos1Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer1Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer1Dead = true
                print("defense player 1 dead")

        difference = defensePos1Y - attackPos1Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer1Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer1Dead = true
                print("defense player 1 dead")
        difference = attackPos1Y - defensePos2Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer2Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer2Dead = true
                print("defense player 2 dead")
        difference = defensePos2Y - attackPos1Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer2Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer2Dead = true
                print("defense player 2 dead")
        difference = attackPos1Y - defensePos3Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer3Dead = false
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer3Dead = true
                print("defense player 3 dead")
        difference = defensePos3Y - attackPos1Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer3Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer3Dead = true
                print("defense player 3 dead")
        difference = attackPos1Y - defensePos4Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer4Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer4Dead = true
                print("defense player 4 dead")
        difference = defensePos4Y - attackPos1Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer4Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer4Dead = true
                print("defense player 4 dead")
        difference = attackPos1Y - defensePos5Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer5Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer5Dead = true
                print("defense player 5 dead")
        difference = defensePos5Y - attackPos1Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 1 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer1Dead = true
                defensePlayer5Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer5Dead = true
                print("defense player 5 dead")

    if playerNum == "2":
        difference = attackPos2X - defensePos1X
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = true
                defensePlayer1Dead = false
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = false
                defensePlayer1Dead = true
                print("defense player 1 dead")

        difference = defensePos1X - attackPos2X
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = true
                defensePlayer1Dead = false
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = false
                defensePlayer1Dead = true
                print("defense player 1 dead")
        difference = attackPos2X - defensePos2X
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = true
                defensePlayer2Dead = false
                print("attack player 1 dead")
            if winChance <= 50:
                attackPlayer2Dead = false
                defensePlayer2Dead = true
                print("defense player 2 dead")
        difference = defensePos2X - attackPos2X
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = true
                defensePlayer2Dead = false
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = false
                defensePlayer2Dead = true
                print("defense player 2 dead")
        difference = attackPos2X - defensePos3X
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = true
                defensePlayer3Dead = false
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer1Dead = false
                defensePlayer3Dead = true
                print("defense player 3 dead")
        difference = defensePos3X - attackPos2X
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = true
                defensePlayer3Dead = false
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = false
                defensePlayer3Dead = true
                print("defense player 3 dead")
        difference = attackPos2X - defensePos4X
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = true
                defensePlayer4Dead = false
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = false
                defensePlayer4Dead = true
                print("defense player 4 dead")
        difference = defensePos4X - attackPos2X
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = true
                defensePlayer4Dead = false
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = false
                defensePlayer4Dead = true
                print("defense player 4 dead")
        difference = attackPos2X - defensePos5X
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = true
                defensePlayer5Dead = false
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = false
                defensePlayer5Dead = true
                print("defense player 5 dead")
        difference = defensePos5X - attackPos2X
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = true
                defensePlayer5Dead = false
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = false
                defensePlayer5Dead = true
                print("defense player 5 dead")
        difference = attackPos2Y - defensePos1Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = True
                defensePlayer1Dead = False
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = defensePos1Y - attackPos2Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = True
                defensePlayer1Dead = False
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = attackPos2Y - defensePos2Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = True
                defensePlayer2Dead = False
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = defensePos2Y - attackPos2Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = True
                defensePlayer2Dead = False
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = attackPos2Y - defensePos3Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = True
                defensePlayer3Dead = False
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = defensePos3Y - attackPos2Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = True
                defensePlayer3Dead = False
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = attackPos2Y - defensePos4Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = True
                defensePlayer4Dead = False
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = defensePos4Y - attackPos2Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = True
                defensePlayer4Dead = False
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = attackPos2Y - defensePos5Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = True
                defensePlayer5Dead = False
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")

        difference = defensePos5Y - attackPos2Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 2 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer2Dead = True
                defensePlayer5Dead = False
                print("attack player 2 dead")
            if winChance <= 50:
                attackPlayer2Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")
    if playerNum == "3":
        difference = attackPos3X - defensePos1X
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer1Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = defensePos1X - attackPos3X
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer1Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = attackPos3X - defensePos2X
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer2Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = defensePos2X - attackPos3X
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer2Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = attackPos3X - defensePos3X
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer3Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = defensePos3X - attackPos3X
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer3Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = attackPos3X - defensePos4X
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer4Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = defensePos4X - attackPos3X
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer4Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = attackPos3X - defensePos5X
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer5Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")

        difference = defensePos5X - attackPos3X
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer5Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")

        difference = attackPos3Y - defensePos1Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer1Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = defensePos1Y - attackPos3Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer1Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = attackPos3Y - defensePos2Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer2Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = defensePos2Y - attackPos3Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer2Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = attackPos3Y - defensePos3Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer3Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = defensePos3Y - attackPos3Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer3Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = attackPos3Y - defensePos4Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer4Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = defensePos4Y - attackPos3Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer4Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = attackPos3Y - defensePos5Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer5Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")

        difference = defensePos5Y - attackPos3Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 3 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer3Dead = True
                defensePlayer5Dead = False
                print("attack player 3 dead")
            if winChance <= 50:
                attackPlayer3Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")
    if playerNum == "4":
        difference = attackPos4X - defensePos1X
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer1Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = defensePos1X - attackPos4X
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer1Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = attackPos4X - defensePos2X
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer2Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = defensePos2X - attackPos4X
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer2Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = attackPos4X - defensePos3X
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer3Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = defensePos3X - attackPos4X
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer3Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = attackPos4X - defensePos4X
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer4Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = defensePos4X - attackPos4X
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer4Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = attackPos4X - defensePos5X
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer5Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")

        difference = defensePos5X - attackPos4X
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer5Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")

        difference = attackPos4Y - defensePos1Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer1Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = defensePos1Y - attackPos4Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer1Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = attackPos4Y - defensePos2Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer2Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = defensePos2Y - attackPos4Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer2Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = attackPos4Y - defensePos3Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer3Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = defensePos3Y - attackPos4Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer3Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = attackPos4Y - defensePos4Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer4Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = defensePos4Y - attackPos4Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer4Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = attackPos4Y - defensePos5Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer5Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")

        difference = defensePos5Y - attackPos4Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 4 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer4Dead = True
                defensePlayer5Dead = False
                print("attack player 4 dead")
            if winChance <= 50:
                attackPlayer4Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")
    if playerNum == "5":
        difference = attackPos5X - defensePos1X
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer1Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = defensePos1X - attackPos5X
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer1Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = attackPos5X - defensePos2X
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer2Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = defensePos2X - attackPos5X
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer2Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = attackPos5X - defensePos3X
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer3Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = defensePos3X - attackPos5X
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer3Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = attackPos5X - defensePos4X
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer4Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = defensePos4X - attackPos5X
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer4Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = attackPos5X - defensePos5X
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer5Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")

        difference = defensePos5X - attackPos5X
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer5Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")

        difference = attackPos5Y - defensePos1Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer1Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = defensePos1Y - attackPos5Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer1Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer1Dead = True
                print("defense player 1 dead")

        difference = attackPos5Y - defensePos2Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer2Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = defensePos2Y - attackPos5Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer2Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer2Dead = True
                print("defense player 2 dead")

        difference = attackPos5Y - defensePos3Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer3Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = defensePos3Y - attackPos5Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer3Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer3Dead = True
                print("defense player 3 dead")

        difference = attackPos5Y - defensePos4Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer4Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = defensePos4Y - attackPos5Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer4Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer4Dead = True
                print("defense player 4 dead")

        difference = attackPos5Y - defensePos5Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer5Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")

        difference = defensePos5Y - attackPos5Y
        if difference <= 10:
            isAttacked = True
            print("Attacker 5 v Defender 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                attackPlayer5Dead = True
                defensePlayer5Dead = False
                print("attack player 5 dead")
            if winChance <= 50:
                attackPlayer5Dead = False
                defensePlayer5Dead = True
                print("defense player 5 dead")
def playerAttackDefenseSideCheck(playerNum):
    global isAttacked
    global attackPlayer1Dead
    global attackPlayer2Dead
    global attackPlayer3Dead
    global attackPlayer4Dead
    global attackPlayer5Dead
    global defensePlayer1Dead
    global defensePlayer2Dead
    global defensePlayer3Dead
    global defensePlayer4Dead
    global defensePlayer5Dead
    isAttacked = False
    winChance = 0
    differnce = 0

    if playerNum == "1":
        difference = defensePos1X - attackPos1X
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer1Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = attackPos1X - defensePos1X
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer1Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = defensePos1X - attackPos2X
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer2Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = attackPos2X - defensePos1X
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer2Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = defensePos1X - attackPos3X
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer3Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer3Dead = True
                print("attack player 1 dead")

        difference = attackPos3X - defensePos1X
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer3Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = defensePos1X - attackPos4X
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer4Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = attackPos4X - defensePos1X
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer4Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = defensePos1X - attackPos5X
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer5Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")

        difference = attackPos5X - defensePos1X
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer5Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")
        difference = defensePos1Y - attackPos1Y
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer1Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = attackPos1Y - defensePos1Y
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer1Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = defensePos1Y - attackPos2Y
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer2Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = attackPos2Y - defensePos1Y
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer2Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = defensePos1Y - attackPos3Y
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer3Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer3Dead = True
                print("attack player 1 dead")

        difference = attackPos3Y - defensePos1Y
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer3Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = defensePos1Y - attackPos4Y
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer4Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = attackPos4Y - defensePos1Y
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer4Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = defensePos1Y - attackPos5Y
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer5Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")

        difference = attackPos5Y - defensePos1Y
        if difference <= 10:
            isAttacked = True
            print("Defender 1 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer1Dead = True
                attackPlayer5Dead = False
                print("defense player 1 dead")
            if winChance <= 50:
                defensePlayer1Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")
    if playerNum == "2":
        difference = defensePos2X - attackPos1X
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer1Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = attackPos1X - defensePos2X
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer1Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = defensePos2X - attackPos2X
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer2Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = attackPos2X - defensePos2X
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer2Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = defensePos2X - attackPos3X
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer3Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer3Dead = True
                print("attack player 1 dead")

        difference = attackPos3X - defensePos2X
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer3Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = defensePos2X - attackPos4X
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer4Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = attackPos4X - defensePos2X
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer4Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = defensePos2X - attackPos5X
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer5Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")

        difference = attackPos5X - defensePos2X
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer5Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")
        difference = defensePos2Y - attackPos1Y
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer1Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = attackPos1Y - defensePos2Y
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer1Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = defensePos2Y - attackPos2Y
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer2Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = attackPos2Y - defensePos2Y
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer2Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = defensePos2Y - attackPos3Y
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer3Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer3Dead = True
                print("attack player 1 dead")

        difference = attackPos3Y - defensePos2Y
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer3Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = defensePos2Y - attackPos4Y
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer4Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = attackPos4Y - defensePos2Y
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer4Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = defensePos2Y - attackPos5Y
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer5Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")

        difference = attackPos5Y - defensePos2Y
        if difference <= 10:
            isAttacked = True
            print("Defender 2 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer2Dead = True
                attackPlayer5Dead = False
                print("defense player 2 dead")
            if winChance <= 50:
                defensePlayer2Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")
    if playerNum == "3":
        difference = defensePos3X - attackPos1X
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer1Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = attackPos1X - defensePos3X
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer1Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = defensePos3X - attackPos2X
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer2Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = attackPos2X - defensePos3X
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer2Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = defensePos3X - attackPos3X
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer3Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer3Dead = True
                print("attack player 1 dead")

        difference = attackPos3X - defensePos3X
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer3Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = defensePos3X - attackPos4X
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer4Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = attackPos4X - defensePos3X
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer4Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = defensePos3X - attackPos5X
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer5Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")

        difference = attackPos5X - defensePos3X
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer5Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")
        difference = defensePos3Y - attackPos1Y
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer1Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = attackPos1Y - defensePos3Y
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer1Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = defensePos3Y - attackPos2Y
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer2Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = attackPos2Y - defensePos3Y
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer2Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = defensePos3Y - attackPos3Y
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer3Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer3Dead = True
                print("attack player 1 dead")

        difference = attackPos3Y - defensePos3Y
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer3Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = defensePos3Y - attackPos4Y
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer4Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = attackPos4Y - defensePos3Y
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer4Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = defensePos3Y - attackPos5Y
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer5Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")

        difference = attackPos5Y - defensePos3Y
        if difference <= 10:
            isAttacked = True
            print("Defender 3 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer3Dead = True
                attackPlayer5Dead = False
                print("defense player 3 dead")
            if winChance <= 50:
                defensePlayer3Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")
    if playerNum == "4":
        difference = defensePos4X - attackPos1X
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer1Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = attackPos1X - defensePos4X
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer1Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = defensePos4X - attackPos2X
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer2Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = attackPos2X - defensePos4X
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer2Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = defensePos4X - attackPos3X
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer3Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = attackPos3X - defensePos4X
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer3Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = defensePos4X - attackPos4X
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer4Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = attackPos4X - defensePos4X
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer4Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = defensePos4X - attackPos5X
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer5Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")

        difference = attackPos5X - defensePos4X
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer5Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")
        difference = defensePos4Y - attackPos1Y
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer1Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = attackPos1Y - defensePos4Y
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer1Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = defensePos4Y - attackPos2Y
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer2Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = attackPos2Y - defensePos4Y
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer2Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = defensePos4Y - attackPos3Y
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer3Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = attackPos3Y - defensePos4Y
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer3Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = defensePos4Y - attackPos4Y
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer4Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = attackPos4Y - defensePos4Y
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer4Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = defensePos4Y - attackPos5Y
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer5Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")

        difference = attackPos5Y - defensePos4Y
        if difference <= 10:
            isAttacked = True
            print("Defender 4 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer4Dead = True
                attackPlayer5Dead = False
                print("defense player 4 dead")
            if winChance <= 50:
                defensePlayer4Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")
    if playerNum == "5":
        difference = defensePos5X - attackPos1X
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer1Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = attackPos1X - defensePos5X
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer1Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = defensePos5X - attackPos2X
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer2Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = attackPos2X - defensePos5X
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer2Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = defensePos5X - attackPos3X
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer3Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = attackPos3X - defensePos5X
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer3Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = defensePos5X - attackPos4X
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer4Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = attackPos4X - defensePos5X
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer4Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = defensePos5X - attackPos5X
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer5Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")

        difference = attackPos5X - defensePos5X
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer5Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")
        difference = defensePos5Y - attackPos1Y
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer1Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = attackPos1Y - defensePos5Y
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 1")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer1Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer1Dead = True
                print("attack player 1 dead")

        difference = defensePos5Y - attackPos2Y
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer2Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = attackPos2Y - defensePos5Y
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 2")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer2Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer2Dead = True
                print("attack player 2 dead")

        difference = defensePos5Y - attackPos3Y
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer3Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = attackPos3Y - defensePos5Y
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 3")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer3Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer3Dead = True
                print("attack player 3 dead")

        difference = defensePos5Y - attackPos4Y
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer4Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = attackPos4Y - defensePos5Y
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 4")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer4Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer4Dead = True
                print("attack player 4 dead")

        difference = defensePos5Y - attackPos5Y
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer5Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")

        difference = attackPos5Y - defensePos5Y
        if difference <= 10:
            isAttacked = True
            print("Defender 5 v Attacker 5")
            winChance = randint(1, 100)
            if winChance >= 50:
                defensePlayer5Dead = True
                attackPlayer5Dead = False
                print("defense player 5 dead")
            if winChance <= 50:
                defensePlayer5Dead = False
                attackPlayer5Dead = True
                print("attack player 5 dead")


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
            playerAttackAttackSideCheck("1")
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
            playerAttackAttackSideCheck("2")
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
            playerAttackAttackSideCheck("3")
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
            playerAttackAttackSideCheck("4")
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
            playerAttackAttackSideCheck("5")
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
            playerAttackDefenseSideCheck("1")
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
            playerAttackDefenseSideCheck("2")
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
            playerAttackDefenseSideCheck("3")
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
            playerAttackDefenseSideCheck("4")
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
            playerAttackDefenseSideCheck("5")

print("Printing Attack Moves")
attackRound1BondaryCheck1()
sleep(0.5)
attackRound1BondaryCheck2()
sleep(0.5)
attackRound1BondaryCheck3()
sleep(0.5)
defenseRoundBondaryCheck4()
sleep(0.5)
defenseRoundBondaryCheck5()
sleep(0.5)
print("Printing Defense Moves")
defenseRoundBondaryCheck1()
sleep(0.5)
defenseRoundBondaryCheck2()
sleep(0.5)
defenseRoundBondaryCheck3()
sleep(0.5)
defenseRoundBondaryCheck4()
sleep(0.5)
defenseRoundBondaryCheck5()
sleep(0.5)

