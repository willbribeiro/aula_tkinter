import tkinter as tk

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

root = tk.Tk()
root.title("Calculadora")

input_text = tk.StringVar()

entry = tk.Entry(root, textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=10, justify='right')
entry.grid(row=0, column=0, columnspan=4)

btn_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_index = 1
col_index = 0

for btn in btn_list:
    tk.Button(root, text=btn, padx=20, pady=20, font=('arial', 18, 'bold'), command=lambda x=btn: btn_click(x)).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

tk.Button(root, text="C", padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_clear).grid(row=5, column=0)

tk.Button(root, text="=", padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_equal).grid(row=5, column=1)

root.mainloop()
