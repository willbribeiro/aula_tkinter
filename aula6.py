#### trabalhando com label e botões ####

from tkinter import *

# função para o clique do botão
def bt_click():
    print("bt_click")
    
    # Alterar o valor de texto da label
    lb["text"] = "Funcionou"

janela = Tk()
janela.geometry("300x300+200+200")

# Button(contido na janela, width=largura, text=texto, command=função invocada)
bt = Button(janela, width=20, text="OK", command=bt_click)

# posicionar o botão com o gerenciador de layout PLACE
bt.place(x=100, y=100)

# criar uma label. Label(contido na janela, text=texto)
lb = Label(janela, text="Teste")

# posicionar a label com o gerenciador de layout PLACE
lb.place(x=100, y=150)

janela.mainloop()
