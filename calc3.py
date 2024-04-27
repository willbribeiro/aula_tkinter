import tkinter as tk

# Função para lidar com o clique dos botões
def btn_click(item):
    global expression
    # Concatena o texto do botão à expressão atual
    expression = expression + str(item)
    # Atualiza o texto na caixa de entrada
    input_text.set(expression)

# Função para limpar a caixa de entrada
def btn_clear():
    global expression
    # Reseta a expressão para uma string vazia
    expression = ""
    # Limpa o texto na caixa de entrada
    input_text.set("")

# Função para calcular o resultado da expressão
def btn_equal():
    global expression
    # Avalia a expressão e obtém o resultado
    result = str(eval(expression))
    # Define o resultado como texto na caixa de entrada
    input_text.set(result)
    # Reseta a expressão para uma string vazia para futuras operações
    expression = ""

# Inicialização da expressão como uma string vazia
expression = ""

# Cria uma janela Tkinter
root = tk.Tk()
# Define o título da janela
root.title("Calculadora")

# Variável para armazenar o texto na caixa de entrada
input_text = tk.StringVar()

# Cria uma caixa de entrada (Entry) para a calculadora
entry = tk.Entry(root, textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=10, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Lista dos textos dos botões da calculadora
btn_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.',  '', '+'
]

# Índices para controlar a posição dos botões na grade
row_index = 1
col_index = 0

# Loop para criar e posicionar os botões na calculadora
for btn in btn_list:
    # Cria um botão com o texto atual do loop
    tk.Button(root, text=btn, padx=20, pady=20, font=('arial', 18, 'bold'), command=lambda x=btn: btn_click(x)).grid(row=row_index, column=col_index)
    # Atualiza os índices de coluna e linha
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

# Botão para limpar a entrada
tk.Button(root, text="C", padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_clear).grid(row=5, column=0)

# Botão para calcular o resultado
tk.Button(root, text="=", padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_equal).grid(row=5, column=1)

# Inicia o loop principal da interface gráfica
root.mainloop()
