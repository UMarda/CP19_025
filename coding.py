#examplecoding.
import tkinter as tk
from tkinter import messagebox as mb

def clickf():
    print("Button clicked ")
    mb.showinfo("My name","My message")
root = tk.Tk()
root.title("testing program")
root.geometry("640x480")
b1=tk.Button(root,text="click",command=clickf)
b1.pack()

root.mainloop()
