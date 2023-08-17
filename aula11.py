#### propriedade side do gerenciador de layout Pack #####

from tkinter import *

janela = Tk()

lb1 = Label(janela, text="right", bg="white")
lb2 = Label(janela, text="bottom", bg="white")
lb3 = Label(janela, text="left", bg="white")
lb4 = Label(janela, text="top", bg="white")

lb1.pack(side="right")
lb2.pack(side="bottom")
lb3.pack(side="left")
lb4.pack(side="top")

janela["bg"] = "black"

janela.geometry("400x300+200+200")
janela.mainloop()