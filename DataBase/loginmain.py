import tkinter as tk
from tkinter import messagebox
import sqlite3
import produtos

def verificar_login():
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE Username=? AND Password=?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        abrir_menu()
    else:
        messagebox.showerror("Login", "Usuário ou senha inválidos!")

def abrir_menu():
    # Fechar a tela de login
    login_window.destroy()

    # Criar a janela do menu
    menu_window = tk.Tk()
    menu_window.title("Menu")

    def abrir_tela_produtos():
        # Fechar a janela do menu
        menu_window.destroy()

        # Chamar a tela de produtos
        produtos.abrir_tela_produtos()

    # Criação dos botões do menu
    produtos_button = tk.Button(menu_window, text="Produtos", command=abrir_tela_produtos)

    produtos_button.pack(pady=10)

    # Inicia o loop principal do tkinter para exibir o menu
    menu_window.mainloop()

# Criação da janela de login
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x300")

# Criação dos campos de entrada para o usuário e senha
username_label = tk.Label(login_window, text="Usuário:")
username_entry = tk.Entry(login_window)
password_label = tk.Label(login_window, text="Senha:")
password_entry = tk.Entry(login_window, show="*")
login_button = tk.Button(login_window, text="Login", command=verificar_login)

username_label.pack(pady=10)
username_entry.pack(pady=5)
password_label.pack(pady=10)
password_entry.pack(pady=5)
login_button.pack(pady=10)

# Inicia o loop principal do tkinter para exibir a tela de login
login_window.mainloop()
