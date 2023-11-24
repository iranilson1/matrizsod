import customtkinter as ctk

class TabelaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Criar cabeçalhos
        ctk.CTkLabel(self, text="Nome", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkLabel(self, text="Idade", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=5, pady=5)

        # Adicionar dados à tabela
        dados = [
            ("João", 25),
            ("Maria", 30),
            ("Carlos", 22),
            ("Ana", 28),
            ("Pedro", 35)
        ]

        for i, (nome, idade) in enumerate(dados, start=1):
            ctk.CTkLabel(self, text=nome).grid(row=i, column=0, padx=5, pady=5)
            ctk.CTkLabel(self, text=str(idade)).grid(row=i, column=1, padx=5, pady=5)

        # Adicionar um botão para testar a funcionalidade
        btn_mostrar_dados = ctk.CTkButton(self, text="Mostrar Dados", command=self.mostrar_dados)
        btn_mostrar_dados.grid(row=len(dados) + 1, column=0, columnspan=2, pady=10)

    def mostrar_dados(self):
        # Exemplo de como obter os dados da tabela
        for i in range(1, 100):  # Assume que há no máximo 100 linhas na tabela
            nome_widget = self.grid_slaves(row=i, column=0)
            idade_widget = self.grid_slaves(row=i, column=1)
            if nome_widget and idade_widget:
                nome = nome_widget[0].cget("text")
                idade = idade_widget[0].cget("text")
                if nome and idade:
                    print(f"Nome: {nome}, Idade: {idade}")


if __name__ == "__main__":
    app = TabelaApp()
    app.mainloop()
