import csv
import json

reiterationNUM = input("reiteration: ")


def json_read(number):
    with open("spawnPhase.json") as spawn:
        data = json.load(spawn)
    atkNum = 1
    defNum = 1
    Number = 1
    for i in range(10):
        for Num in data:
            globals()[f'Player{Number}'] = Num
            Number = Number + 1

        objects = data[i]["team"]
        number = 0
        for object in objects:
            globals()[f'team{number}'] = object[0]
            number += 1
        if team0 == "A":
            globals()[f'AttackPlayer{atkNum}Team'] = team0 + team1 + team2 + team3 + team4 + team5
            atkNum += 1


        else:
            globals()[f'DefensePlayer{defNum}Team'] = team0 + team1 + team2 + team3 + team4 + team5 + team6
            defNum += 1

    globals()[f'Run{number}Player1PosX'] = Player1["posX"]
    globals()[f'Run{number}Player2PosX'] = Player2["posX"]
    globals()[f'Run{number}Player3PosX'] = Player3["posX"]
    globals()[f'Run{number}Player4PosX'] = Player4["posX"]
    globals()[f'Run{number}Player5PosX'] = Player5["posX"]
    globals()[f'Run{number}Player6PosX'] = Player6["posX"]
    globals()[f'Run{number}Player7PosX'] = Player7["posX"]
    globals()[f'Run{number}Player8PosX'] = Player8["posX"]
    globals()[f'Run{number}Player9PosX'] = Player9["posX"]
    globals()[f'Run{number}Player10PosX'] = Player10["posX"]

    globals()[f'Run{number}Player1PosY'] = Player1["posY"]
    globals()[f'Run{number}Player2PosY'] = Player2["posY"]
    globals()[f'Run{number}Player3PosY'] = Player3["posY"]
    globals()[f'Run{number}Player4PosY'] = Player4["posY"]
    globals()[f'Run{number}Player5PosY'] = Player5["posY"]
    globals()[f'Run{number}Player6PosY'] = Player6["posY"]
    globals()[f'Run{number}Player7PosY'] = Player7["posY"]
    globals()[f'Run{number}Player8PosY'] = Player8["posY"]
    globals()[f'Run{number}Player9PosY'] = Player9["posY"]
    globals()[f'Run{number}Player10PosY'] = Player10["posY"]

for i in range(int(reiterationNUM)):
    with open("Main.py") as file:
        exec(file.read())

    json_read(i)


with open('SpawnAITrain.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Succses", "Player1PosX", "Player1PosY", "Player2PosX", "Player2PosY", "Player3PosX", "Player3PosY", "Player4PosX", "Player4PosY",
             "Player5PosX", "Player5PosY", "Player6PosX", "Player6PosY", "Player7PosX", "Player7PosY", "Player8PosX", "Player8PosY",
             "Player9PosX", "Player9PosY", "Player10PosX", "Player10PosY"]

    writer.writerow(field)
    writer.writerow(["N/A", globals()[f'Run{i}Player1PosX'], globals()[f'Run{i}Player1PosY'], globals()[f'Run{i}Player2PosX'], globals()[f'Run{i}Player2PosY'], globals()[f'Run{i}Player3PosX'], globals()[f'Run{i}Player3PosY']])