import tkinter
import random
import mysql.connector
import pandas as pd

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

global player
global pc
global rounds
global playerScore
global pcScore
global fullScoreData

playerScore = 0
pcScore = 0
rounds = 5
fullScoreData = ["", "", "", "", ""]

connection = mysql.connector.connect(
        user="root", password="root", host="localhost", port="3306", database="db"
    )

cursor = connection.cursor()

# games history
def lastGamesList():
    """
    global tree
    historyWindow = Tk()
    historyWindow.title("Last Games")
    historyWindow.geometry("600x300")
    
    tree = ttk.Treeview(historyWindow)
    tree["show"] = "headings"

    tree["columns"] = ("RoundOne", "RoundTwo", "RoundThree", "RoundFour", "RoundFive", "OverallResult")

    tree.column("RoundOne", width=50, minwidth=50, anchor=CENTER)
    tree.column("RoundTwo", width=50, minwidth=50, anchor=CENTER)
    tree.column("RoundThree", width=50, minwidth=50, anchor=CENTER)
    tree.column("RoundFour", width=50, minwidth=50, anchor=CENTER)
    tree.column("RoundFive", width=50, minwidth=50, anchor=CENTER)
    tree.column("OverallResult", width=50, minwidth=50, anchor=CENTER)

    tree.heading("RoundOne", text="Round One", anchor=CENTER)
    tree.heading("RoundTwo", text="Round Two", anchor=CENTER)
    tree.heading("RoundThree", text="Round Three", anchor=CENTER)
    tree.heading("RoundFour", text="Round Four", anchor=CENTER)
    tree.heading("RoundFive", text="Round Five", anchor=CENTER)
    tree.heading("OverallResult", text="Overall Result", anchor=CENTER)

    cursor.execute("SELECT * FROM games")
    queryResponse = cursor.fetchall()
    print(queryResponse)

    i = 0
    for row in queryResponse:
        tree.insert('', i, text="", values=(row[0],row[1],row[2],row[3],row[4],row[5]))
        i += 1
    historyWindow.mainloop()
    """
    cursor.execute("SELECT * FROM games")
    queryResponse = cursor.fetchall()
    print(pd.DataFrame(queryResponse))

# colorsHex --------------------------------
white = "#FFFFFF"  # white / branca
black = "#333333"  # black / preta
orange = "#fcc058"  # orange / laranja
yellow = "#fff873"  # yellow / amarela
green = "#34eb3d"   # green / verde
red = "#e85151"   # red / vermelha
background = "#3b3b3b"

# Window Configuration
window = Tk()
window.title("game")
window.geometry("260x280")
window.configure(bg=background)

# Windos frames + styles
frame_top = Frame(window, width=260, height=100, bg=black, relief="raised")
frame_top.grid(row=0, column=0, sticky=NW)

frame_bottom = Frame(window, width=260, height=300, bg=white, relief="flat")
frame_bottom.grid(row=1, column=0, sticky=NW)

style = ttk.Style(window)
style.theme_use("clam")

# Score Labels
playerIdentifyLabel = Label(frame_top, text="You", height=1, anchor="center", font=("Ivy 10 bold"), bg=black, fg=white)
playerIdentifyLabel.place(x=25, y=70)

playerWinLabel = Label(frame_top, text="", height=10, anchor="center", font=("Ivy 10 bold"), bg=white, fg=white)
playerWinLabel.place(x=0, y=0)

playerScoreLabel = Label(frame_top, text="0", height=1, anchor="center", font=("Ivy 30 bold"), bg=black, fg=white)
playerScoreLabel.place(x=50, y=20)

scoreSplitLabel = Label(frame_top, text=":", height=1, anchor="center", font=("Ivy 30 bold"), bg=black, fg=white)
scoreSplitLabel.place(x=125, y=20)

pcScoreLabel = Label(frame_top, text="0", height=1, anchor="center", font=("Ivy 30 bold"), bg=black, fg=white)
pcScoreLabel.place(x=200, y=20)

pcIdentifyLabel = Label(frame_top, text="PC", height=1, anchor="center", font=("Ivy 10 bold"), bg=black, fg=white)
pcIdentifyLabel.place(x=205, y=70)

pcWinLabel = Label(frame_top, text="", height=10, anchor="center", font=("Ivy 10 bold"), bg=white, fg=white)
pcWinLabel.place(x=255, y=0)

tieLabel = Label(frame_top, text="", width=255, anchor="center", font=("Ivy 10 bold"), bg=white, fg=white)
tieLabel.place(x=0, y=95)

pcChoose = Label(frame_bottom, text="", height=1, anchor="center", font=("Ivy 10 bold"), bg=white, fg=white)
pcChoose.place(x=190, y=10)

lastGamesIcon = Image.open("Assets/lastGames.png")
lastGamesIcon.resize((26,26), Image.ANTIALIAS)
lastGamesIcon = ImageTk.PhotoImage(lastGamesIcon)
buttonlastGames = Button(frame_bottom, command=lastGamesList, width=50, image=lastGamesIcon, compound=CENTER, bg=yellow, fg=white, font=("Ivi 10 bold"), anchor=CENTER, relief="flat")
buttonlastGames.place(x=15, y=120)

result = Label(frame_bottom, text="", height=1, anchor="center", font=("Ivy 40 bold"), bg=white, fg=white)
result.place(x=100, y=60)

# game over function
def gameOver():
    global playerScore
    global pcScore
    global fullScoreData

    buttonRock.destroy()
    buttonPaper.destroy()
    buttonScissor.destroy()

    if pcScore > playerScore:
        result["text"] = "LOSE"
        result["fg"] = red
    else:
        result["text"] = "WIN"
        result["fg"] = green
    
    # mySql connection

    query = f'INSERT INTO games (RoundOneResult, RoundTwoResult, RoundThreeResult, RoundFourResult, RoundFiveResult, OverallResult) VALUES ("{fullScoreData[0]}", "{fullScoreData[1]}", "{fullScoreData[2]}", "{fullScoreData[3]}", "{fullScoreData[4]}", {playerScore>pcScore})'

    cursor.execute("use db;")
    cursor.execute(query)
    cursor.execute("SELECT * from db.games")
    selectResult = cursor.fetchall()
    print(selectResult)
    connection.commit()

# game rules function
def gameRule(choose):
    global rounds
    global playerScore
    global pcScore

    playerWinLabel["bg"] = white
    tieLabel["bg"] = white
    pcWinLabel["bg"] = white

    if rounds>=0:
        optionPlays = ["rock", "paper", "scissor"]

        pc = random.choice(optionPlays)
        pcChoose['text'] = pc
        pcChoose["fg"] = black

        you = optionPlays[choose]

        match you:
            case "rock":
                if pc == "paper":
                    pcScore += 1
                    pcWinLabel["bg"] = red
                    fullScoreData[5-rounds] = "LOSE"
                elif pc == "scissor":
                    playerScore += 1
                    playerWinLabel["bg"] = green
                    fullScoreData[5-rounds] = "WIN"
                else:
                    tieLabel["bg"] = yellow
                    fullScoreData[5-rounds] = "TIE"
            case "paper":
                if pc == "scissor":
                    pcScore += 1
                    pcWinLabel["bg"] = red
                    fullScoreData[5-rounds] = "LOSE"
                elif pc == "rock":
                    playerScore += 1
                    playerWinLabel["bg"] = green
                    fullScoreData[5-rounds] = "WIN"

                else:
                    tieLabel["bg"] = yellow
                    fullScoreData[5-rounds] = "TIE"
            case "scissor":
                if pc == "rock":
                    pcScore += 1
                    pcWinLabel["bg"] = red
                    fullScoreData[5-rounds] = "LOSE"
                elif pc == "paper":
                    playerScore += 1
                    playerWinLabel["bg"] = green
                    fullScoreData[5-rounds] = "WIN"
                else:
                    tieLabel["bg"] = yellow
                    fullScoreData[5-rounds] = "TIE"

        pcScoreLabel["text"] = pcScore
        playerScoreLabel["text"] = playerScore
        rounds-=1
        if rounds == 0:
            gameOver()

# game start function
def startGame():
    global rockIcon
    global paperIcon
    global scissorIcon
    global buttonRock
    global buttonPaper
    global buttonScissor
    global rounds
    global playerScore
    global pcScore

    playerScore = 0
    pcScore = 0
    rounds = 5

    result["text"] = ""

    rockIcon = Image.open("Assets/rock.png")
    paperIcon = Image.open("Assets/paper.png")
    scissorIcon = Image.open("Assets/scissor.png")

    rockIcon.resize((50,50), Image.ANTIALIAS)
    rockIcon = ImageTk.PhotoImage(rockIcon)

    paperIcon.resize((50,50), Image.ANTIALIAS)
    paperIcon = ImageTk.PhotoImage(paperIcon)

    scissorIcon.resize((50,50), Image.ANTIALIAS)
    scissorIcon = ImageTk.PhotoImage(scissorIcon)

    buttonRock = Button(frame_bottom, command=lambda: gameRule(0), width=50, image=rockIcon, compound=CENTER, bg=white, fg=white, font=("Ivi 10 bold"), anchor=CENTER, relief="flat")
    buttonRock.place(x=40, y=60)

    buttonPaper = Button(frame_bottom, command=lambda: gameRule(1), width=50, image=paperIcon, compound=CENTER, bg=white, fg=white, font=("Ivi 10 bold"), anchor=CENTER, relief="flat")
    buttonPaper.place(x=105, y=60)

    buttonScissor = Button(frame_bottom, command=lambda: gameRule(2), width=50, image=scissorIcon, compound=CENTER, bg=white, fg=white, font=("Ivi 10 bold"), anchor=CENTER, relief="flat")
    buttonScissor.place(x=165, y=60)


buttonPlay = Button(frame_bottom, command=startGame, width=30, text="Play", bg=background, fg=white, font=("Ivi 10 bold"), anchor=CENTER, relief="flat")
buttonPlay.place(x=5, y=151)

window.mainloop()