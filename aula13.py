#### propriedade fill para ocupar toda a área designada, ou seja, a área que o objeto se expandirá #####

from tkinter import *

janela = Tk()

lb1 = Label(janela, text="Label 1", bg="red")
lb2 = Label(janela, text="", bg="yellow")
lb3 = Label(janela, text="", bg="blue")

lb1.pack(side=TOP, fill=X)
lb2.pack(side=LEFT, fill=Y)
lb3.pack(side=RIGHT, fill=Y)

janela.geometry("500x200+600+200")
janela.mainloop()