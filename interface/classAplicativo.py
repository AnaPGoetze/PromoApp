from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


root = Tk()

    #Chamada das funções, e definir as propriedades da janela
class aplicativo():
    def __init__(self):

        self.root  = root
        self.tela()
        self.frames()
        self.botoes()
        self.inserirLogo()
        self.addTitulo()
        root.mainloop()


    #Vai definir a cor de fundo e o tamanho da janela
    def tela(self):
        self.root.title("Promo App")
        #Background roxo claro
        self.root.configure(background="#7120b8")
        self.root.geometry("940x1000")


    #Definir as propriedades dos frames
    def frames(self):
    
        self.frame_1 = Frame(self.root, bd=4, bg="#8c17f1", highlightbackground="black", highlightthickness=3)
        self.frame_1.place(relx=0.1, rely=0.1, relwidth=0.80, relheight=0.80)


    #Função do botão adicionar promoção, ele vai abrir uma nova janela
    def funcAdPromo(self):
        self.newWindow = Toplevel(self.root)
        self.newWindow.geometry("720x620")
        self.newWindow.title("Adicionar promoção")

        #Dentro da nova janela, vai ser criado uma entry, para inserir as informações da promoção

        #Nome do estabelecimento
        self.lb_nomeLocal = Label(self.newWindow, text="Digite o nome do estabelecimento:")
        self.lb_nomeLocal.place(relx=-0.06, rely=0.01, relwidth=0.40, relheight=0.06)
        self.codigo_entry = Entry(self.newWindow)
        self.codigo_entry.place(relx=0.01, rely=0.09, relwidth=0.98, relheight=0.06)

        #Endereço do estabelecimento
        self.lb_endLocal = Label(self.newWindow, text="Endereço do estabelecimento:")
        self.lb_endLocal.place(relx=-0.076, rely=0.17, relwidth=0.40, relheight=0.06)
        self.codigo_entry = Entry(self.newWindow)
        self.codigo_entry.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.06)

        #Nome do produto
        self.lb_produto = Label(self.newWindow, text="Nome do produto:")
        self.lb_produto.place(relx=-0.12, rely=0.33, relwidth=0.40, relheight=0.06)
        self.codigo_entry = Entry(self.newWindow)
        self.codigo_entry.place(relx=0.01, rely=0.41, relwidth=0.98, relheight=0.06)

        #Valor padrão do produto
        self.lb_valorPadrao = Label(self.newWindow, text="Valor padrão do produto:")
        self.lb_valorPadrao.place(relx=-0.096, rely=0.49, relwidth=0.40, relheight=0.06)
        self.codigo_entry = Entry(self.newWindow)
        self.codigo_entry.place(relx=0.01, rely=0.57, relwidth=0.98, relheight=0.06)

        #Valor com desconto do produto
        self.lb_valorComDesconto = Label(self.newWindow, text="Valor com desconto do produto:")
        self.lb_valorComDesconto.place(relx=-0.07, rely=0.65, relwidth=0.40, relheight=0.06)
        self.codigo_entry = Entry(self.newWindow)
        self.codigo_entry.place(relx=0.01, rely=0.73, relwidth=0.98, relheight=0.06)

        ######################## Botão de confirmar e cancelar ########################

        self.bt_confirmar = Button(self.newWindow, text="Confirmar")
        self.bt_confirmar.place(relx=0.04, rely=0.85, relwidth=0.40, relheight=0.06)

        #Botão cancelar vai fechar a janela
        self.bt_cancelar = Button(self.newWindow, text="Cancelar", command=self.newWindow.destroy)
        self.bt_cancelar.place(relx=0.55, rely=0.85, relwidth=0.40, relheight=0.06)


    #Função para remover promoção
    def removerPromo(self):
        self.newWindow = Toplevel(self.root)
        self.newWindow.geometry("720x620")
        self.newWindow.title("Remover promoção")

        #Aba para digitar o nome do estabelecimento 
        self.lb_nomeLocal = Label(self.newWindow, text="Digite o nome do estabelecimento:")
        self.lb_nomeLocal.place(relx=-0.06, rely=0.01, relwidth=0.40, relheight=0.06)
        self.codigo_entry = Entry(self.newWindow)
        self.codigo_entry.place(relx=0.01, rely=0.09, relwidth=0.98, relheight=0.06)

        #Aba para digitar o nome do produto
        self.lb_produto = Label(self.newWindow, text="Nome do produto:")
        self.lb_produto.place(relx=-0.12, rely=0.17, relwidth=0.40, relheight=0.06)
        self.codigo_entry = Entry(self.newWindow)
        self.codigo_entry.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.06)

        #Label para informar uma segunda opção de inserção de dados
        frame_info = Frame(self.newWindow, bd=4, bg="white", highlightbackground="black", highlightthickness=1)
        frame_info.place(relx=0.35, rely=0.45, relwidth=0.30, relheight=0.06)
        label_info = Label(frame_info, text="Ou")
        label_info.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        #Aba para digitar o ID de venda do produto
        self.lb_idVenda = Label(self.newWindow, text="ID de venda:")
        self.lb_idVenda.place(relx=-0.14, rely=0.62, relwidth=0.40, relheight=0.06)
        self.codigo_entry = Entry(self.newWindow)
        self.codigo_entry.place(relx=0.01, rely=0.7, relwidth=0.98, relheight=0.06)

        #Botão de confirmar e cancelar
        self.bt_confirmar = Button(self.newWindow, text="Confirmar")
        self.bt_confirmar.place(relx=0.04, rely=0.85, relwidth=0.40, relheight=0.06)

        #Botão cancelar vai fechar a janela
        self.bt_cancelar = Button(self.newWindow, text="Cancelar", command=self.newWindow.destroy)
        self.bt_cancelar.place(relx=0.55, rely=0.85, relwidth=0.40, relheight=0.06)


    #Adicionar o titilo do app
    def addTitulo(self):
        self.lb_titulo = Label(self.frame_1, text="Promo App", font="Arial 20 bold", bg="#8c17f1", highlightbackground="black", highlightthickness=3)
        self.lb_titulo.place(relx=0.3, rely=0.01, relwidth=0.40, relheight=0.06)


    #Criar os botões
    def botoes(self):
        self.bt_Adicionar = Button(self.frame_1, text="Adicionar promoção", command=self.funcAdPromo)
        self.bt_Adicionar.place(relx=0.24, rely=0.2, relwidth=0.17, relheight=0.10)

        self.bt_RemoverPromo = Button(self.frame_1, text="Remover promoção", command=self.removerPromo)
        self.bt_RemoverPromo.place(relx=0.6, rely=0.2, relwidth=0.17, relheight=0.10)

        self.bt_BuscaPromo = Button(self.frame_1, text="Buscar promoções", command=self.buscarPromo)
        self.bt_BuscaPromo.place(relx=0.15, rely=0.1, relwidth=0.70, relheight=0.05)

        self.bt_IrHome = Button(self.frame_1, text="Home")
        self.bt_IrHome.place(relx=0.1, rely=0.88, relwidth=0.10, relheight=0.10)

        self.bt_IrAtividades = Button(self.frame_1, text="Ver mais tarde")
        self.bt_IrAtividades.place(relx=0.4, rely=0.88, relwidth=0.2, relheight=0.10)

        self.bt_IrConfig = Button(self.frame_1, text="Explorar", command=self.explorar)
        self.bt_IrConfig.place(relx=0.8, rely=0.88, relwidth=0.10, relheight=0.10)


    def buscarPromo(self):
        self.newWindow = Toplevel(self.root)
        self.newWindow.geometry("720x620")
        self.newWindow.title("Buscar promoção")

        #Dentro da nova janela, vai ser criado uma aba de busca de promoções
        self.lb_busca = Label(self.newWindow, text="Digite o produto ou estabelecimento que deseja procurar:")
        self.lb_busca.place(relx=0.16, rely=0.4, relwidth=0.7, relheight=0.06)
        self.codigo_entry = Entry(self.newWindow)
        self.codigo_entry.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.06)

        #Botão de confirmar e cancelar
        self.bt_confirmar = Button(self.newWindow, text="Confirmar")
        self.bt_confirmar.place(relx=0.04, rely=0.85, relwidth=0.40, relheight=0.06)

        #Botão cancelar vai fechar a janela
        self.bt_cancelar = Button(self.newWindow, text="Cancelar", command=self.newWindow.destroy)
        self.bt_cancelar.place(relx=0.55, rely=0.85, relwidth=0.40, relheight=0.06)

    #Funcionalidade do botão explorar, o botão explorar vai chamar esta função
    def explorar(self):
        # Crie um Frame para o conteúdo da tela
        self.frame_explorar = Frame(self.root)
        self.frame_explorar.pack(fill=BOTH, expand=True)
        self.frame_explorar.config(background="#7120b8")

        self.frame_explorar.pack_forget()
        self.frame_explorar.pack(fill=BOTH, expand=True)

        #Frame para adicionar conteudo na tela
        self.frame_2 = Frame(self.frame_explorar, bd=4, bg="#8c17f1", highlightbackground="black", highlightthickness=3)
        self.frame_2.place(relx=0.1, rely=0.1, relwidth=0.80, relheight=0.80)

        self.lb_titulo = Label(self.frame_2, text="Explorar")
        self.lb_titulo.place(relx=0.3, rely=0.01, relwidth=0.40, relheight=0.06)

        self.bt_IrHome = Button(self.frame_2, text="Home", command=self.voltarPaginaInicial)
        self.bt_IrHome.place(relx=0.1, rely=0.88, relwidth=0.2, relheight=0.10)

        self.bt_IrAtividades = Button(self.frame_2, text="Ver mais tarde")
        self.bt_IrAtividades.place(relx=0.7, rely=0.88, relwidth=0.2, relheight=0.10)

        self.listaPromoExplorar()


    def listaPromoExplorar(self):
        self.lista_promo = ttk.Treeview(self.frame_2, columns=("Local", "Endereço", "Produto", "Preço", "Preço Promocional"), show='headings')
        self.lista_promo.heading("#1", text="Local")
        self.lista_promo.heading("#2", text="Endereço")
        self.lista_promo.heading("#3", text="Produto")
        self.lista_promo.heading("#4", text="Preço")
        self.lista_promo.heading("#5", text="Preço Promocional")

        self.lista_promo.column("#1", width=100)
        self.lista_promo.column("#2", width=100)
        self.lista_promo.column("#3", width=100)
        self.lista_promo.column("#4", width=100)
        self.lista_promo.column("#5", width=100)

        self.lista_promo.place(relx=0.01, rely=0.1, relwidth=0.97, relheight=0.70)

        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_promo.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.98, rely=0.1, relwidth=0.02, relheight=0.70)



    #O botão home vai voltar para a tela inicial
    def voltarPaginaInicial(self):
        self.frame_explorar.pack_forget()
        self.root.pack(fill=BOTH, expand=True)
        self.frame_1.pack(fill=BOTH, expand=True)


    def inserirLogo(self):
        imagem = Image.open("D:\PROGRAMAÇÃO\codigos]\Software\Python\Teste TKINTER\ex\imagens\LogoPromoApp.png")
        imagem_tk = ImageTk.PhotoImage(imagem)

        self.logo = Label(self.frame_1, image=imagem_tk)
        self.logo.image = imagem_tk  # Manter uma referência à imagem
        self.logo.place(relx=0.5, rely=0.5, anchor="center")

aplicativo()

