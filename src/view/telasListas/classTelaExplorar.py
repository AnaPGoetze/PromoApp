from tkinter import *
from tkinter import ttk

from src.controller.planilha import Planilha


# Modificação na classe TelaExplorar
class TelaExplorar:
    def __init__(self, janela):
        self.janela = Toplevel(janela)
        self.janela.title("Explorar")
        self.janela.geometry("700x800")
        self.lista_promocoes(Planilha().copiarPlanilha())
        self.adicionar_titulo()

    # Criar um frame com uma label com o titulo remover promoção
    def adicionar_titulo(self):
        self.frame = Frame(self.janela)
        self.frame.configure(background="white", borderwidth=2, relief="solid")
        self.frame.place(relx=0.35, rely=0.03, relheight=0.05, relwidth=0.3)
        # Label de titulo com fonte arial 20 e cor azul
        self.lb = Label(self.frame, text="Explorar", background="white", font=("Arial", 20))
        self.lb.place(relx=0.08, rely=0.1, relheight=0.8, relwidth=0.9)

    # Criar uma tabela com as promoções que estão no banco de dados, para o usuario poder navegar
    def lista_promocoes(self, copia):
        self.listaPromo = ttk.Treeview(self.janela, columns=('Local', 'Produto', 'Desconto'), show='headings')

        self.listaPromo.heading('#1', text='Local')
        self.listaPromo.heading('#2', text='Produto')
        self.listaPromo.heading('#3', text='Desconto')

        self.listaPromo.column('#1', width=100)
        self.listaPromo.column('#2', width=100)
        self.listaPromo.column('#3', width=40)

        self.listaPromo.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)  # Add this line

        # Colocar o scrollbar da tabela
        self.scrollbar = Scrollbar(self.janela, orient="vertical", command=self.listaPromo.yview)
        self.listaPromo.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=0.9, rely=0.1, relheight=0.8, relwidth=0.02)

        # Adicionar os valores da copia da planilha, da class planilha na treeview
        for i in range(len(copia)):
            self.listaPromo.insert("", 'end', values=(copia[i][0], copia[i][1], copia[i][2]))

        self.botoes()

    # Adicionar o botão de voltar
    def botoes(self):
        self.botao = Button(self.janela, text="Voltar", command=self.janela.destroy)
        self.botao.place(relx=0.1, rely=0.9, relheight=0.05, relwidth=0.8)
