import tkinter as tk
from tkinter import messagebox
import sqlite3

def abrir_janela_edicao(produto):
    # Criar a janela de edição do produto
    janela_edicao = tk.Toplevel()
    janela_edicao.title("Editar Produto")
    janela_edicao.geometry("300x200")

    # Criar os widgets da janela de edição
    # Exemplo: labels, entrys, botão de salvar, etc.
    # Você pode criar os widgets necessários para editar os campos do produto

    # Exemplo: Criar uma label e entry para o campo "nome"
    nome_label = tk.Label(janela_edicao, text="Nome:")
    nome_entry = tk.Entry(janela_edicao)
    nome_entry.insert(tk.END, produto[2])  # Preencher a entry com o valor atual do campo "nome"

    # Exemplo: Criar um botão de salvar
    salvar_button = tk.Button(janela_edicao, text="Salvar", command=lambda: salvar_edicao(produto[0], nome_entry.get()))

    # Posicionar os widgets na janela de edição
    # Exemplo: Utilize grid, pack ou place para posicionar os widgets conforme necessário

    nome_label.grid(row=0, column=0, padx=10, pady=5)
    nome_entry.grid(row=0, column=1, padx=10, pady=5)
    salvar_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

def salvar_edicao(item_id, nome):
    # Atualizar o campo "nome" do produto no banco de dados
    conn = sqlite3.connect("produtos.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE estoque SET nome=? WHERE codigo1=?", (nome, item_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
