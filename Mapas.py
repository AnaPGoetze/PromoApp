import folium
from folium.plugins import Geocoder #AntPath
import pandas as pd

class Mapas:
    def __init__(self, arquivo_excel='pontos_santacruz.xlsx'):
        self.mapa = folium.Map(location=[-29.71886949612006, -52.42644538100079], zoom_start=15)
        self.df = pd.read_excel(arquivo_excel)
        self.df.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
        self.adicionar_marcadores()
        self.adicionar_geocoder()

    # Função para adicionar as "lojas"
    def adicionar_marcadores(self):
        for local, lat, lon, desc in zip(self.df.LOCAL, self.df.LATITUDE.values, self.df.LONGITUDE.values, self.df.DESCRICAO.values):
            html = f"""
            <strong>{local}</strong><br>
            {desc}<br>
            """
            # Configuração do ícone do waypoint
            folium.Marker(
                [lat, lon],
                popup=folium.Popup(html, max_width=250),
                icon=folium.Icon(color='purple', icon='info-sign')
            ).add_to(self.mapa)

    # Essa função não está funcionando (JavaScript)
    def adicionar_geocoder(self):
      Geocoder(position='topleft').add_to(self.mapa)

    # Lista todas as "lojas" presentes no arquivo xlsx
    def listar_waypoints(self):
      for index, row in self.df.iterrows():
        local = row['LOCAL']
        desc = row['DESCRICAO']
        print(f"{local}: - {desc}")
        print("-" * 80)

    # Adiciona uma "loja" na planilha
    def adicionar_local(self, local, lat, lon, desc):
      new_row = pd.DataFrame({
          'LOCAL': [local],
          'LATITUDE': [lat],
          'LONGITUDE': [lon],
          'DESCRICAO': [desc]
      })
      updated_dataframe = pd.concat([self.df, new_row], ignore_index=True)

      # Salva o dataframe atualizado de volta à planilha
      updated_dataframe.to_excel('pontos_santacruz.xlsx', index=False)

      self.df = pd.concat([self.df, new_row], ignore_index=True)
      self.df.to_excel('pontos_santacruz.xlsx', index=False)
      self.df = updated_dataframe
      self.adicionar_marcadores()

      return updated_dataframe

    # Busca uma "loja" específica, passando o nome da "loja"
    def buscar_waypoint(self, local):
      waypoint = self.df[self.df['LOCAL'] == local]
      if not waypoint.empty:
        return {
            'latitude': waypoint['LATITUDE'].values[0],
            'longitude': waypoint['LONGITUDE'].values[0],
            'descricao': waypoint['DESCRICAO'].values[0]
        }
      return None

    # Remove uma "loja" da planilha
    def remover_waypoint(self, local):
      self.df = self.df[self.df['LOCAL'] != local]
      self.df.to_excel('pontos_santacruz.xlsx', index = False)

    # Atualiza a descrição (descontos) de uma "loja"
    def atualizar_waypoint(self, local, novo_lat, novo_lon, nova_desc):
      self.df.loc[self.df['LOCAL'] == local, ['DESCRICAO']] = [nova_desc]
      self.df.to_excel('pontos_santacruz.xlsx', index = False)
      self.df = pd.read_excel('pontos_santacruz.xlsx')

    # Função para exibir o mapa com os waypoints (lojas)
    def mostrar_mapa(self):
      return self.mapa

