#### Gerenciador de janela PLACE ####

from tkinter import *

janela = Tk()

janela.geometry("300x300+200+200")

# label(contido em, ou seja, container)
lb = Label(janela, text="Olá Mundo")

# aplicar o gerenciador de layout PLACE
lb.place(x=100, y=100)

janela.mainloop()