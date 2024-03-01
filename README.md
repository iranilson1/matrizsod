# matrizsod com python e customtkinter
um projeto feito para gerenciar relacionamentos conflitantes entre determinadas entidades de modelo. então neste projeto é mostrado a relação de conflitos de uma escola usando python e o tkinter e custontkinter criando assim um software para o tratamento de conflitos. 

começamos pela class *App*
```
class App(ctk.CTk, Backend):
```
Essa é a class onde todo o projeto roda, e foi dividido por  funções 
```
class App(ctk.CTk, Backend):
    def __init__(self):
        super().__init__()
        self.tema()
        self.tela()
        self.salvando()
        self.tela_inicial()
    
    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        self.title("Sistema Escolar")
        self.geometry("700x500")
        self.resizable(False,False)
```
a função __initial__ serve para inicializar todas as outras funções e chamar elas, ja a função tem e tela é para definir as configurações de tela como cor, tema e tamanho.
logo abaixo temos a função da ###telainicial 
