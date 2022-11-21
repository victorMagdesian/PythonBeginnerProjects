import tkinter
from tkinter import *
from tkinter import ttk

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

window.mainloop()