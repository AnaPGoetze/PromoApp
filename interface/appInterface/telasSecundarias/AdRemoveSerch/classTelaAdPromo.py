from tkinter import *

class TelaAdPromo:
    #Construtor
    def __init__(self, janela):
        self.janela = Toplevel(janela)
        self.janela.title("Adicionar Promoção")
        self.janela.geometry("600x600")
        self.criarWidget()
        self.adicionarTitulo()

    #Adicionar uma frame com uma label com o titulo adicionar promoção
    def adicionarTitulo(self):
        self.frame = Frame(self.janela)
        self.frame.configure(background="white", borderwidth=2, relief="solid")
        self.frame.place(relx=0.24, rely=0.05, relheight=0.1, relwidth=0.5)
        #Label de titulo com fonte arial 20 e cor azul
        self.lb = Label(self.frame, text="Adicionar Promoção", background="white", font=("Arial", 20))
        self.lb.place(relx=0.08, rely=0.1, relheight=0.8, relwidth=0.9)

    #Criar labels e entry para inserir os dados da promoção a ser adicionada
    def criarWidget(self):
        self.lbNomeLocal = Label(self.janela, text="Nome do Local")
        self.lbNomeLocal.place(relx=0.1, rely=0.35, relheight=0.05, relwidth=0.8)
        self.entryNomeLocal = Entry(self.janela)
        self.entryNomeLocal.place(relx=0.1, rely=0.4, relheight=0.05, relwidth=0.8)

        self.lbDescrição = Label(self.janela, text="Descrição")
        self.lbDescrição.place(relx=0.1, rely=0.45, relheight=0.05, relwidth=0.8)
        self.entryDescrição = Entry(self.janela)
        self.entryDescrição.place(relx=0.1, rely=0.5, relheight=0.05, relwidth=0.8)

        self.botoes()
        
    #Criar os botoes para voltar e adicionar
    def botoes(self):
        self.botao = Button(self.janela, text="Adicionar", command=self.janela.destroy)
        self.botao.place(relx=0.1, rely=0.8, relheight=0.08, relwidth=0.2)

        self.botaoCancelar = Button(self.janela, text="Cancelar", command=self.janela.destroy)
        self.botaoCancelar.place(relx=0.7, rely=0.8, relheight=0.08, relwidth=0.2)


        
