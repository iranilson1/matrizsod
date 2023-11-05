from typing import Optional, Tuple, Union
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import openpyxl, xlrd
import pathlib
from openpyxl import workbook
from PIL import Image
import pandas as pd


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tema()
        self.tela()
        self.tela_inicial()
    
    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        self.title("Sistema Escolar")
        self.geometry("700x500")
        self.resizable(False,False)

    def tela_inicial(self):
        #dentro de inicial frame
        #img = ctk.CTkImage(Image.open(r'C:\Users\irani\SynologyDrive\fullstack\trabalhos\matrizSOD\PROJETOMATRIZSOD\icon.jpg'), size=(300,200))
        #img = ctk.CTkImage(Image.open(r'C:\Users\irani\SynologyDrive\fullstack\trabalhos\matrizSOD\PROJETOMATRIZSOD\Gestao-escolar.jpg'), size=(700,200))
        #label_img = ctk.CTkLabel(self, image=img, text='').place(x=0,y=10)
        img = ctk.CTkImage(Image.open(r'PROJETOMATRIZSOD/service-1028805_640.jpg'), size=(100,71))
        titulo = ctk.CTkLabel(self, text = 'Sistema de gestão escolar', font=('Century Gothic bold',24), text_color='#fff').place(x=200,y=10)
        
        #subtitulo = ctk.CTkLabel(self, text='Por favor, preencha todos os campos do formulario', font=('Century Gothic bold',12), text_color='#fff').place(x=0,y=40)
        
        #frame
        inicial_frame = ctk.CTkFrame(master=self, width=700, height= 400)
        inicial_frame.pack(side=RIGHT)

        # sistema completo com todas as telas 
        def tela_sistemas():
            #remover tela inicial
            inicial_frame.pack_forget()

            #criando tela de cadastro de sistema
            sistema_frame = ctk.CTkFrame(master=self, width=700, height= 400)
            sistema_frame.pack(side=RIGHT)

            titulo = ctk.CTkLabel(master=sistema_frame, text = 'Cadastre os sistemas', font=('Century Gothic bold',16), text_color='gray').place(x=20,y=10)
            label_codigo = ctk.CTkLabel(master=sistema_frame, text = 'Digite o codigo do sistema', font=('Century Gothic bold',16), text_color='#fff').place(x=265,y=65)
            codigo_sistemas = ctk.CTkEntry(master=sistema_frame,placeholder_text= 'CDG', width=300).place(x=200, y=100)
            
            label_sistema = ctk.CTkLabel(master=sistema_frame, text = 'Digite o nome do sistema', font=('Century Gothic bold',16), text_color='#fff').place(x=265,y=140)
            nome_sistemas = ctk.CTkEntry(master=sistema_frame,placeholder_text= 'Sistema', width=300).place(x=200, y=175)
            
            def back():
                #removendo frame
                sistema_frame.pack_forget()

                #devolvendo frame da tela inicial
                inicial_frame.pack(side=RIGHT)
                
            voltar = ctk.CTkButton(master=sistema_frame, text='VOLTAR', font=('Century Gothic bold',16), text_color='#fff',command= back ).place(x=20, y=350)

            def salva_servico():
                msg = messagebox.showinfo(title='Estado do cadastro', message= "Parabens! serviço cadastrado com sucesso")

            salvar = ctk.CTkButton(master=sistema_frame, text='SALVAR', font=('Century Gothic bold',16), text_color='#fff', fg_color='green',hover_color="#014B05", command= salva_servico ).place(x=545, y=350)
            def tela_perfil():
                #remover tela inicial
                inicial_frame.pack_forget()

                #criando tela de cadastro de sistema
                perfil_frame = ctk.CTkFrame(master=self, width=700, height= 400)
                perfil_frame.pack(side=RIGHT)

                #pegar um datafreme
                dataframe = pd.read_excel('.\sistemaEscola.xlsx', sheet_name='Sistema')
                valor = dataframe.loc[:,'CODIGO']
                

                titulo = ctk.CTkLabel(master=perfil_frame, text = 'Cadastro do perfil de acesso', font=('Century Gothic bold',16), text_color='gray').place(x=20,y=10)
                label_codigo_perfil = ctk.CTkLabel(master=perfil_frame, text = 'Digite o código do sistema', font=('Century Gothic bold',16), text_color='#fff').place(x=265,y=65)
                self.codigo_perfil = ctk.CTkComboBox(master=perfil_frame, values=list(valor))
                self.codigo_perfil.place(x=280, y=100)
                
                label_nome = ctk.CTkLabel(master=perfil_frame, text = 'Nome do perfil', font=('Century Gothic bold',16), text_color='#fff').place(x=295,y=140)
                self.nome_perfil = ctk.CTkEntry(master=perfil_frame,placeholder_text= 'Nome', width=300)
                self.nome_perfil.place(x=200, y=175)

                label_nome = ctk.CTkLabel(master=perfil_frame, text = 'Descrição', font=('Century Gothic bold',16), text_color='#fff').place(x=300,y=215)
                self.r_caixaTexto = ctk.CTkTextbox(master=perfil_frame, width=300, height=120, corner_radius=0)
                self.r_caixaTexto.place(x=200, y=250)

                def back():
                    #removendo frame
                    perfil_frame.pack_forget()

                    #devolvendo frame da tela inicial
                    inicial_frame.pack(side=RIGHT)
                
                voltar = ctk.CTkButton(master=perfil_frame, text='VOLTAR', font=('Century Gothic bold',16), text_color='#fff',command= back ).place(x=20, y=350)
                self.salvar = ctk.CTkButton(master=perfil_frame, text='SALVAR', font=('Century Gothic bold',16), text_color='#fff', fg_color='green',hover_color="#014B05", command= self.salvaPerfilServico ).place(x=545, y=350)
                            
                
        #BOTÃOS DA TELA INICIAL 
        cadastroSistema = ctk.CTkButton(master=inicial_frame,text='Cadastros \n dos \n Sistemas',font=('Century Gothic bold',16), text_color='#fff',image=img, command=tela_sistemas).place(x=10,y=70)  
        


if __name__=="__main__":
    app = App()
    app.mainloop()