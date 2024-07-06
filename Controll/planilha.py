import openpyxl

class Planilha:
    def __init__(self):
        try:
            self.wb = openpyxl.load_workbook("promocoes.xlsx")
            self.ws = self.wb.active
        except FileNotFoundError:
            self.wb = openpyxl.Workbook()
            self.ws = self.wb.active
            self.ws.title = "Promos"
            self.ws.append(["Local", "Latitude", "Longitude"])
            self.wb.save("promocoes.xlsx")

    def inserirPlanilha(self, nome_local, latitude, longitude):
        self.ws.append([nome_local, latitude, longitude])
        self.wb.save("promocoes.xlsx")


    def lerPlanilha(self):
        return self.ws

    def fecharPlanilha(self):
        self.wb.close()
