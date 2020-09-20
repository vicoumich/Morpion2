from tkinter import*
from time import sleep
from random import randint

#Création du tableau qui servira de support de jeu


class Morpion_pvb():
    def __init__(self, x, y):
        self.tableau = []
        self.used = []
        self.x = x
        self.y = y
        self.count = 0
        self.pos_tab_x = 999
        self.pos_tab_y = 999
        
    def parametrage(self, x, y):
        for a in range(y):
            self.tableau.append([])
            for b in range(x):
                self.tableau[a].append(0)
        global pos_tab_x
        global pos_tab_y
        pos_tab_x,pos_tab_y = 999, 999
        self.count = 0

    def clic(self, event):
        croix = croix_115x115
        cercle = cercle_115x115
        if self.x < 5 and self.y < 5:
            croix = croix_150x150
            cercle = cercle_150x150

        
        self.pos_tab_x, self.pos_tab_y = event.y // (dimension ), event.x // (dimension) #Position de la croix dans la liste tableau


        if self.pos_tab_x == self.y:
            print("oui")
            self.pos_tab_x -= 1
             
        if self.pos_tab_y == self.x:
            print("oui2")
            self.pos_tab_y -= 1


        if self.count < self.x * self.y and  (self.pos_tab_x, self.pos_tab_y) not in self.used and self.count % 2 == 0:
            pos_x,pos_y = dimension / 2 + self.pos_tab_x * dimension, dimension / 2 + self.pos_tab_y * dimension   #Position sur la grille    
            grille.create_image((pos_y,pos_x), image = croix)
            print(self.pos_tab_x, self.pos_tab_y)
            Player._placer_(self.pos_tab_x, self.pos_tab_y)
            
            if Player.bigue_verif(self.pos_tab_x, self.pos_tab_y) == Player.numero:
                result.configure(text = "Le joueur 1 a gagné, bravo!", fg = "green")
                self.count = 100
        

        if self.count < self.x * self.y and  (self.pos_tab_x, self.pos_tab_y) not in self.used and self.count % 2 == 1:
            pos_x,pos_y = dimension / 2 + self.pos_tab_x * dimension, dimension / 2 + self.pos_tab_y * dimension   #Position sur la grille    
            grille.create_image((pos_y,pos_x), image = cercle)
            print(self.pos_tab_x, self.pos_tab_y)
            Player2._placer_(self.pos_tab_x, self.pos_tab_y)
            
            if Player2.bigue_verif(self.pos_tab_x, self.pos_tab_y) == Player2.numero:
                result.configure(text = "Le joueur 2 a gagné, bravo!", fg = "green")
                self.count = 100


            
# Fonction de la partie
    def _partie_(self, x, y):
        global Player
        global Player2
        self.parametrage(x, y)
        Player = joueur(1)
        Player2 = joueur(2)                                                  
        #Boucle de la partie
        grille.bind("<Button>", self.clic)
        
    
############################################################
##########     CREATION DU TABLEAU DU MORPION     ##########
############################################################
    def start_pvb(self):
        global dimension
        
        #Partie si le tableau fais moins de 5 case de sur la longueur ou la largeur
        if self.x < 5 and self.y < 5:
            dimension = 155
            larg = dimension*self.x
            longu = dimension*self.y
            X0 = Y0 = dimension / 2
            global grille
            global result
            grille = Canvas(p_v_b, background="#292727",
                            width=larg, height=longu)
            result = Label (p_v_b, bg = "#292727", text = "", 
                            font = ("Press start 2p",15), fg = "red")
            for i in range(self.x):
                new = X0 + i*dimension
                centre = (new, Y0)
                for c in range(self.y):
                    centre = (new, Y0 + c*dimension)
                    grille.create_image(centre, image=_white_150x150)
                    
                   
            #Fin de la configuration de la grille
            grille.pack(pady=50)
            result.pack()

            #debut de la partie
            self._partie_(self.x, self.y)

        #Création du tableau si le tableau fais plus de 4 case de sur la longueur ou la largeur
        else:
            dimension = 120
            larg = dimension*self.x
            longu = dimension*self.y

            X0 = Y0 = dimension / 2
            grille = Canvas(p_v_b, background="#292727",
                               width=larg, height=longu)
            result = Label (p_v_b, bg = "#292727", text = "", 
                               font = ("Press start 2p",15), fg = "red")

            for i in range(self.x):
                new = X0 + i*dimension
                centre = (new, Y0)
                for c in range(self.y):
                    centre = (new, Y0 + c*dimension)
                    grille.create_image(centre, image=_white_115x115)
            #Fin de la configuration de la grille

            grille.pack(pady=50)
            result.pack()
            #debut de la partie
            self._partie_(self.x, self.y)
############################################################
#######################     FIN     ########################
############################################################

class joueur ():
    def __init__(self,numero):
        self.numero = numero
        
    def _placer_(self,x,y):
        Morpion_1.tableau[x][y] = self.numero
        Morpion_1.count += 1
        Morpion_1.used.append((x,y))
    def verif_ligne_1 (self,x,y):
        try:
            for z in range(1,3):
                if Morpion_1.tableau[x+1][y] == self.numero and x + 1 >= 0 and y >= 0:
                    if Morpion_1.tableau[x+2][y] == self.numero and x + 2 >= 0 and y >= 0:
                        return self.numero
                    else:
                        return 0
                else:
                    return 0
        except:
            return 0
    def verif_ligne_2 (self,x,y):
        try:
            
            if Morpion_1.tableau[x-1][y] == self.numero and x - 1 >= 0 and y >= 0:
                if Morpion_1.tableau[x-2][y] == self.numero and x - 2 >= 0 and y >= 0:
                    return self.numero
                else:
                    return 0
            else:
                return 0
        except:
            return 0
    def verif_ligne_3 (self,x,y):
        try:
            if Morpion_1.tableau[x-1][y] == self.numero and x - 1 >= 0 and y >= 0:
                if Morpion_1.tableau[x+1][y] == self.numero and x + 1 >= 0 and y >= 0:
                    return self.numero
                else:
                    return 0
            else:
                return 0
        except:
            return 0
    def verif_colonne_1(self,x,y):
        try:
            
            if Morpion_1.tableau[x][y-1] == self.numero and x >= 0 and y - 1 >= 0:
                if Morpion_1.tableau[x][y-2] == self.numero and x >= 0 and y - 2 >= 0:
                    return self.numero
                else:
                    return 0
            else:
                return 0
        except:
            return 0 
    def verif_colonne_2 (self,x,y):
        try:
        
            if Morpion_1.tableau[x][y+1] == self.numero and x >= 0 and y + 1 >= 0:
                if Morpion_1.tableau[x][y+2] == self.numero and x >= 0 and y + 2 >= 0:
                    return self.numero
                else:
                    return 0
            else:
                return 0
        except:
            return 0
    def verif_colonne_3 (self,x,y):
        try:
            if Morpion_1.tableau[x][y-1] == self.numero and x >= 0 and y - 1 >= 0:
                if Morpion_1.tableau[x][y+1] == self.numero and x >= 0 and y + 1 >= 0:
                    return self.numero
                else:
                    return 0
            else:
                return 0
        except:
            return 0
    def verif_diagonale_1 (self,x,y):
        try:
        
            if Morpion_1.tableau[x-1][y-1] == self.numero and x - 1 >= 0 and y - 1 >= 0:
                if Morpion_1.tableau[x-2][y-2] == self.numero and x - 2 >= 0 and y - 2 >= 0:
                    return self.numero
                else:
                    return 0
            else:
                return 0
        except:
            return 0
    def verif_diagonale_2 (self,x,y):
        try:

            if Morpion_1.tableau[x+1][y+1] == self.numero and x + 1 >= 0 and y + 1 >= 0:
                if Morpion_1.tableau[x+2][y+2] == self.numero and x + 2 >= 0 and y + 2 >= 0:
                    return self.numero
                else:
                    return 0
            else:
                return 0
        except:
            return 0   
    def verif_diagonale_3 (self,x,y):
        try:

            if Morpion_1.tableau[x+1][y-1] == self.numero and x + 1 >= 0 and y - 1 >= 0:
                if Morpion_1.tableau[x+2][y-2] == self.numero and x + 2 >= 0 and y - 2 >= 0:
                    return self.numero
                else:
                    return 0
            else:
                return 0
        except:
            return 0  
    def verif_diagonale_4 (self,x,y):
        try:

            if Morpion_1.tableau[x-1][y+1] == self.numero and x - 1 >= 0 and y + 1 >= 0:
                if Morpion_1.tableau[x-2][y+2] == self.numero and x - 2 >= 0 and y + 2 >= 0:
                    return self.numero
                else:
                    return 0
            else:
                return 0
        except:
            return 0 
    def verif_diagonale_5 (self,x,y):
        try:
            if Morpion_1.tableau[x-1][y-1] == self.numero and x - 1 >= 0 and y - 1 >= 0:
                if Morpion_1.tableau[x+1][y+1] == self.numero and x + 1 >= 0 and y + 1 >= 0:
                    return self.numero
                else:
                    return 0
            else:
                return 0
        except:
            return 0
    def verif_diagonale_6 (self,x,y):
        try:
            if Morpion_1.tableau[x+1][y-1] == self.numero and x + 1 >= 0 and y - 1 >= 0:
                if Morpion_1.tableau[x-1][y+1] == self.numero and x - 1 >= 0 and y + 1 >= 0:
                    return self.numero
                else:
                    return 0
            else:
                return 0
        except:
            return 0
    def bigue_verif(self,x,y):
        liste_verif = [
            self.verif_ligne_1(x,y), self.verif_ligne_2(x,y), self.verif_ligne_3(x,y), 
            self.verif_colonne_1(x,y), self.verif_colonne_2(x,y), self.verif_colonne_3(x,y), 
            self.verif_diagonale_1(x,y), self.verif_diagonale_2(x,y), self.verif_diagonale_3(x,y), 
            self.verif_diagonale_4(x,y), self.verif_diagonale_5(x,y), self.verif_diagonale_6(x,y)
            ]
        
        if self.numero in liste_verif:
            print(liste_verif)
            return self.numero
        else: 
            return 0




def start_game():
    x = champ_longueur.get()
    y = champ_largeur.get()
    global Morpion_1
    try:
        x = int(x)
        y = int(y)
        if (x <= 2 and y <= 2) or (x > 6 and y > 6) or x <= 2 or y <= 2 or x > 6 or y > 6:
            explain4.configure(fg="red")
            return 0
    except:
        explain1.configure(
                text="Vous devez impérativement remplir \n le champ avec des valeurs entre ")
        return 0
    frame1.pack_forget()
    Morpion_1 = Morpion_pvb(x, y)
    Morpion_1.start_pvb()





p_v_b = Tk()  # Création de la fenêtre

croix_150x150 = PhotoImage(file="./image/croix_150x150.png")
cercle_150x150 = PhotoImage(file="./image/cercle_150x150.png")
_white_150x150 = PhotoImage(file="./image/white_150x150.png")
croix_115x115 = PhotoImage(file="./image/croix_115x115.png")
cercle_115x115 = PhotoImage(file="./image/cercle_115x115.png")
_white_115x115 = PhotoImage(file="./image/white_115x115.png")

p_v_b.title('Player VS Player')
p_v_b.geometry("1000x900")
p_v_b.minsize(720, 480)
p_v_b.configure(background="#292727")

#Avant partie
frame1 = Frame(p_v_b, bg="#292727")
titre = Label(frame1, text="Player VS Player", font=(
    "Press start 2p", 23), fg="#1BD6F1", bg='#292727')
explain1 = Label(frame1, bg='#292727', text="Veuillez cliquer sur start après avoir rempli \n le champ par de valeur entre ",
                 fg="#1BD6F1", font=("Arial", 30))
explain4 = Label(frame1, bg='#292727', text="3 et 6 compris",
                 fg="#1BD6F1", font=("Arial", 30))
champ_longueur = Entry(frame1, bg="#A6E7BC", width=10)
champ_largeur = Entry(frame1, bg="#A6E7BC", width=10)
explain2 = Label(frame1, bg='#292727',
                 text="Longueur du Morpion:", fg="white", font=("Arial", 20))
explain3 = Label(frame1, bg='#292727', text="Largeur du Morpion:",
                 fg="white", font=("Arial", 20))
pvb_start = Button(frame1, bg="#FFFFED", text="Start", font=(
    "Press start 2p", 20), fg="black", height=3, width=25, command=start_game)
charge_fake = Label(frame1, bg="#292727", text="",
                    fg="white", font=("Press start 2p", 30))
titre.pack(pady=30)
explain1.pack()
explain4.pack()
explain2.pack(pady=20)
champ_largeur.pack(pady=10)
explain3.pack(pady=20)
champ_longueur.pack()
pvb_start.pack(pady=100)
charge_fake.pack()
frame1.pack()

#Début de partie


p_v_b.mainloop()
