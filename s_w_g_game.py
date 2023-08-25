from tkinter import *
from functools import partial
import random
import time
import tkinter.messagebox as tmsg

yourscore = 0
computerscore = 0
turns = 0

def titleblock():
    topp = Frame(root, bg='black', padx=30, pady=15)
    intro = Label(topp, text="SNAKE WATER GUN", font=('algerian', 32, 'bold'), padx=25, pady=10, fg='red', bg='purple')
    topp.pack()
    intro.pack()

def exe():
    global yourscore, val3, l
    f = open('snake_w_g.txt', 'r')
    x = f.read().split()
    f.close()
    value = tmsg.askquestion('Quitting', 'Do you really want to quit this game?')
    if value=='yes':
        if yourscore/turns>int(x[0])/int(x[2]):
            f = open('snake_w_g.txt', 'w')
            f.write(f"{yourscore} {computerscore} {turns}")
            f.close()
            val3.set(f'HIGHEST SCORE : {x}')
            l.update()
        quit()
    else:
        pass


def buttonblock():
    f = Frame(root, padx=50, pady=10, bg='white')
    b1 = Button(f, text='SNAKE', padx=10, pady=10, command=partial(action, 0), font=('mangal', 18, 'bold'), bg='pink', activebackground='green', activeforeground='orange')
    b2 = Button(f, text='WATER', padx=10, pady=10, command=partial(action, 1), font=('mangal', 18, 'bold'), bg='pink', activebackground='green', activeforeground='orange')
    b3 = Button(f, text='GUN', padx=10, pady=10, command=partial(action, 2), font=('mangal', 18, 'bold'), bg='pink', activebackground='green', activeforeground='orange')
    b4 = Button(f, text="EXIT", padx=10, pady=10,command=exe, font=('mangal', 18, 'bold'), bg='pink', activebackground='green', activeforeground='orange')
    f.pack(pady=25)
    b1.pack(side=LEFT, padx=30, pady=20)
    b2.pack(side=LEFT, padx=30, pady=20)
    b3.pack(side=LEFT, padx=30, pady=20)
    b4.pack(side=LEFT, padx=30, pady=20)

def resultblock():
    global lab, val
    val = StringVar()
    val.set('Select the buttons by clicking them')
    f = Frame(root,pady=10, padx=30, bg='black')
    lab = Label(f, textvariable=val,font=('mangal', 23, 'bold'), bg='purple', fg='white')
    f.pack(fill=X, padx=25)
    lab.pack(fill=X, padx=75, pady=20)

def scoreblock():
    global val2, lab2, winner
    val2 = StringVar()
    val2.set(f'  YOUR SCORE : 0/0               COMPUTER SCORE : 0/0  ')
    f = Frame(root, pady=10, padx=30, bg='black')
    f.pack()
    lab2 = Label(f, textvariable=val2,font=('mangal', 23, 'bold'), bg='purple', fg='white')
    lab2.pack(fill=X, padx=75, pady=20)
    winner = Label(root, text='   Both are at draw   ',font=('mangal', 23, 'bold'), bg='purple', fg='white')
    winner.pack(padx=75, pady=20)


def result():
    global playerchoice, lab, computerchoice, choice, matrix, val
    val.set(f'Computer chose {choice}. Its a {matrix[playerchoice][computerchoice]} for you!')
    if matrix[playerchoice][computerchoice]=='Loss':
        lab.configure(background='red')
    elif matrix[playerchoice][computerchoice]=='Win':
        lab.configure(background='green')
    else:
        lab.configure(background='purple')
    lab.update()

def scorecard():
    global yourscore, computerscore, turns, matrix
    global playerchoice, computerchoice, choice, val2, lab2
    if matrix[playerchoice][computerchoice] == 'Win':
        yourscore = yourscore +1
    if matrix[playerchoice][computerchoice] == 'Loss':
        computerscore = computerscore +1
    turns+=1
    if yourscore>computerscore:
        string = f'  You lead Computer by {yourscore-computerscore}  '
        winner.configure(text=string, bg='green')
    if yourscore<computerscore:
        string = f'  Computer lead You by {computerscore-yourscore}  '
        winner.configure(text=string, bg='red')
    if yourscore==computerscore:
        string = '   Both are at draw   '
        winner.configure(text=string, bg='purple')
    val2.set(f'  YOUR SCORE : {yourscore}/{turns}              COMPUTER SCORE : {computerscore}/{turns}  ')
    lab2.update()

def Highscoreblock():
    global val3, l
    f = open('snake_w_g.txt', 'r')
    x = f.read()
    f.close()
    val3 = StringVar()
    val3.set(f'HIGHEST SCORE : {x}')
    f = Frame(root, pady=10, padx=30, bg='black')
    f.pack()
    l = Label(f, textvariable=val3, font=('mangal', 23, 'bold'), bg='purple', fg='white')
    l.pack(fill=X, padx=75, pady=10)

def action(var):
    global playerchoice, computerchoice, choice, matrix
    playerchoice = var
    computerchoice = random.randint(0, 2)
    if computerchoice==0:
        choice = 'snake'
    elif computerchoice==1:
        choice = 'water'
    else:
        choice = 'gun'
    matrix = [['Draw', 'Win', 'Loss'], ['Loss', 'Draw', 'Win'], ['Win', 'Loss', 'Draw']]
    result()
    scorecard()

if __name__=='__main__':
    root = Tk()
    root.title('Snake Water Gun')
    root.wm_iconbitmap("games.ico")
    root.configure(background='black')
    root.geometry('1170x557')
    titleblock()
    Highscoreblock()
    scoreblock()
    buttonblock()
    resultblock()
    root.mainloop()
