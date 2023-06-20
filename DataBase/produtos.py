import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from produto_edicao import abrir_janela_edicao
import sqlite3

def criar_tabela():
    conn = sqlite3.connect("produtos.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estoque (
            codigo1 INTEGER,
            codigo2 INTEGER,
            nome TEXT,
            valor REAL,
            quantidade INTEGER
        )
    """)
    conn.commit()
    conn.close()

def salvar_dados():
    codigo1 = int(codigo1_entry.get())
    codigo2 = int(codigo2_entry.get())
    nome = nome_entry.get()
    valor = float(valor_entry.get())
    quantidade = int(quantidade_entry.get())

    conn = sqlite3.connect("produtos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO estoque VALUES (?, ?, ?, ?, ?)", (codigo1, codigo2, nome, valor, quantidade))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

    # Limpar os campos de entrada após a inserção
    codigo1_entry.delete(0, tk.END)
    codigo2_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)

    # Atualizar a tabela automaticamente após a inserção
    exibir_dados()

def exibir_dados():
    conn = sqlite3.connect("produtos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estoque")
    rows = cursor.fetchall()
    conn.close()

    # Limpa a tabela existente
    for item in table.get_children():
        table.delete(item)

    # Preenche a tabela com os dados do banco de dados
    for row in rows:
        table.insert("", tk.END, values=row)

def excluir_produto():
    selection = table.focus()  # Obter o item selecionado
    if selection:
        item = table.item(selection)
        values = item['values']
        codigo1 = values[0]
        codigo2 = values[1]

        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM estoque WHERE codigo1=? AND codigo2=?", (codigo1, codigo2))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")

        # Atualizar a tabela após a exclusão
        exibir_dados()

def abrir_janela_edicao(event):
    selection = table.focus()  # Obter o item selecionado
    if selection:
        item = table.item(selection)
        values = item['values']
        codigo1 = values[0]
        codigo2 = values[1]
        
        # Chamar a tela de edição de produto
        produto_edicao.abrir_tela_edicao(codigo1, codigo2, exibir_dados)  # Passa a função exibir_dados como argumento para atualizar a tabela após a edição

# Criação da janela principal
root = tk.Tk()
root.title("Cadastro de Produtos")

# Obter as dimensões da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Define o tamanho da janela para o tamanho total da tela
root.geometry(f"{screen_width}x{screen_height}")

# Frame para a caixa de pesquisa, criação e exclusão de produtos
search_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
search_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

# Divisória entre as seções
divisor1 = ttk.Separator(search_frame, orient="horizontal")
divisor1.pack(fill=tk.X, padx=10, pady=5)

# Criação dos campos para pesquisa
search_label = tk.Label(search_frame, text="Pesquisar:")
search_entry = tk.Entry(search_frame)
search_button = tk.Button(search_frame, text="Pesquisar")
search_label.pack(padx=10, pady=5)
search_entry.pack(padx=10, pady=5)
search_button.pack(padx=10, pady=5)

# Divisória entre as seções
divisor2 = ttk.Separator(search_frame, orient="horizontal")
divisor2.pack(fill=tk.X, padx=10, pady=5)

# Criação dos campos para criação de produtos
codigo1_label = tk.Label(search_frame, text="Código 1:")
codigo1_entry = tk.Entry(search_frame)
codigo2_label = tk.Label(search_frame, text="Código 2:")
codigo2_entry = tk.Entry(search_frame)
nome_label = tk.Label(search_frame, text="Nome:")
nome_entry = tk.Entry(search_frame)
valor_label = tk.Label(search_frame, text="Valor:")
valor_entry = tk.Entry(search_frame)
quantidade_label = tk.Label(search_frame, text="Quantidade:")
quantidade_entry = tk.Entry(search_frame)
salvar_button = tk.Button(search_frame, text="Salvar", command=salvar_dados)
codigo1_label.pack(padx=10, pady=5)
codigo1_entry.pack(padx=10, pady=5)
codigo2_label.pack(padx=10, pady=5)
codigo2_entry.pack(padx=10, pady=5)
nome_label.pack(padx=10, pady=5)
nome_entry.pack(padx=10, pady=5)
valor_label.pack(padx=10, pady=5)
valor_entry.pack(padx=10, pady=5)
quantidade_label.pack(padx=10, pady=5)
quantidade_entry.pack(padx=10, pady=5)
salvar_button.pack(padx=10, pady=10)

# Frame para a tabela de produtos
table_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
table_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Criação da tabela
table = ttk.Treeview(table_frame, columns=("codigo1", "codigo2", "nome", "valor", "quantidade"))
table.heading("codigo1", text="Código 1")
table.heading("codigo2", text="Código 2")
table.heading("nome", text="Nome")
table.heading("valor", text="Valor")
table.heading("quantidade", text="Quantidade")
table.pack(fill=tk.BOTH, expand=True)

# Scrollbar vertical para a tabela
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
table.configure(yscrollcommand=scrollbar.set)

# Divisória entre as seções
divisor3 = ttk.Separator(search_frame, orient="horizontal")
divisor3.pack(fill=tk.X, padx=10, pady=5)

# Botão para excluir produto
excluir_button = tk.Button(search_frame, text="Excluir Produto", command=excluir_produto)
excluir_button.pack(padx=10, pady=5)

# Cria a tabela no banco de dados (se não existir)
criar_tabela()

# Exibe os dados iniciais na tabela
exibir_dados()


# Chamar a tela de edição de produto ao clicar em um item da tabela
table.bind("<Double-1>", abrir_janela_edicao)

# ...

# Inicia o loop principal do tkinter
root.mainloop()

# Inicia o loop principal do tkinter
root.mainloop()
