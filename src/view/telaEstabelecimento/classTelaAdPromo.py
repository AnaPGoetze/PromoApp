from tkinter import *

from src.controller.planilha import Planilha


class TelaAdPromo:
    def __init__(self, janela):
        self.janela = Toplevel(janela)
        self.janela.title("Adicionar Promoção")
        self.janela.geometry("600x600")
        self.criarWidget()
        self.adicionarTitulo()

    def adicionarTitulo(self):
        self.frame = Frame(self.janela)
        self.frame.configure(background="white", borderwidth=2, relief="solid")
        self.frame.place(relx=0.24, rely=0.05, relheight=0.1, relwidth=0.5)
        self.lb = Label(self.frame, text="Adicionar Promoção", background="white", font=("Arial", 20))
        self.lb.place(relx=0.08, rely=0.1, relheight=0.8, relwidth=0.9)

    def criarWidget(self):
        self.lbNomeLocal = Label(self.janela, text="Nome do Local")
        self.lbNomeLocal.place(relx=0.1, rely=0.2, relheight=0.05, relwidth=0.8)
        self.entryNomeLocal = Entry(self.janela)
        self.entryNomeLocal.place(relx=0.1, rely=0.25, relheight=0.05, relwidth=0.8)

        self.lbNomeProduto = Label(self.janela, text="Nome do Produto")
        self.lbNomeProduto.place(relx=0.1, rely=0.3, relheight=0.05, relwidth=0.8)
        self.entryNomeProduto = Entry(self.janela)
        self.entryNomeProduto.place(relx=0.1, rely=0.35, relheight=0.05, relwidth=0.8)

        self.lbDescontoProduto = Label(self.janela, text="Desconto do Produto")
        self.lbDescontoProduto.place(relx=0.1, rely=0.4, relheight=0.05, relwidth=0.8)
        self.entryDescontoProduto = Entry(self.janela)
        self.entryDescontoProduto.place(relx=0.1, rely=0.45, relheight=0.05, relwidth=0.8)

        self.lbLatitude = Label(self.janela, text="Latitude")
        self.lbLatitude.place(relx=0.1, rely=0.5, relheight=0.05, relwidth=0.8)
        self.entryLatitude = Entry(self.janela)
        self.entryLatitude.place(relx=0.1, rely=0.55, relheight=0.05, relwidth=0.8)

        self.lbLongitude = Label(self.janela, text="Longitude")
        self.lbLongitude.place(relx=0.1, rely=0.6, relheight=0.05, relwidth=0.8)
        self.entryLongitude = Entry(self.janela)
        self.entryLongitude.place(relx=0.1, rely=0.65, relheight=0.05, relwidth=0.8)

        self.botoes()

    def botoes(self):
        self.botaoAdicionar = Button(self.janela, text="Adicionar", command=self.adicionar)
        self.botaoAdicionar.place(relx=0.1, rely=0.8, relheight=0.08, relwidth=0.2)

        self.botaoCancelar = Button(self.janela, text="Cancelar", command=self.janela.destroy)
        self.botaoCancelar.place(relx=0.7, rely=0.8, relheight=0.08, relwidth=0.2)

    def adicionar(self):
        planilha = Planilha()
        planilha.inserir_promocao_planilha(self.entryNomeLocal.get(), self.entryNomeProduto.get(), self.entryDescontoProduto.get(), self.entryLatitude.get(), self.entryLongitude.get())
        self.janela.destroy()
