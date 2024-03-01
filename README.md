# matrizsod com python e customtkinter
um projeto feito para gerenciar relacionamentos conflitantes entre determinadas entidades de modelo. então neste projeto é mostrado a relação de conflitos de uma escola usando python e o tkinter e custontkinter criando assim um software para o tratamento de conflitos.
são quatro telas e em sequencia termos o *cadastroSistema*, cadatro dos sistemas da escola, como direção e educação, depois *cadastroPerfis* cadastros dos perfis onde se cadastra os perfis de cada sistema como na direção teremos como perfil, secretaria, coordenação, financeiro etc... 
em seguida *cadastroSMatriz* os cadastros de matriz pega cada sistema e seu perfil e cadastra o conflito com outro perfil ex. no sistema direção perfil coordenação e cadastrar o conflito com o perfil secretaria. e por fim cadastra o usuario *cadastroPerfiluser*, onde aqui tudo do sistema é testado pois é cadastrado o usuario no sistema e no perfil, por exemplo iranilson vai ser cadastrado no sistema de direção no perfil secretaria e pronto sera salvo então o teste de cadatrar iranilson como coordenador o sistema teria que acusar um conflito pois esse conflito ja foi cadastrado.

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

logo abaixo temos a função da *tela_inicial*  onde configura e monta toda a tela inicial 
```
 def tela_inicial(self):
    # dentro de inicial frame
    # Obtém o diretório atual do arquivo .py
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    # Usa o caminho do arquivo como argumento para CTkImage
    retornar = ctk.CTkImage(Image.open(os.path.join(os.path.join(diretorio_atual, 'icones'),  'casa.png')))
    adusuario = ctk.CTkImage(Image.open(os.path.join(os.path.join(diretorio_atual, 'icones'), 'adicionar-usuario.png')))

    titulo = ctk.CTkLabel(self, text = 'Sistema de gestão escolar', font=('Century Gothic bold',24), text_color='#fff').place(x=200,y=10)

    #frame
    inicial_frame = ctk.CTkFrame(master=self, width=700, height= 400)
    inicial_frame.pack(side=RIGHT)
``` 
neste primeiro momento configura o titulo e o frame da tela inicial, lembrando que cada tela tera um frame diferente, e no frame da tela inicial so vai aparecer os botões para entrar nas outras telas.
```
 #BOTÃOS DA TELA INICIAL 
cadastroSistema = ctk.CTkButton(master=inicial_frame,text='Cadastros dos Sistemas',font=('Century Gothic bold',16), text_color='#fff', width=290, command=tela_sistemas).place(x=10,y=70)
cadastroPerfis = ctk.CTkButton(master=inicial_frame,text='Cadastros dos perfis do Sistemas',font=('Century Gothic bold',16), text_color='#fff', width=290, command=tela_perfil).place(x=10,y=150)
cadastroSMatriz = ctk.CTkButton(master=inicial_frame,text='Cadastros da matriz SOD',font=('Century Gothic bold',16), text_color='#fff', width=290, command=tela_matriz).place(x=400,y=70)
cadastroPerfiluser = ctk.CTkButton(master=inicial_frame,text='Cadastros dos Perfils de usuarios',font=('Century Gothic bold',16), text_color='#fff',image=adusuario, width=290, command=tela_perfil_user).place(x=400,y=150)
```
são quatro telas descritas anteriormente cada uma delas tem uma função que realiza a sua determinada função de cadastrar vou demostrar somente a de cadastro de sistemas, podera ver todas nos arquivos acima linkados 
```
 def tela_sistemas():
    #remover tela inicial
    inicial_frame.pack_forget()

    #criando tela de cadastro de sistema
    sistema_frame = ctk.CTkFrame(master=self, width=700, height= 400)
    sistema_frame.pack(side=RIGHT)

    titulo = ctk.CTkLabel(master=sistema_frame, text = 'Cadastre os sistemas', font=('Century Gothic bold',16), text_color='gray').place(x=20,y=10)
    label_codigo = ctk.CTkLabel(master=sistema_frame, text = 'Digite o codigo do sistema', font=('Century Gothic bold',16), text_color='#fff').place(x=265,y=65)
    self.codigoSistemas = ctk.CTkEntry(master=sistema_frame,placeholder_text= 'CDG', width=300)
    self.codigoSistemas.place(x=200, y=100)
    
    label_sistema = ctk.CTkLabel(master=sistema_frame, text = 'Digite o nome do sistema', font=('Century Gothic bold',16), text_color='#fff').place(x=265,y=140)
    self.nomeSistemas = ctk.CTkEntry(master=sistema_frame,placeholder_text= 'Sistema', width=300)
    self.nomeSistemas.place(x=200, y=175)
    
    def back():
        #removendo frame
        sistema_frame.pack_forget()

        #devolvendo frame da tela inicial
        inicial_frame.pack(side=RIGHT)
    def consultas():
        #removendo frame
        sistema_frame.pack_forget()
        
        # Criar um frame com customtkinter
        consulta_frame = ctk.CTkFrame(self)
        consulta_frame.pack(padx=10, pady=60)

        # Criar um widget Treeview
        tree = ttk.Treeview(consulta_frame,height=15, columns=('CODIGO', 'SISTEMA'), show='headings')
        tree.heading('CODIGO', text='CODIGO')
        tree.heading('SISTEMA', text='SISTEMA')
        tree.pack()

        # criando os dados
        contacts = []
        dataframe = pd.read_excel('.\sistemaEscola.xlsx', sheet_name='Sistema')

        for n in range(0,len(dataframe)):
            codigs = dataframe.loc[n,:]
            tree.insert('', tk.END, values=list(codigs))
            
        
        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                # show a message
                showinfo(title='Information', message=','.join(record))
        
        tree.bind('<<TreeviewSelect>>', item_selected)
        tree.pack(side='top', padx=(5, 5), pady=10, anchor='n')

        def back():
            #removendo frame
            consulta_frame.pack_forget()

            #devolvendo frame da tela inicial
            sistema_frame.pack(side=RIGHT)

        voltar = ctk.CTkButton(master=consulta_frame, text='',image=retornar,command= back, width=100, height=40)
        voltar.pack(ipady=10)

    voltar = ctk.CTkButton(master=sistema_frame, text='',image=retornar,command= back, width=100, height=40).place(x=20, y=350)
    self.salvar = ctk.CTkButton(master=sistema_frame, text='SALVAR', font=('Century Gothic bold',16), text_color='#fff', fg_color='green',hover_color="#014B05", command=         
       self.salvaSistema,width=100, height=40).place(x=580, y=350)
    consulta = ctk.CTkButton(master=sistema_frame, text='CONSULTAR', font=('Century Gothic bold',16), text_color='#fff', fg_color='green',hover_color="#014B05", command= 
       consultas,width=100, height=40).place(x=300, y=350)
```
é criado um novo frame temos duas entradas de dados esse dados são enviados para uma outra class por nome backend onde realmente são tratados e salvos no banco onde neste caso foi usado o Excel para salvar esses dados.
a class que processas as informações dos cadastros é essa logo abaixo, ela salva tudo no backend
```
class Backend():   
    def salvando(self):
        arquivo = pathlib.Path('sistemaEscola.xlsx')
        if arquivo.exists():
            pass
        else:
            #FOLHA DA FUNÇÃO SISTEMA
            arquivo = Workbook()
            folha1 = arquivo.active
            folha1.title = 'Sistema'
            folha1['A1'] = 'CODIGO'
            folha1['B1'] = 'NOME'
            
            #FOLHA DA FUNÇÃO PERFIL DO SISTEMA 
            folha2=arquivo.create_sheet('perfilSistema')
            folha2['A1'] = 'CODIGO'
            folha2['B1'] = 'NOME'
            folha2['C1'] = 'DESCRIÇÃO'

            #FOLHA DA FUNÇÃO MATRIZSOD 
            folha3=arquivo.create_sheet('matrizSOD')
            folha3['A1'] = 'CODIGO1'
            folha3['B1'] = 'NOME1'
            folha3['C1'] = 'CODIGO2'
            folha3['D1'] = 'NOME2'

            #FOLHA DA FUNÇÃO perfiluser
            folha4=arquivo.create_sheet('PerfilUser')
            folha4['A1'] = 'CPF'
            folha4['B1'] = 'CODIGO'
            folha4['C1'] = 'NOME'
            arquivo.save(r'sistemaEscola.xlsx')
            
    def salvaSistema(self):
        #pegar os daos que estão no formulario do sistema 
        self.codigo = self.codigoSistemas.get()
        self.sistema = self.nomeSistemas.get()

        # Carregue o arquivo Excel em um DataFrame
        dataframesistema = pd.read_excel('.\sistemaEscola.xlsx', sheet_name='Sistema')

        # Verifique a unicidade dos valores na coluna
        codigo_duplicados = dataframesistema.loc[dataframesistema['CODIGO']==self.codigo,'CODIGO']
        nome_duplicados = dataframesistema.loc[dataframesistema['NOME']==self.sistema,'NOME']

```
nesse exemplo é mostrado somente a parte de salvamento do sistema mas mostra a construção no excel de todas as folhas para cada função.
