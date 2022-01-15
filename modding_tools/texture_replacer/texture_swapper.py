__author__ = "MrScott1234"
__copyright__ = "Copyright (C) 2022 MrScott1234"
__license__ = "MIT License"
__version__ = "1.0"

#import tkinter libs
import tkinter as tk
from tkinter import *
from tkinter.filedialog import *

import sys, os

program_dir = sys.path[0]
assets_path = ""

#Tkinter frame
root = tk.Tk()

#Set the window size and other properties
root.geometry("400x300")
root.title("10 Pin Shuffle Texture Swapper")
root.iconphoto(True, tk.PhotoImage(file=os.path.join(program_dir, "icon.png")))

assets_str = tk.StringVar()

def open_file():
    file = askdirectory()
    if file is not None:
        assets_path = file
        assets_str.set(file)
        print(assets_path)

btn = Button(root, text ='Open', command = lambda:open_file())
btn.pack(side = TOP, pady = 10)

Label(root, textvariable=assets_str).pack()


root.mainloop()
