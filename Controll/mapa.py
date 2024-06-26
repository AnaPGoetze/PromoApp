import folium
import webbrowser
from Controll.funcoesSql import *

# ------------------------/ Classe do mapa de Santa Cruz do Sul
class MapaSantaCruzDoSul:
    def __init__(self):
        funcoesSql.criarBancodeDados(self)

        # lê os dados do banco de dados
        self.df = pd.read_sql_query("SELECT * FROM temp_data",
                                    sqlite3.connect('C:\\SQLite\\testemapa.db'))

        # setta a posição inicial e o zoom
        self.mapa = folium.Map(location=[-29.71886949612006, -52.42644538100079], zoom_start=15)

        # configuração dos marcadores
        for index, row in self.df.iterrows():
            popup = "<b>" + row['LOCAL'] + "</b><br>" + "<u>" + row['DESCRICAO'] + "</u>"

            # Configuração dos marcadores
            folium.Marker(
                location=[row['LATITUDE'], row['LONGITUDE']],
                popup=popup,
                icon=folium.Icon(color='purple', icon='info-sign')
            ).add_to(self.mapa)

         # Salva o mapa em html
        self.mapa.save("mapa_santacruz.html")

    # ------------------------/ Abre o mapa em html em uma nova guia no navegador
    def open_map(self):
        webbrowser.open_new_tab("mapa_santacruz.html")