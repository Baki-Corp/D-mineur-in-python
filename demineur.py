import random
from tkinter import *

gameOver = False
score = 0
carre_tchek = 0

def play_dimineur():
    cree_terrainminé(terrainminé)
    fenetre = tkinter.tk()
    configuration_fenetre(fenetre)
    fenetre.mainloop()

terrainminé = []
def cree_terrainminé(terrainminé):
    global carre_tchek
    for rangée in range(0,10):
        listeRangée = []
        for colonne in range(0,10):
            if random.randit(1,100) < 20:
                listeRangée.append(1)
            else:
                listeRangée.append(0)
                carre_tchek = carre_tchek + 1
        terrainminé.append(listeRangée)



def printTerrain(terrainminé):
    for listeRangée in terrainminé:
        print(listeRangée)



def configuration_fenetre(fenetre):
    for numéroRangée, listeRangée in enumerate(listeRangée):
        if random.randit(1,100) < 25:
            carré = tkinter.Label(fenetre, text="   ", bg = "darkgreen")
        elif random.randit(1,100) > 75:
            carré = tkinter.Label(fenetre, text="   ", bg = "seagreen")
        else:
            carré = tkinter.Label(fenetre, text="   ", bg = "green")
        carré.grid(row = numéroRangée, column = numéroColonne)
        carré.bind("<button-1>", quand_cliqué)


def quand_cliqué(event):
    global score
    global gameOver
    global carre_tchek
    carré = event.widget
    rangée = int(carré.grid_info()["row"])
    colonne = int(carré.grid_info()("column"))
    texteActuel = carré.cget("text")


    if terrainminé[rangée][colonne] == 1:
        gameOver = True
        carré.config(bg = "red")
        print("Game Over, tu as marché sur une mine")
        print("Ton score est de : ", score)

    elif texteActuel == "   ":
        carré.config(bg = "brown")
        totalBombes = 0

        if rangée < 9:

            if terrainminé[rangée+1][colonne] == 1:
                totalBombes = totalBombes + 1

        if rangée > 0:

            if terrainminé[rangée-1][colonne] == 1:
                totalBombes = totalBombes + 1
        
        if colonne > 0:

            if terrainminé[rangée][colonne-1] == 1:
                totalBombes = totalBombes + 1
        
        if colonne < 9:

            if terrainminé[rangée][colonne+1] == 1:
                totalBombes = totalBombes + 1
        
        if rangée > 0 and colonne > 0:

            if terrainminé[rangée-1][colonne-1]:
                totalBombes = totalBombes +1
        
        if rangée < 9 and colonne > 0:

            if terrainminé[rangée+1][colonne-1] == 1:
                totalBombes = totalBombes + 1
        
        if rangée < 9 and colonne > 0:

            if terrainminé[rangée-1][colonne+1] == 1:
                totalBombes = totalBombes + 1
        
        if rangée < 9 and colonne < 9:

            if terrainminé[rangée+1][colonne+1] == 1:
                totalBombes = totalBombes + 1
        
        carré.config(text = " " + str(totalBombes) + " ")
        carre_tchek = carre_tchek - 1
        score = score + 1
        
        if carre_tchek == 0:
            gameOver = True
            print("Bien joué tu as gagné !")
            print("Ton score est de : ", score)

    play_demineur()
            