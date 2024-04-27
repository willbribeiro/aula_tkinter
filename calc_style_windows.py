import tkinter as tk
import math

# Função para adicionar números e operadores na tela
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Função para calcular o resultado da expressão
def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Erro")
        expression = ""

# Função para limpar a tela
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Função para calcular a raiz quadrada
def btn_sqrt():
    global expression
    try:
        result = str(math.sqrt(eval(expression)))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Erro")
        expression = ""

# Função para inverter o sinal do número
def btn_negate():
    global expression
    try:
        result = str(-eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Erro")
        expression = ""

expression = ""

root = tk.Tk()
root.title("Calculadora")

input_text = tk.StringVar()

entry = tk.Entry(root, textvariable=input_text, font=('Segoe UI', 18), bd=10, insertwidth=4, width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4)

btn_list = [
    ('√', btn_sqrt), ('C', btn_clear), ('±', btn_negate), ('/', lambda: btn_click('/')),
    ('7', lambda: btn_click('7')), ('8', lambda: btn_click('8')), ('9', lambda: btn_click('9')), ('*', lambda: btn_click('*')),
    ('4', lambda: btn_click('4')), ('5', lambda: btn_click('5')), ('6', lambda: btn_click('6')), ('-', lambda: btn_click('-')),
    ('1', lambda: btn_click('1')), ('2', lambda: btn_click('2')), ('3', lambda: btn_click('3')), ('+', lambda: btn_click('+')),
    ('0', lambda: btn_click('0')), ('.', lambda: btn_click('.')), ('=', btn_equal)
]

row_index = 1
col_index = 0

for text, command in btn_list:
    if command:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Segoe UI', 12), bd=0, command=command)
    else:
        button = tk.Label(root, text=text, padx=20, pady=20, font=('Segoe UI', 12))
    button.grid(row=row_index, column=col_index, padx=2, pady=2, sticky='nsew')
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

root.mainloop()
