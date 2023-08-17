#### propriedade anchor do gerenciador de layout Pack -> segue a rosa dos ventos #####

from tkinter import *

janela = Tk()

lb1 = Label(janela, text="SIDE 1", bg="white")
lb2 = Label(janela, text="SIDE 2", bg="red")
lb3 = Label(janela, text="ANCHOR 1", bg="white")
lb4 = Label(janela, text="ANCHOR 2", bg="red")

# propriedade side coloca o componente no canto e reserva todo o campo para o componente
# omitir a propriedade side é colocar os componentes em side="top"
# propriedade anchor os componentes estarão alinhados o mais oeste (neste caso) possível
lb1.pack(side="left")
lb2.pack(side="left")
lb3.pack(side="left", anchor="nw")
lb4.pack(side="left", anchor="sw")

janela["bg"] = "black"

janela.geometry("400x300+200+200")
janela.mainloop()