#### propriedade sticky do gerenciador de layout grid ####
# sentido do componente deve ter dentro da célula. Sentido da rosa dos ventos.

from tkinter import *

# janela principal
janela = Tk()

lb1 = Label(janela, text="ESPAÇO", width="15", height="3", bg="blue")
lbhorizontal = Label(janela, text="horizontal", bg="yellow")
lbvertical = Label(janela, text="vertical", bg="green")

lb1.grid(row=0, column=0)
lbhorizontal.grid(row=1, column=0, sticky=E)
lbvertical.grid(row=0, column=1, sticky=S)

janela.geometry("200x100+100+100")
janela.mainloop()
