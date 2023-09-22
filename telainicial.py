from typing import Optional, Tuple, Union
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import openpyxl, xlrd
import pathlib
from openpyxl import workbook
from PIL import Image


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
        # dentro de inicial frame
        #img = ctk.CTkImage(Image.open(r'C:\Users\irani\SynologyDrive\fullstack\trabalhos\matrizSOD\PROJETOMATRIZSOD\icon.jpg'), size=(300,200))
        #img = ctk.CTkImage(Image.open(r'C:\Users\irani\SynologyDrive\fullstack\trabalhos\matrizSOD\PROJETOMATRIZSOD\Gestao-escolar.jpg'), size=(700,200))
        #label_img = ctk.CTkLabel(self, image=img, text='').place(x=0,y=10)
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

            titulo = ctk.CTkLabel(master=perfil_frame, text = 'Cadastre os perfis do sistema', font=('Century Gothic bold',16),  text_color='gray').place(x=20,y=10)


            def back():
                #removendo frame
                perfil_frame.pack_forget()

                #devolvendo frame da tela inicial
                inicial_frame.pack(side=RIGHT)
            
            voltar = ctk.CTkButton(master=perfil_frame, text='VOLTAR', font=('Century Gothic bold',16), text_color='#fff',command= back ).place(x=20, y=350)
            
            def salva_perfil():
                msg = messagebox.showinfo(title='Estado do cadastro', message= "Parabens! perfil do serviço cadastrado com sucesso")
                
            salvar = ctk.CTkButton(master=perfil_frame, text='SALVAR', font=('Century Gothic bold',16), text_color='#fff', fg_color='green',hover_color="#014B05", command= salva_perfil ).place(x=545, y=350)
            
        def tela_matriz():
            #remover tela inicial
            inicial_frame.pack_forget()

            #criando tela de cadastro de sistema
            matriz_frame = ctk.CTkFrame(master=self, width=700, height= 400)
            matriz_frame.pack(side=RIGHT)
            
            titulo = ctk.CTkLabel(master=matriz_frame, text = 'Cadastre dos conflitos', font=('Century Gothic bold',16), text_color='gray').place(x=20,y=10)


            def back():
                #removendo frame
                matriz_frame.pack_forget()

                #devolvendo frame da tela inicial
                inicial_frame.pack(side=RIGHT)
            voltar = ctk.CTkButton(master=matriz_frame, text='VOLTAR', font=('Century Gothic bold',16), text_color='#fff',command= back ).place(x=20, y=350)

            def salva_matriz():
                msg = messagebox.showinfo(title='Estado do cadastro', message= "Parabens! conflito de perfis cadastrado com sucesso")

            salvar = ctk.CTkButton(master=matriz_frame, text='SALVAR', font=('Century Gothic bold',16), text_color='#fff', fg_color='green',hover_color="#014B05", command= salva_matriz ).place(x=545, y=350)
            

        def tela_perfil_user():
            #remover tela inicial
            inicial_frame.pack_forget()

            #criando tela de cadastro de sistema
            perfilU_frame = ctk.CTkFrame(master=self, width=700, height= 400)
            perfilU_frame.pack(side=RIGHT)

            titulo = ctk.CTkLabel(master=perfilU_frame, text = 'Cadastre os perfis dos usuarios', font=('Century Gothic bold',16),  text_color='gray').place(x=20,y=10)


            def back():
                #removendo frame
                perfilU_frame.pack_forget()

                #devolvendo frame da tela inicial
                inicial_frame.pack(side=RIGHT)
            
            voltar = ctk.CTkButton(master=perfilU_frame, text='VOLTAR', font=('Century Gothic bold',16), text_color='#fff',command= back ).place(x=20, y=350)
            
            def salva_user():
                msg = messagebox.showinfo(title='Estado do cadastro', message= "Parabens! usuario cadastrado com sucesso")
            
            salvar = ctk.CTkButton(master=perfilU_frame, text='SALVAR', font=('Century Gothic bold',16), text_color='#fff', fg_color='green',hover_color="#014B05", command= salva_user ).place(x=545, y=350)
            
            
        #BOTÃOS DA TELA INICIAL 
        cadastroSistema = ctk.CTkButton(master=inicial_frame,text='Cadastros dos Sistemas',font=('Century Gothic bold',16), text_color='#fff', width=290, command=tela_sistemas).place(x=10,y=70)
        cadastroPerfis = ctk.CTkButton(master=inicial_frame,text='Cadastros dos perfils Sistemas',font=('Century Gothic bold',16), text_color='#fff', width=290, command=tela_perfil).place(x=10,y=150)
        cadastroSMatriz = ctk.CTkButton(master=inicial_frame,text='Cadastros da matriz SOD',font=('Century Gothic bold',16), text_color='#fff', width=290, command=tela_matriz).place(x=400,y=70)
        cadastroPerfiluser = ctk.CTkButton(master=inicial_frame,text='Cadastros dos Perfils de usuarios',font=('Century Gothic bold',16), text_color='#fff', width=290, command=tela_perfil_user).place(x=400,y=150)
        
        


if __name__=="__main__":
    app = App()
    app.mainloop()