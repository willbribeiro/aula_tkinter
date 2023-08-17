from tkinter import *
from functools import partial

def bt_click(botao):
    print(botao["text"])

janela = Tk()

bt1 = Button(janela, width=20, text="Botão 1")

# para passar os parâmetros para a função. partial(função, parâmetro). Já que não seria possível passar parâmetro só criando o botão.
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=100, y=100)

bt2 = Button(janela, width=20, text="Botão 2")
# para passar os parâmetros para a função. partial(função, parâmetro). Já que não seria possível passar parâmetro só criando o botão.
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=100, y=130)

janela.geometry("300x300+200+200")

janela.mainloop()