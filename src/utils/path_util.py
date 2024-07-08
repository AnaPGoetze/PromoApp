from pathlib import Path


class PathUtil:
    def __init__(self):
        self.logo = Path('assets/img/LogoPromoApp.png')
        self.mapa = Path('assets/misc/mapa_promocoes.html')
        self.planilha_promocao = Path('assets/planilhas/promocoes.xlsx')


path = PathUtil()
