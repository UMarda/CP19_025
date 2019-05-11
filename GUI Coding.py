#GUICODING
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import Frame 
from tkinter import scrolledtext
def f1():

    print('button click ')

    mb.showinfo('first text','correct')

def f2():

    print('button click ')

    mb.showinfo('second text','incorrect')
root=tk.Tk()
form=Frame()
form.grid()
root.title('Talking Bot')
root.geometry('500x350')
root.resizable(width=False, height=False)
root.configure(bg='light blue')
b1=tk.Button(root,text='enter text',command=f1,fg='red',bg='purple',height='2',width='10')
b1.grid(row=0,column=1, padx=20, pady=50)
b2=tk.Button(root,text='submit text',fg='blue',bg='pink',height='2',width='10')
b2.grid(row=1,column=1, padx=20, pady=50)
txt1 = scrolledtext.ScrolledText(root,width=30,height=1,bg='grey',fg='purple')
txt1.grid(column=0,row=0)
txt2 = scrolledtext.ScrolledText(root,width=30,height=1,bg='grey',fg='pink')
txt2.grid(column=0,row=1)

root.mainloop()