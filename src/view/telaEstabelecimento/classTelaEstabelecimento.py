import tkinter as tk
from tkinter import *

from PIL import ImageTk, Image

from src.utils.path_util import path
from src.view.telaEstabelecimento.classTelaAdPromo import TelaAdPromo
from src.view.telaEstabelecimento.classTelaRemPromo import TelaRemPromo


class TelaEstabelecimento:
    # Construtor
    def __init__(self, janela):
        self.janela = Toplevel(janela)
        self.janela.title("Promo App")
        self.janela.geometry("800x750")
        self.janela.configure(background="lightblue")
        self.botoes_estabelecimento()
        self.inserir_logo()

    def botoes_estabelecimento(self):
        self.botaoEstabelecimento = Button(self.janela, text="Adicionar Promoção", command=self.tela_ad_promo)
        self.botaoEstabelecimento.place(relx=0.5, rely=0.35, relheight=0.07, relwidth=0.4, anchor="center")
        self.botaoCliente = Button(self.janela, text="Remover Promoção", command=self.tela_remover_promo)
        self.botaoCliente.place(relx=0.5, rely=0.47, relheight=0.07, relwidth=0.4, anchor="center")
        self.botaoFechar = Button(self.janela, text="Voltar", command=self.janela.destroy)
        self.botaoFechar.place(relx=0.5, rely=0.59, relheight=0.07, relwidth=0.4, anchor="center")

    def inserir_logo(self):
        img = Image.open(path.logo)
        # Redimensiona a imagem mantendo a proporção original
        largura, altura = img.size
        nova_largura = 182  # Largura desejada
        nova_altura = int(altura * nova_largura / largura)  # Calcula a altura proporcional
        img = img.resize((nova_largura, nova_altura), Image.LANCZOS)

        tk_img = ImageTk.PhotoImage(img)

        logo_label = tk.Label(self.janela, image=tk_img, bd=0)
        logo_label.image = tk_img  # Manter uma referência à imagem para evitar que seja destruída
        logo_label.pack(pady=40)  # Ajusta o pady conforme necessário

    def tela_remover_promo(self):
        TelaRemPromo(self.janela)

    def tela_ad_promo(self):
        TelaAdPromo(self.janela)
