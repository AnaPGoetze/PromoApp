from tkinter import *

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
        self.root.configure(background="purple")
        self.root.geometry("940x1000")

    #Definir as propriedades dos frames
    def frames(self):
        #Frame 1 vai ser roxo claro
        self.frame_1 = Frame(self.root, bd=4, bg="", highlightbackground="black", highlightthickness=3)
        self.frame_1.place(relx=0.1, rely=0.1, relwidth=0.80, relheight=0.80)

    #Função do botão adicionar promoção, ele vai abrir uma nova janela
    def funcAdPromo(self):
        self.newWindow = Toplevel(self.root)
        self.app = AdicionarPromo(self.newWindow)
        #mudar a dimenção da nova janela para 820x400
        self.newWindow.geometry("1240x720")

        #Dentro desta nova tela, vamos colocar uma label com o titulo de nome do estabelecimento
        self.lb_estabelecimento = Label(self.newWindow, text="Nome do estabelecimento")
        self.lb_estabelecimento.place(relx=0.1, rely=0.1)

    #Adicionar o titilo do app
    def addTitulo(self):
        self.lb_titulo = Label(self.frame_1, text="Promo App")
        self.lb_titulo.place(relx=0.3, rely=0.01, relwidth=0.40, relheight=0.06)


    #Criar os botões
    def botoes(self):
        self.bt_Adicionar = Button(self.frame_1, text="Adicionar promoção", command=self.funcAdPromo)
        self.bt_Adicionar.place(relx=0.24, rely=0.2, relwidth=0.17, relheight=0.10)

        self.bt_RemoverPromo = Button(self.frame_1, text="Remover promoção")
        self.bt_RemoverPromo.place(relx=0.6, rely=0.2, relwidth=0.17, relheight=0.10)

        self.bt_BuscaPromo = Button(self.frame_1, text="Buscar promoções")
        self.bt_BuscaPromo.place(relx=0.15, rely=0.1, relwidth=0.70, relheight=0.05)

        self.bt_IrHome = Button(self.frame_1, text="Home")
        self.bt_IrHome.place(relx=0.1, rely=0.88, relwidth=0.10, relheight=0.10)

        self.bt_IrAtividades = Button(self.frame_1, text="Atividades")
        self.bt_IrAtividades.place(relx=0.45, rely=0.88, relwidth=0.10, relheight=0.10)

        self.bt_IrConfig = Button(self.frame_1, text="Config")
        self.bt_IrConfig.place(relx=0.8, rely=0.88, relwidth=0.10, relheight=0.10)

    def inserirLogo(self):
        try:
            self.logo_image = PhotoImage(file="ex\imagens\LogoPromoApp.png") # Carrega a imagem
            self.logo_image = self.logo_image.zoom(1, 1) # Aplica zoom à imagem
            self.logo = Label(self.root, image=self.logo_image) # Cria um widget Label com a imagem carregada
            self.logo.image = self.logo_image  # Manter uma referência à imagem
            self.logo.place(relx=0.45, rely=0.45) # Posiciona a imagem
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")

aplicativo()
"""
            imagem = Image.open("imagens/LogoPromoApp.png")
            imagem_tk = ImageTk.PhotoImage(imagem)
            
            self.logo = Label(self.root, image=imagem_tk)
            self.logo.image = imagem_tk  # Manter uma referência à imagem
            self.logo.place(relx=0.2, rely=0.2)
"""
