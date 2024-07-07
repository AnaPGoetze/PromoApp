from tkinter import *
from tkinter import ttk

#Importar class planilha, para utilizar a def procurarPromoPlanilha, para utilizar no botão procurar
from Controll.planilha import Planilha
class TelaPesquisa:
    # Construtor
    def __init__(self, janela):
        self.janela = Toplevel(janela)
        self.janela.title("Pesquisar")
        self.janela.geometry("600x600")
        self.criarWidget()
        self.adicionarTitulo()


    # Criar uma frame com uma label com o titulo remover promoção
    def adicionarTitulo(self):
        self.frame = Frame(self.janela)
        self.frame.configure(background="white", borderwidth=2, relief="solid")
        self.frame.place(relx=0.35, rely=0.02, relheight=0.1, relwidth=0.3)
        # Label de titulo com fonte arial 20 e cor azul
        self.lb = Label(self.frame, text="Pesquisar", background="white", font=("Arial", 20))
        self.lb.place(relx=0.08, rely=0.1, relheight=0.8, relwidth=0.9)


    #def utilizando a função da class planilha, vai buscar todas as promos que tiverem o produto ou parte do produto, na planilha, e vai ser inserido em uma copia, e colocado na treeview
    def procurarPromo(self):
        copia = Planilha().procurarPromoOupartePlanilha(self.entryPesquisa.get())
        for promo in copia:
            self.listaPromo.insert("", "end", values=promo)





# Criar labels e entry para inserir os dados da promoção a ser pesquisada
    def criarWidget(self):
        self.lbPesquisa = Label(self.janela, text="Digite o produto que procura:")
        self.lbPesquisa.place(relx=0.1, rely=0.15, relheight=0.05, relwidth=0.8)
        self.entryPesquisa = Entry(self.janela)
        self.entryPesquisa.place(relx=0.1, rely=0.2, relheight=0.05, relwidth=0.8)

        self.botao = Button(self.janela, text="Pesquisar", command=self.procurarPromo)
        self.botao.place(relx=0.1, rely=0.9, relheight=0.08, relwidth=0.2)

        self.botaoCancelar = Button(self.janela, text="Cancelar", command=self.janela.destroy)
        self.botaoCancelar.place(relx=0.7, rely=0.9, relheight=0.08, relwidth=0.2)

        ################################## Criação da treeview #####################################
        self.listaPromo=ttk.Treeview(self.janela, columns=("Local", "Produto", "Desconto"), show='headings')

        self.listaPromo.heading('#1', text='Local')
        self.listaPromo.heading('#2', text='Produto')
        self.listaPromo.heading('#3', text='Desconto')

        self.listaPromo.column('#1', width=100)
        self.listaPromo.column('#2', width=100)
        self.listaPromo.column('#3', width=40)

        self.listaPromo.place(relx=0.1, rely=0.3, relheight=0.6, relwidth=0.8)

        #Colocar o scrollbar da tabela
        self.scrollbar = Scrollbar(self.janela, orient="vertical", command=self.listaPromo.yview)
        self.listaPromo.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=0.9, rely=0.1, relheight=0.8, relwidth=0.02)








