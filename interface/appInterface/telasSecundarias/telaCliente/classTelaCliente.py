from interface.appInterface.telasSecundarias.telasListas.classTelaExplorar import TelaExplorar
from interface.appInterface.telasSecundarias.telasListas.classTelaPesquisa import TelaPesquisa
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os
from Controll.mapa import Mapa
import folium
import webbrowser

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
        self.botaoEstabelecimento = Button(self.janela, text="Ver Mapa", command=self.mostrar_mapa)
        self.botaoEstabelecimento.place(relx=0.5, rely=0.4, relheight=0.07, relwidth=0.4, anchor="center")


        self.botaoCliente = Button(self.janela, text="Explorar", command=self.telaExplorar)
        self.botaoCliente.place(relx=0.5, rely=0.525, relheight=0.07, relwidth=0.4, anchor="center")

        self.botaoCliente = Button(self.janela, text="Pesquisar", command=self.telaPesquisar)
        self.botaoCliente.place(relx=0.5, rely=0.65, relheight=0.07, relwidth=0.4, anchor="center")

        self.botaoFechar = Button(self.janela, text="Voltar", command=self.janela.destroy)
        self.botaoFechar.place(relx=0.5, rely=0.775, relheight=0.07, relwidth=0.4, anchor="center")

    # Função para exibir o mapa
    def mostrar_mapa(self):
        # copiar o endereço absoluto
        url_mapa = r"C:\Users\Lucas\PycharmProjects\PromoApp\interface\appInterface\telaPrimaria\mapa_promocoes.html"
        webbrowser.open(url_mapa, new=2)

    def inserirLogo(self):
        image_path = r'C:\Users\Lucas\PycharmProjects\PromoApp\interface\appInterface\logoTelaPrincipal\LogoPromoApp.png'
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

    def telaPesquisar(self):
        TelaPesquisa(self.janela)