import tkinter

import customtkinter
from PIL import Image
import json
number = 0

app = customtkinter.CTk()
app.geometry("1000x1000")
app.title("Valorant Auto Play Viewer")

def json_read():
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

    globals()[f'Player1PosX'] = Player1["posX"]
    globals()[f'Player2PosX'] = Player2["posX"]
    globals()[f'Player3PosX'] = Player3["posX"]
    globals()[f'Player4PosX'] = Player4["posX"]
    globals()[f'Player5PosX'] = Player5["posX"]
    globals()[f'Player6PosX'] = Player6["posX"]
    globals()[f'Player7PosX'] = Player7["posX"]
    globals()[f'Player8PosX'] = Player8["posX"]
    globals()[f'Player9PosX'] = Player9["posX"]
    globals()[f'Player10PosX'] = Player10["posX"]

    globals()[f'Player1PosY'] = Player1["posY"]
    globals()[f'Player2PosY'] = Player2["posY"]
    globals()[f'Player3PosY'] = Player3["posY"]
    globals()[f'Player4PosY'] = Player4["posY"]
    globals()[f'Player5PosY'] = Player5["posY"]
    globals()[f'Player6PosY'] = Player6["posY"]
    globals()[f'Player7PosY'] = Player7["posY"]
    globals()[f'Player8PosY'] = Player8["posY"]
    globals()[f'Player9PosY'] = Player9["posY"]
    globals()[f'Player10PosY'] = Player10["posY"]



json_read()


print(Player1PosX)

Player1PosXConversion = Player1PosX * 10
Player1PosYConversion = Player1PosY * 10

Player2PosXConversion = Player2PosX * 10
Player2PosYConversion = Player2PosY * 10

Player3PosXConversion = Player3PosX * 10
Player3PosYConversion = Player3PosY * 10

Player4PosXConversion = Player4PosX * 10
Player4PosYConversion = Player4PosY * 10

Player5PosXConversion = Player5PosX * 10
Player5PosYConversion = Player5PosY * 10

Player6PosXConversion = Player6PosX * 10
Player6PosYConversion = Player6PosY * 10

Player7PosXConversion = Player7PosX * 10
Player7PosYConversion = Player7PosY * 10

Player8PosXConversion = Player8PosX * 10
Player8PosYConversion = Player8PosY * 10

Player9PosXConversion = Player9PosX * 10
Player9PosYConversion = Player9PosY * 10

Player10PosXConversion = Player10PosX * 10
Player10PosYConversion = Player10PosY * 10


print("Player 1 Pos")
print(Player1PosXConversion)
print(Player1PosYConversion)
print("Player 2 Pos")
print(Player2PosXConversion)
print(Player2PosYConversion)
print("Player 3 Pos")
print(Player3PosXConversion)
print(Player3PosYConversion)
print("Player 4 Pos")
print(Player4PosXConversion)
print(Player4PosYConversion)
print("Player 5 Pos")
print(Player5PosXConversion)
print(Player5PosYConversion)
print("Player 6 Pos")
print(Player6PosXConversion)
print(Player6PosYConversion)
print("Player 7 Pos")
print(Player7PosXConversion)
print(Player7PosYConversion)
print("Player 8 Pos")
print(Player8PosXConversion)
print(Player8PosYConversion)
print("Player 9 Pos")
print(Player9PosXConversion)
print(Player9PosYConversion)
print("Player 10 Pos")
print(Player10PosXConversion)
print(Player10PosYConversion)

print("Players Positions Showing")


my_image = customtkinter.CTkImage(light_image=Image.open("Lotus-Map.png"),
                                  dark_image=Image.open("Lotus-Map.png"),
                                  size=(1000, 1000))
background_label = customtkinter.CTkLabel(app, image=my_image, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Load and place the player image on top of the background
player1 = customtkinter.CTkImage(light_image=Image.open("Omen.png"),
                                 dark_image=Image.open("Omen.png"),
                                 size=(30, 30))
player1_label = customtkinter.CTkLabel(app, image=player1, text="")
player1_label.place(x=Player1PosXConversion, y=Player1PosYConversion)
print("Player 1 Positions Showing")
player2 = customtkinter.CTkImage(light_image=Image.open("Omen.png"),
                                 dark_image=Image.open("Omen.png"),
                                 size=(30, 30))
player2_label = customtkinter.CTkLabel(app, image=player2, text="")
player2_label.place(x=Player2PosXConversion, y=Player2PosYConversion)
print("Player 2 Positions Showing")
player3 = customtkinter.CTkImage(light_image=Image.open("Omen.png"),
                                 dark_image=Image.open("Omen.png"),
                                 size=(30, 30))
player3_label = customtkinter.CTkLabel(app, image=player3, text="")
player3_label.place(x=Player3PosXConversion, y=Player3PosYConversion)
print("Player 3 Positions Showing")
player4 = customtkinter.CTkImage(light_image=Image.open("Omen.png"),
                                 dark_image=Image.open("Omen.png"),
                                 size=(30, 30))
player4_label = customtkinter.CTkLabel(app, image=player4, text="")
player4_label.place(x=Player4PosXConversion, y=Player4PosYConversion)
print("Player 4 Positions Showing")
player5 = customtkinter.CTkImage(light_image=Image.open("Omen.png"),
                                 dark_image=Image.open("Omen.png"),
                                 size=(30, 30))
player5_label = customtkinter.CTkLabel(app, image=player5, text="")
player5_label.place(x=Player5PosXConversion, y=Player5PosYConversion)
print("Player 5 Positions Showing")
player6 = customtkinter.CTkImage(light_image=Image.open("Omen.png"),
                                 dark_image=Image.open("Omen.png"),
                                 size=(30, 30))
player6_label = customtkinter.CTkLabel(app, image=player6, text="")
player6_label.place(x=Player6PosXConversion, y=Player6PosYConversion)
print("Player 6 Positions Showing")
player7 = customtkinter.CTkImage(light_image=Image.open("Omen.png"),
                                 dark_image=Image.open("Omen.png"),
                                 size=(30, 30))
player7_label = customtkinter.CTkLabel(app, image=player7, text="")
player7_label.place(x=Player7PosXConversion, y=Player7PosYConversion)
print("Player 7 Positions Showing")
player8 = customtkinter.CTkImage(light_image=Image.open("Omen.png"),
                                 dark_image=Image.open("Omen.png"),
                                 size=(30, 30))
player8_label = customtkinter.CTkLabel(app, image=player8, text="")
player8_label.place(x=Player8PosXConversion, y=Player8PosYConversion)
print("Player 8 Positions Showing")
player9 = customtkinter.CTkImage(light_image=Image.open("Omen.png"),
                                 dark_image=Image.open("Omen.png"),
                                 size=(30, 30))
player9_label = customtkinter.CTkLabel(app, image=player9, text="")
player9_label.place(x=Player9PosXConversion, y=Player9PosYConversion)
print("Player 9 Positions Showing")
player10 = customtkinter.CTkImage(light_image=Image.open("Omen.png"),
                                  dark_image=Image.open("Omen.png"),
                                  size=(30, 30))
player10_label = customtkinter.CTkLabel(app, image=player10, text="")
player10_label.place(x=Player10PosXConversion, y=Player10PosYConversion)
print("Player 10 Positions Showing")




app.mainloop()
