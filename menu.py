import tkinter as tk
from Pacman20 import *
import pygame


from musiqueVRAI import*

root = tk.Tk() #création fenêtre


root.title("Master window")
TFR_U=pygame.mixer.Sound("TFR_Unity.wav")

def jouer():#s'active quand on clique "start"
    root.destroy()
    mon_audio.stop()
    TFR_U.play()
    Jeu()
    
     
bt_child_window = tk.Button(root, text="Start", command=jouer,width=20)
bt_child_window.pack(expand=0)


image = PhotoImage(file='images/fond.gif') #appelation de l'image
canvas = Canvas(root, width=1, height=1)
canvas.pack(fill=BOTH, expand=1)
canvas.create_image(0, 0, image=image, anchor=NW)
#Anchor definit ou est placé l'image par rapport a l'origine
root.geometry('635x707')#dimension de l'image
root.mainloop()





