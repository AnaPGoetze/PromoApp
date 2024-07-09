# importação das bibliotecas
import folium

from src.controller.planilha import Planilha
from src.utils.path_util import path


# classe mapa
class Mapa:

    # construtor
    def __init__(self):
        # configuração da localização inicial e zoom
        self.mapa = folium.Map(location=[-29.71886949612006, -52.42644538100079], zoom_start=15)
        self.planilha = Planilha()

    # função para adicionar os marcadores
    def adicionar_marcadores(self):
        ws = self.planilha.lerPlanilha()

        # prints para depuração
        # print("Lendo dados da planilha:")
        for row in ws.iter_rows(min_row=2, values_only=True):
            nome_local = row[0]
            nome_produto = row[1]
            desconto = row[2]
            latitude = row[3]
            longitude = row[4]

            # verifica se todos os campos necessários estão presentes
            if None in (nome_local, nome_produto, desconto, latitude, longitude):
                # print(f"Dados incompletos: {row}")
                continue

            # para depuração, remover posteriormente
            # print(f"Nome Local: {nome_local}, Produto: {nome_produto}, Desconto: {desconto}, Latitude: {latitude}, Longitude: {longitude}")

            # Configuração do texto
            html = f"""
            <strong>{nome_local}</strong><br>
            Produto: {nome_produto}<br>
            Desconto: {desconto}
            """
            popup = folium.Popup(html, max_width=250)

            # Configuração dos marcadores
            marker = folium.Marker(
                [latitude, longitude],
                popup=popup,
                icon=folium.Icon(color='blue', icon='info-sign')
            )
            marker.add_to(self.mapa)

            # para depuração, remover posteriormente
            # print(f"Marcador adicionado: {marker}")

    # função para salvar o mapa em html
    def salvar_mapa(self, nome_arquivo=path.mapa):
        self.mapa.save(nome_arquivo)

    # função para atualizar o mapa
    def atualizar_mapa(self):
        # reinicializa o mapa
        self.mapa = folium.Map(location=[-29.71886949612006, -52.42644538100079], zoom_start=15)
        # adiciona marcadores novamente
        self.adicionar_marcadores()
        # salva o mapa atualizado
        self.salvar_mapa()
