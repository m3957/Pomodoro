from time import sleep
import os
import pygame
import random
pygame.mixer.init()
pomodoro = 900 #15 minutes
pomobreak = 300 #5 minutes
numpomodoro = 4

#if os.name == "posix":
    #startpath = "/home/{os.getlogin()}/"
#if os.name == "nt":
    #startpath = """C:\Users\{os.getlogin()}\"""

#Vite il me faut un fix pour le code 10-13


##############################################################
# Dans cette section, vous pouvez personnalisez le code      #
# pour avoir ce que vous voulez comme choix de musique,      #
# et si vous ne comprenez pas, voici un exemple.             #
# Vous voyez à la ligne 37 un path = f""? Vous pouvez        #
# le changer pour le path vers la bonne musique. Ensuite,    #
# ligne 28, changez le print pour afficher une option pour   #
# votre nouveau dossier. FLEMME DE FAIRE UN TRUC AUTOMATIQUE #
##############################################################
os.system("clear")
print("""
Choix de la musique

1. Context Sensitive
2. Toute la musique
""")
musicpath = int(input())

if musicpath == 1:
    path = f"/home/{os.getlogin()}/Music/Context Sensitive/" #Changez pour votre dossier de musique
if musicpath == 2:
    path = f"/home/{os.getlogin()}/Music/"
###############################################################

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
