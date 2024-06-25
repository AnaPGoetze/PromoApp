from appInterface.telasSecundarias.AdRemoveSerch.classTelaAdPromo import TelaAdPromo
from appInterface.telasSecundarias.AdRemoveSerch.classTelaRemPromo import TelaRemPromo
from appInterface.telasSecundarias.AdRemoveSerch.classTelaPesquisa import telaPesquisa
from appInterface.telasSecundarias.telasListas.classTelaExplorar import TelaExplorar
from appInterface.telasSecundarias.telasListas.classTelaVermaistarde import TelaVerMaisTarde
from tkinter import *

class TelaPrincipal:
    #Construtor
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Promo App")
        self.janela.geometry("800x900")
        self.janela.configure(background="lightblue")
        self.botaoAdPromo()
        self.inserirTitulo()
        self.janela.mainloop()

    #Botões da Tela Principal
    def botaoAdPromo(self):
        self.botao = Button(self.janela, text="Adicionar Promoção", command=self.telaAdPromo)
        self.botao.place(relx=0.24, rely=0.3, relheight=0.05, relwidth=0.2)
        self.botaoRemoverPromo = Button(self.janela, text="Remover Promoção", command=self.telaRemoverPromo)
        self.botaoRemoverPromo.place(relx=0.55, rely=0.3, relheight=0.05, relwidth=0.2)
        self.botaoPesquisar = Button(self.janela, text="Pesquisar", command=self.telaPesquisar)
        self.botaoPesquisar.place(relx=0.15, rely=0.2, relheight=0.05, relwidth=0.7)
        self.botaoExplorar = Button(self.janela, text="Explorar", command=self.telaExplorar)
        self.botaoExplorar.place(relx=0.2, rely=0.9, relheight=0.05, relwidth=0.2)
        self.botaoFechar = Button(self.janela, text="Fechar", command=self.janela.destroy)
        self.botaoFechar.place(relx=0.6, rely=0.9, relheight=0.05, relwidth=0.2)
        self.botaoVerMaisTarde = Button(self.janela, text="Ver mais tarde", command=self.telaVerMaisTarde)
        self.botaoVerMaisTarde.place(relx=0.4, rely=0.9, relheight=0.05, relwidth=0.2)

    #Inseririr uma frame com uma label com o titulo promo app
    def inserirTitulo(self):
        self.frame = Frame(self.janela)
        #Cor de fundo azul claro e borda preta
        self.frame.configure(background="#8ed1e7", borderwidth=2, relief="solid")
        self.frame.place(relx=0.35, rely=0.05, relheight=0.1, relwidth=0.3)
        #Label de titulo com fonte arial 20 e cor azul
        self.lb = Label(self.frame, text="Promo App", background="#8ed1e7", font=("Arial", 20))
        self.lb.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)


    ########################################### Janelas Secundarias ########################################
    # Janelas Secundarias, chamadas pelos botões
    def telaAdPromo(self):
        TelaAdPromo(self.janela)

    def telaRemoverPromo(self):
        TelaRemPromo(self.janela)

    def telaPesquisar(self):
        telaPesquisa(self.janela)

    def telaExplorar(self):
        TelaExplorar(self.janela)

    def telaVerMaisTarde(self):
        TelaVerMaisTarde(self.janela)

TelaPrincipal(Tk())
