#### propriedade row e column do gerencidador de layout grid ####

from tkinter import *

janela = Tk()

lb1 = Label(janela, text="Label 1")
lb2 = Label(janela, text="Label 2")

lb1.grid(row=1000, column=1000)
# o lb2 será colocado uma coluna ao lado direito
lb2.grid(row=2000, column=2000)

janela.geometry("500x200+600+200")
janela.mainloop()