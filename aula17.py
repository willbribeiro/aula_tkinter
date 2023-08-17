#### tela de login e senha #####
from tkinter import *

# janela principal
janela = Tk()

# componentes
lb1 = Label(janela, text="Login: ")
lb2 = Label(janela, text="Senha: ")

entrada1 = Entry(janela)
entrada2 = Entry(janela)

botao = Button(janela, text="Confirmar")

# gerenciador de layout grid
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
entrada1.grid(row=0, column=1)
entrada2.grid(row=1, column=1)
botao.grid(row=2, column=1)

janela.geometry("200x100+100+100")
janela.mainloop()