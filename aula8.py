### widget entry -> para entrada de dados ####

from tkinter import *

def bt_onclick():
    lb["text"] = ed.get() # get -> pega o valor atribuido (entrada do usuário) a variável pelo Entry

janela = Tk()

# Entry(vincular a janela)
ed = Entry(janela)
ed.place(x=100, y=100)

bt = Button(janela, width=20, text="OK", command=bt_onclick)
bt.place(x=100, y=150)

lb = Label(janela, text="Label")
lb.place(x=100, y=200)

janela.geometry("300x300+300+300")
janela.mainloop()