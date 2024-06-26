from tkinter import *
from Controll import funcoesSql

class telaPesquisa:
    #Construtor
    def __init__(self, janela):
        self.janela = Toplevel(janela)
        self.janela.title("Pesquisar")
        self.janela.geometry("600x600")
        self.criarWidget()
        self.adicionarTitulo()
        
    #Criar uma frame com uma label com o titulo remover promoção
    def adicionarTitulo(self):
        self.frame = Frame(self.janela)
        self.frame.configure(background="white", borderwidth=2, relief="solid")
        self.frame.place(relx=0.25, rely=0.05, relheight=0.1, relwidth=0.5)
        #Label de titulo com fonte arial 20 e cor azul
        self.lb = Label(self.frame, text="Pesquisar", background="white", font=("Arial", 20))
        self.lb.place(relx=0.08, rely=0.1, relheight=0.8, relwidth=0.9)

    #Criar labels e entry para inserir os dados da promoção a ser pesquisada
    def criarWidget(self):
        self.lbPesquisa = Label(self.janela, text="Digite o nome do local ou o nome do produto:")
        self.lbPesquisa.place(relx=0.1, rely=0.35, relheight=0.05, relwidth=0.8)
        self.entryPesquisa = Entry(self.janela)
        self.entryPesquisa.place(relx=0.1, rely=0.4, relheight=0.05, relwidth=0.8)

        self.botao = Button(self.janela, text="Pesquisar", command=self.pesquisarNoBanco)
        self.botao.place(relx=0.1, rely=0.8, relheight=0.08, relwidth=0.2)

        self.botaoCancelar = Button(self.janela, text="Cancelar", command=self.janela.destroy)
        self.botaoCancelar.place(relx=0.7, rely=0.8, relheight=0.08, relwidth=0.2)

    def pesquisarNoBanco(self):
        nome = self.entryPesquisa.get()
        funcoesSql.pesquisarNoBanco(nome)
