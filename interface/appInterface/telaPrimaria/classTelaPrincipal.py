from interface.appInterface.telasSecundarias.telaEstabelecimento.classTelaEstabelecimento import TelaEstabelecimento
from interface.appInterface.telasSecundarias.telaCliente.classTelaCliente import TelaCliente
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os

class TelaPrincipal:
    #Construtor
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Promo App")
        self.janela.geometry("800x750")
        self.janela.configure(background="lightblue")
        self.botaoAdPromo()
        self.inserirLogo()
        self.janela.mainloop()

    #Botões da Tela Principal
    def botaoAdPromo(self):
        self.botaoEstabelecimento = Button(self.janela, text="Estabelecimento", command=self.telaEstabelecimento)
        self.botaoEstabelecimento.place(relx=0.5, rely=0.35, relheight=0.07, relwidth=0.4, anchor="center")
        self.botaoCliente = Button(self.janela, text="Cliente", command=self.telaCliente)
        self.botaoCliente.place(relx=0.5, rely=0.47, relheight=0.07, relwidth=0.4, anchor="center")
        self.botaoFechar = Button(self.janela, text="Fechar", command=self.janela.destroy)
        self.botaoFechar.place(relx=0.5, rely=0.59, relheight=0.07, relwidth=0.4, anchor="center")

    #Inseririr uma frame com uma label com o titulo promo app


    def inserirLogo(self):
        image_path = '../PromoApp/interface/appInterface/logoTelaPrincipal/LogoPromoApp.png'
        img = Image.open(image_path)
        # Redimensiona a imagem mantendo a proporção original
        largura, altura = img.size
        nova_largura = 182  # Largura desejada
        nova_altura = int(altura * nova_largura / largura)  # Calcula a altura proporcional
        img = img.resize((nova_largura, nova_altura), Image.LANCZOS)

        tk_img = ImageTk.PhotoImage(img)

        logo_label = tk.Label(self.janela, image = tk_img, bd=0)
        logo_label.image = tk_img  # Manter uma referência à imagem para evitar que seja destruída
        logo_label.pack(pady=40)  # Ajusta o pady conforme necessário

    ########################################### Janelas Secundarias ########################################
    # Janelas Secundarias, chamadas pelos botões
    def telaEstabelecimento(self):
        TelaEstabelecimento(self.janela)

    def telaCliente(self):
        TelaCliente(self.janela)

TelaPrincipal(Tk())