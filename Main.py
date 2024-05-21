from random import randint
from time import sleep

gridSizeX = 1000
gridSizeY = 1000

def spawn_enemies(amount):
    def Enemy(enemyNum):
        enemySpawnRadiusMaxX = gridSizeX - 700
        enemyPos1X = randint(0, enemySpawnRadiusMaxX)
        #test

