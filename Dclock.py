from tkinter import*
from time import strftime

root=Tk()


root.resizable(0, 0)
root.title("Python Digital Clock")
Label.pack()


Label = Label(root, font=('calibri', 40,'bold'),bg='blue')
Label.pack()

root.geometry("500*100")

def Dclock():
    string=strftime('%I:%M:%S:%P')
    Label.config(text=string)
    Label.after(1000,Dclock)

Dclock()

root.mainloop()
