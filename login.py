import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Lógica de autenticação
    # Por exemplo, verificar se o nome de usuário e senha correspondem a um registro válido
    
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha incorretos!")

# Configurações da janela
root = tk.Tk()
root.title("Tela de Login")
root.geometry("300x200")

# Label de nome de usuário
username_label = tk.Label(root, text="Nome de Usuário:")
username_label.pack()

# Entrada de nome de usuário
username_entry = tk.Entry(root)
username_entry.pack()

# Label de senha
password_label = tk.Label(root, text="Senha:")
password_label.pack()

# Entrada de senha
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Botão de login
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()
