from tkinter import *
from tkinter import ttk
from Controll.funcoesSql import *

class TelaVerMaisTarde:

    #Construtor
    def __init__(self, janela):
        self.janela = Toplevel(janela)
        self.janela.title("Ver mais tarde")
        self.janela.geometry("700x800")
        self.listaVermaistarde()
        self.adicionarTitulo()
        self.listaVermaistarde()

    #Criar um frame com uma label com o titulo remover promoção
    def adicionarTitulo(self):
        self.frame = Frame(self.janela)
        self.frame.configure(background="white", borderwidth=2, relief="solid")
        self.frame.place(relx=0.35, rely=0.03, relheight=0.05, relwidth=0.3)
        #Label de titulo com fonte arial 20 e cor azul
        self.lb = Label(self.frame, text="Ver mais tarde", background="white", font=("Arial", 20))
        self.lb.place(relx=0.07, rely=0.1, relheight=0.8, relwidth=0.9)

    #Adicionar o botão de voltar
    def botoes(self):
        self.botao = Button(self.janela, text="Voltar", command=self.janela.destroy)
        self.botao.place(relx=0.1, rely=0.9, relheight=0.05, relwidth=0.8)

    #Adiciona a lista para guardar as promoções que o usuario marcou para ver mais tarde
    def listaVermaistarde(self):
        self.listaPromo=ttk.Treeview(self.janela, columns=('Local', 'Descrição'), show='headings')

        self.listaPromo.heading('#1', text='Local')
        self.listaPromo.heading('#2', text='Descrição')

        self.listaPromo.column('#1', width=100)
        self.listaPromo.column('#2', width=100)

        self.listaPromo.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        #Colocar o scrollbar da tabela
        self.scrollbar = Scrollbar(self.janela, orient="vertical", command=self.listaPromo.yview)
        self.listaPromo.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=0.9, rely=0.1, relheight=0.8, relwidth=0.02)

        registros = funcoesSql.listarDadosNoSQLite()
        for local, descricao in registros:
            self.listaPromo.insert("", tk.END, values=(local, descricao))

        self.botoes()