#### capturando e processando valores ####

from tkinter import *

def soma():
    if(str(entrada1.get()).isnumeric() and str(entrada2.get()).isnumeric()):
        num1 = int(entrada1.get())
        num2 = int(entrada2.get())
        lb["text"] = num1 + num2
    else:
        lb["text"] = "Valores inválidos (NaN)"

janela = Tk()
janela.geometry("400x300+200+200")

entrada1 = Entry(janela)
entrada1.place(x=100, y=100)

entrada2 = Entry(janela)
entrada2.place(x=100, y=130)

botao = Button(janela, width=20, text="Soma", command=soma)
botao.place(x=100, y=150)

lb = Label(janela, text="Label1")
lb.place(x=100, y=200)

janela.mainloop()