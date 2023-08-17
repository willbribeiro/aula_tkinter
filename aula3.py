# importação do módulo tkinter
import tkinter as tk

# atribuindo a classe principal que retorna a instância da janela principal à variável janela
janela = tk.Tk()

# título da janela
janela.title("Janela principal")

# altera o plano de fundo da janela
# a partir da alteração da chave "bg" ou "background" do dicionário janela
janela["bg"] = "green"

# alterar o tamanho da janela a partir da função geometry
# largura x altura + definir a instância a partir da esquerda da tela + distância do topo da tela (sem espaços; unidade em pixels)
janela.geometry("800x300+100+100") 

# função mainloop seria um laço de repetição enquanto a janela é exibida
# ou seja, interrompe a execução do script enquanto a janela é exibida
janela.mainloop()
