from interface.appInterface.telasSecundarias.telasListas.classTelaExplorar import TelaExplorar
from interface.appInterface.telasSecundarias.telasListas.classTelaVermaistarde import TelaVerMaisTarde
from interface.appInterface.telasSecundarias.telasListas.classTelaPesquisa import TelaPesquisa
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os

class TelaCliente:

    #Construtor
    def __init__(self, janela):
        self.janela = Toplevel(janela)
        self.janela.title("Promo App")
        self.janela.geometry("800x750")
        self.janela.configure(background="lightblue")
        self.botoesCliente()
        self.inserirLogo()

    def botoesCliente(self):
        self.botaoEstabelecimento = Button(self.janela, text="Ver Mapa")
        self.botaoEstabelecimento.place(relx=0.5, rely=0.35, relheight=0.07, relwidth=0.4, anchor="center")
        self.botaoEstabelecimento = Button(self.janela, text="Ver mais tarde", command=self.telaVerMaisTarde)
        self.botaoEstabelecimento.place(relx=0.5, rely=0.47, relheight=0.07, relwidth=0.4, anchor="center")
        self.botaoCliente = Button(self.janela, text="Explorar", command=self.telaExplorar)
        self.botaoCliente.place(relx=0.5, rely=0.59, relheight=0.07, relwidth=0.4, anchor="center")
        self.botaoCliente = Button(self.janela, text="Pesquisar", command=self.telaPesquisar)
        self.botaoCliente.place(relx=0.5, rely=0.71, relheight=0.07, relwidth=0.4, anchor="center")
        self.botaoFechar = Button(self.janela, text="Voltar", command=self.janela.destroy)
        self.botaoFechar.place(relx=0.5, rely=0.83, relheight=0.07, relwidth=0.4, anchor="center")

    def inserirLogo(self):
        image_path = r'D:\PROGRAMAÇÃO\gitPromoApp\interface\appInterface\logoTelaPrincipal\LogoPromoApp.png'
        img = Image.open(image_path)
        # Redimensiona a imagem mantendo a proporção original
        largura, altura = img.size
        nova_largura = 182  # Largura desejada
        nova_altura = int(altura * nova_largura / largura)  # Calcula a altura proporcional
        img = img.resize((nova_largura, nova_altura), Image.LANCZOS)

        tk_img = ImageTk.PhotoImage(img)

        logo_label = tk.Label(self.janela, image=tk_img, bd=0)
        logo_label.image = tk_img  # Manter uma referência à imagem para evitar que seja destruída
        logo_label.pack(pady=40)  # Ajusta o pady conforme necessário

    def telaExplorar(self):
        TelaExplorar(self.janela)

    def telaVerMaisTarde(self):
        TelaVerMaisTarde(self.janela)

    def telaPesquisar(self):
        TelaPesquisa(self.janela)
