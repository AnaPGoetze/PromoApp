import folium
import tkinter as tk
import webbrowser
import pandas as pd

# ------------------------/ Código do mapa de Santa Cruz do Su

engine = create_engine('mysql+msqlconnector://usuario:senha@localhost/database_name')

df = pd.read_sql_query("SELECT LOCAL, LATITUDE, LONGITUDE, DESCRICAO FROM temp_data", con=engine)

class MapaSantaCruzDoSul:
    def __init__(self, arquivo_excel='pontos_santacruz.xlsx'):
        # Setta a localização de Sta. Cruz do Sul e define o zoom start
        self.mapa = folium.Map(location=[-29.71886949612006, -52.42644538100079], zoom_start=15)
        # Lê os waypoints presentes no excel
        self.df = pd.read_excel(arquivo_excel)

        # Imprime as informções no mapa
        for index, row in self.df.iterrows():
            popup = "<b>" + row['LOCAL'] + "</b><br>" + "<u>" + row['DESCRICAO'] + "</u>"

            # Configuração dos marcadores
            folium.Marker(
                location = [row['LATITUDE'], row['LONGITUDE']],
                popup = popup,
                icon = folium.Icon(color='purple', icon='info-sign')
            ).add_to(self.mapa)

        # Salva o mapa em html
        self.mapa.save("mapa_santacruz.html")

    # ------------------------/ Abre o mapa em html em uma nova guia no navegador
    def open_map(self):
        webbrowser.open_new_tab("mapa_santacruz.html")

# ------------------------/ Parte do Tkinter
def button1_action():
    # Abre o mapa ao clicar no botão 1
    mapa = MapaSantaCruzDoSul()
    mapa.open_map()

def button2_action():
    print("Início")

def button3_action():
    print("Usuário")

# Configuração da janela principal
root = tk.Tk()
root.title("Tela de Celular")
root.geometry("341x643")  # Largura x Altura
root.resizable(False, False)  # Impedindo redimensionamento

# Define a cor de fundo
root.configure(bg="#e6e6e6")

# Cria o cabeçalho
cabecalho = tk.Frame(root, bg="#663399", height=60)
cabecalho.pack(fill="x")

# Adiciona o logotipo
logotipo = tk.Label(cabecalho, text="PromoTour", fg="white", bg="#663399", font=("Arial", 16, "bold"))
logotipo.pack(pady=10)

# Adiciona o ícone de configurações (dentro do cabeçalho) => acho que ta dando pobrema
#config_icon = tk.Label(cabecalho, text="⚙️", fg="grey", font=("Arial", 14))
#config_icon.pack(side="right", padx=10)


frame_promocoes = tk.Frame(root, bg="#e6e6e6")
frame_promocoes.pack(pady=10)

frame_promocoes.columnconfigure(0, weight=1)  # Define o peso da coluna 0 como 1
frame_promocoes.columnconfigure(1, weight=1)  # Define o peso da coluna 1 como 1

# Cria os botões de promoções
for i in range(4):
    promocao = tk.Frame(frame_promocoes, bg="white", borderwidth=1, relief="solid",
                        width=300, height=80)  # Ajuste a altura
    promocao.grid(row=i, columnspan=2, sticky="ew", pady=5)  # Use grid para posicionar

    # Adiciona a caixa de cor
    cor_promocao = tk.Label(promocao, bg="#B39DDB", width=5, height=3)
    cor_promocao.grid(row=0, column=0, padx=10)

    # Adiciona o texto da promoção
    texto_promocao = tk.Label(promocao, text=f"Loja {i+1}\nPromoções", font=("Arial", 12))
    texto_promocao.grid(row=0, column=1, padx=10, pady=10)

# Cria os botões de navegação
botoes_navegacao = tk.Frame(root, bg="#e6e6e6")
botoes_navegacao.pack(side="bottom", pady=10)

# Criando um frame para os botões na parte inferior
button_frame = tk.Frame(root, bg="white")
button_frame.pack(side="bottom", fill=tk.X)

# Adicionando os botões ao frame
button1 = tk.Button(button_frame, text="Mostrar mapa", command=button1_action)
button1.pack(side="left", fill=tk.X, expand=True)

button2 = tk.Button(button_frame, text="Início", command=button2_action)
button2.pack(side="left", fill=tk.X, expand=True)

button3 = tk.Button(button_frame, text="Usuário", command=button3_action)
button3.pack(side="left", fill=tk.X, expand=True)

# Iniciar o loop principal
root.mainloop()