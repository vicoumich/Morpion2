from tkinter import*
import time
import subprocess
import sys


def player_vs_bot():
    subprocess.call("python player_vs_bot.pyw")


def player_vs_player():
    subprocess.call("python player_vs_player.pyw")


def create():
    label_auteur.configure(text="Victor Michel")


menu = Tk()
menu.title('Morpion')
menu.geometry("1000x900")
menu.minsize(720, 480)
menu.configure(background="#292727")

titre = Label(menu, text="Bienvenue sur le jeu du morpion",
              font=("Press start 2p", 23), fg="#1BD6F1", bg='#292727')

mode_bot = Button(menu, text="Player VS Bot", bg="#626262", font=(
    'Arial', 10), height=5, width=40, command=player_vs_bot)

mode_pvp = Button(menu, text="Player VS Player", bg="#626262", font=(
    'Arial', 10), height=5, width=40, command=player_vs_player)

label_auteur = Label(menu, bg="#292727", text="",
                     fg="white", font=("Press start 2p", 12))

Auteur = Button(menu, bg="#D7D7D7", text="Voir le créateur", command=create)


titre.pack()
mode_bot.pack(pady=100)
mode_pvp.pack()
label_auteur.pack(pady=100)
Auteur.pack(side="right", pady=100, padx=50)

menu.mainloop()
