from interface.appInterface.telasSecundarias.telaEstabelecimento.classTelaRemPromo import TelaRemPromo
from interface.appInterface.telasSecundarias.telaEstabelecimento.classTelaAdPromo import TelaAdPromo
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
#from tkinter import ttk

class TelaEstabelecimento:
    #Construtor
    def __init__(self, janela):
        self.janela = Toplevel(janela)
        self.janela.title("Promo App")
        self.janela.geometry("800x750")
        self.janela.configure(background="lightblue")
        self.botoesEstabelecimento()
        self.inserirLogo()

    def botoesEstabelecimento(self):
        self.botaoEstabelecimento = Button(self.janela, text="Adcionar Promoção", command=self.telaAdPromo)
        self.botaoEstabelecimento.place(relx=0.5, rely=0.35, relheight=0.07, relwidth=0.4, anchor="center")
        self.botaoCliente = Button(self.janela, text="Remover Promoção", command=self.telaRemoverPromo)
        self.botaoCliente.place(relx=0.5, rely=0.47, relheight=0.07, relwidth=0.4, anchor="center")
        self.botaoFechar = Button(self.janela, text="Voltar", command=self.janela.destroy)
        self.botaoFechar.place(relx=0.5, rely=0.59, relheight=0.07, relwidth=0.4, anchor="center")

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


    def telaRemoverPromo(self):
        TelaRemPromo(self.janela)


    def telaAdPromo(self):
        TelaAdPromo(self.janela)
