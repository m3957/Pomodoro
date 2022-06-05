from time import sleep
import os
import pygame
import random
pygame.mixer.init()
pomodoro = 900 #15 minutes
pomobreak = 300 #5 minutes
numpomodoro = 4


os.system("clear")
print("""
Choix de la musique

1. Context Sensitive
2. Toute la musique
""")
musicpath = int(input())

if musicpath == 1:
    path = f"/home/{os.getlogin()}/Music/Context Sensitive/"
if musicpath == 2:
    path = f"/home/{os.getlogin()}/Music/"
#else:
    #print("Mais bruh, tu m'as écrit quoi, là?!")
    #sleep(3)
    #quit()

all_mp3 = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp3')]
randomfile = random.choice(all_mp3)
pygame.mixer.music.load(randomfile)
pygame.mixer.music.play()


for i in range(numpomodoro):
    for i in range(pomodoro):
        os.system("clear")
        print("= Txt Pomodoro ========= Mode: Pomodoro")
        print(f"{i+1}/{pomodoro}")
        sleep(1)
    for i in range(pomobreak):
        os.system("clear")
        print("= Txt Pomodoro ========= Mode: Break")
        print(f"{i+1}/{pomobreak}")
        sleep(1)
