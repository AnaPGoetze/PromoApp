from tkinter import *
from tkinter import ttk
from Controll.mapa import MapaSantaCruzDoSul

# Modificação na classe TelaExplorar
class TelaExplorar:
    #Construtor
    def __init__(self, janela):
        self.janela = Toplevel(janela)
        self.janela.title("Explorar")
        self.janela.geometry("700x800")
        #self.listaPromocoes()
        self.adicionarTitulo()
        self.criar_botao_mapa()

    #Criar um frame com uma label com o titulo remover promoção
    def adicionarTitulo(self):
        self.frame = Frame(self.janela)
        self.frame.configure(background="white", borderwidth=2, relief="solid")
        self.frame.place(relx=0.35, rely=0.03, relheight=0.05, relwidth=0.3)
        #Label de titulo com fonte arial 20 e cor azul
        self.lb = Label(self.frame, text="Explorar", background="white", font=("Arial", 20))
        self.lb.place(relx=0.08, rely=0.1, relheight=0.8, relwidth=0.9)

    #Criar uma tabela com as promoções que estão no banco de dados, para o usuario poder navegar
    '''
    def listaPromocoes(self):
        self.listaPromo=ttk.Treeview(self.janela, columns=('Local', 'Descrição'), show='headings')

        self.listaPromo.heading('#1', text='Local')
        self.listaPromo.heading('#2', text='Descrição')

        self.listaPromo.column('#1', width=100)
        self.listaPromo.column('#2', width=100)

        self.listaPromo.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)  # Add this line

        #Colocar o scrollbar da tabela
        self.scrollbar = Scrollbar(self.janela, orient="vertical", command=self.listaPromo.yview)
        self.listaPromo.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=0.9, rely=0.1, relheight=0.8, relwidth=0.02)

        self.botoes()
    '''

    def criar_botao_mapa(self):
        self.botao_mapa = Button(self.janela, text="Abrir Mapa", command=self.abrir_mapa)
        self.botao_mapa.place(relx=0.1, rely=0.9, relheight=0.05, relwidth=0.8)

    def abrir_mapa(self):
        self.mapa = MapaSantaCruzDoSul()
        self.mapa.open_map()


    #Adicionar o botão de voltar
    def botoes(self):
        self.botao = Button(self.janela, text="Voltar", command=self.janela.destroy)
        self.botao.place(relx=0.1, rely=0.9, relheight=0.05, relwidth=0.8)