import tkinter as tk
from tkinter import ttk

def adicionar_dados():
    # Obtém os dados do Entry e os adiciona à Treeview
    nome = entry_nome.get()
    idade = entry_idade.get()
    tree.insert('', 'end', values=(nome, idade))

# Configuração da janela principal
root = tk.Tk()
root.title("Tabela com Tkinter")

# Criar Treeview com colunas
tree = ttk.Treeview(root, columns=('Nome', 'Idade'), show='headings')
tree.heading('Nome', text='Nome')
tree.heading('Idade', text='Idade')
tree.pack(padx=10, pady=10)

# Adicionar dados à tabela
tree.insert('', 'end', values=('João', 25))
tree.insert('', 'end', values=('Maria', 30))

# Entradas para adicionar novos dados
label_nome = tk.Label(root, text='Nome:')
label_nome.pack(pady=(10, 0))
entry_nome = tk.Entry(root)
entry_nome.pack(pady=(0, 10))

label_idade = tk.Label(root, text='Idade:')
label_idade.pack()
entry_idade = tk.Entry(root)
entry_idade.pack(pady=(0, 10))

# Botão para adicionar dados
btn_adicionar = tk.Button(root, text='Adicionar', command=adicionar_dados)
btn_adicionar.pack()

# Iniciar o loop principal
root.mainloop()