import numpy as np
from tkinter import *
from random import randint
import time
from threading import Thread
import pygame
from PIL import ImageTk
from PIL import Image

pygame.mixer.init()
perdu=pygame.mixer.Sound("pacman_death.wav")
perdu.set_volume(1)

   
carre = 35 #côté carré
 
fin_de_jeu = False
attente = 0.000000011
   
#Dans la matrice :
# 0 = case libre
# 1 = mur
# 2 = pacman
# 3 = fantome
# 4 = bonbons
   
pacman = [9,11]
fantomes=[[9,7]]
a = np.array([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
              [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],      
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
              [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1],
              [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1],
              [1,1,1,1,0,1,0,0,0,3,0,0,0,1,0,1,1,1,1],
              [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
              [1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1],
              [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
              [1,1,1,1,0,1,0,0,0,2,0,0,0,1,0,1,1,1,1],
              [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
              [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
              [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
              [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
              [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
              [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
score=0 #initialisation du score
   
class Fantome(Thread):
    def __init__(self, numero):
         Thread.__init__(self)
         self.position = fantomes[numero]
     
    def deplacement(self): #déplacement fantôme
        global a, Zone
        direction = randint(1,4)
        if direction == 1:
                if a[self.position[1]-1][self.position[0]]!=1!=3:  #haut
                        Zone.delete(all)
                        a[self.position[1]][self.position[0]]=0  
                        self.position[1] -=1
                        a[self.position[1]][self.position[0]]=3
        if direction == 2:
                if a[self.position[1]][self.position[0]-1]!=1!=3:#gauche
                        Zone.delete(all)
                        a[self.position[1]][self.position[0]]=0
                        self.position[0] -=1
                        a[self.position[1]][self.position[0]]=3
        if direction == 3:
                if a[self.position[1]+1][self.position[0]]!=1!=3:#bas
                        Zone.delete(all)
                        a[self.position[1]][self.position[0]]=0
                        self.position[1] +=1
                        a[self.position[1]][self.position[0]]=3
        if direction == 4:
                if a[self.position[1]][self.position[0]+1]!=1!=3:#droite
                        Zone.delete(all)
                        a[self.position[1]][self.position[0]]=0
                        self.position[0] +=1
                        a[self.position[1]][self.position[0]]=3
     
    def run(self):
        while not fin_de_jeu:
            self.deplacement()
            time.sleep(attente)
            colorie_quadrillage()
                         
def Fin():
    global fin_de_jeu, Fenêtre
    fin_de_jeu = True
    perdu.play()
    Fenêtre.destroy()
    Game_over = Tk()
    canvas = Canvas(Game_over, width=100, height=100)
    canvas.create_text(50, 20, text='GAME OVER',fill='red')
    canvas.create_text(50, 40, text='le score est de :', anchor=CENTER)
    canvas.create_text(50, 60, text=str(score), anchor=CENTER)
    canvas.pack()
    
          
      
   
def grille(epaisseur, couleur): #création grille
    global Zone
    for i in range(nb_ligne-1):
        Zone.create_line(0, hauteur_case*(i+1), Largeur, hauteur_case*(i+1), fill=couleur, width=epaisseur)
    for j in range(nb_colonne-1):
        Zone.create_line(largeur_case*(j+1), 0, largeur_case*(j+1), Hauteur, fill=couleur, width=epaisseur)
    Zone.pack()
   
   
def colorie_case(position, color='white'):#colorisation case selon chiffre matrice
        if a[position[0]][position[1]] == 1:
                Zone.create_rectangle(largeur_case*(position[1]), hauteur_case*(position[0]), largeur_case*(position[1]+1), hauteur_case*(position[0]+1), fill='black')
                Zone.pack()
        elif a[position[0]][position[1]] == 2:
                Zone.create_image(largeur_case*(position[1])+carre//2, hauteur_case*(position[0])+carre//2, image=img)
                Zone.pack()
        elif a[position[0]][position[1]] == 3:
                Zone.create_rectangle(largeur_case*(position[1]), hauteur_case*(position[0]), largeur_case*(position[1]+1), hauteur_case*(position[0]+1), fill='purple')
                Zone.pack()
        elif a[position[0]][position[1]] == 0:
                Zone.create_rectangle(largeur_case*(position[1]), hauteur_case*(position[0]), largeur_case*(position[1]+1), hauteur_case*(position[0]+1), fill=color)
                Zone.pack()
                   
def colorie_quadrillage():
        for i in range(nb_ligne):
                for j in range(nb_colonne):
                        colorie_case([i,j])
                                 

                         
def haut(evt):#s'active quand on clique sur haut
        global pacman
        global a
        global score
        global perdu
        if a[pacman[1]-1][pacman[0]]!=1:
                if a[pacman[1]-1][pacman[0]]==3:
                        Fin()
                else :
                    Zone.delete(all)
                    a[pacman[1]][pacman[0]]=0
                    pacman[1] -= 1
                    a[pacman[1]][pacman[0]]=2
                    colorie_quadrillage()
                    score=score+100

         
def bas(evt):#s'active quand on clique sur bas
        global pacman
        global a
        global score
        global perdu
        if a[pacman[1]+1][pacman[0]]!=1:
                if a[pacman[1]+1][pacman[0]]==3:
                        Fin()
                else :
                    Zone.delete(all)
                    a[pacman[1]][pacman[0]]=0
                    pacman[1] += 1
                    a[pacman[1]][pacman[0]]=2
                    colorie_quadrillage()
                    score=score+100
def droite(evt): #s'active quand on clique sur droite
        global pacman
        global a
        global score
        global perdu
        if a[pacman[1]][pacman[0]+1]!=1:
                if a[pacman[1]][pacman[0]+1]==3:
                        Fin()
                else :
                    Zone.delete(all)
                    a[pacman[1]][pacman[0]]=0
                    pacman[0] += 1
                    a[pacman[1]][pacman[0]]=2
                    colorie_quadrillage()
                    score=score+100
  
  
def gauche(evt): #s'active quand on clique sur gauche
        global pacman
        global a
        global perdu
        global score
        if a[pacman[1]][pacman[0]-1]!=1:
                if a[pacman[1]][pacman[0]-1]==3:
                        Fin()
                else :
                    Zone.delete(all)
                    a[pacman[1]][pacman[0]]=0
                    pacman[0] -= 1
                    a[pacman[1]][pacman[0]]=2
                    colorie_quadrillage()
                    score=score+100
  
 
def Jeu(): #execution du jeu
        global Fenêtre, nb_ligne, nb_colonne, largeur_case, hauteur_case, img
        global Largeur, Hauteur, Couleur, Zone, fantome
        Fenêtre = Tk()
        nb_ligne = len(a)
        nb_colonne = len(a[0])
        image = Image.open("Images/pacman.gif")
        img = ImageTk.PhotoImage(image)
        largeur_case = carre
        hauteur_case = carre
        Largeur = carre*nb_colonne
        Hauteur = carre*nb_ligne
        Couleur = "white"
        Zone = Canvas(Fenêtre, width=Largeur, height=Hauteur, background=Couleur)
        colorie_quadrillage()
        Zone.bind_all('<Up>', haut)
        Zone.bind_all('<Right>', droite)
        Zone.bind_all('<Left>', gauche)
        Zone.bind_all('<Down>',bas)
        fantome = Fantome(0)
        fantome.start()
        Fenêtre.mainloop()
  
                   
if __name__=="__main__":
        Jeu()
