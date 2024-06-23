from IPython.display import display #Javascript
from Mapas import Mapas

# Função para exibir o menu
def menu():
    print("\n╔═══════════[ Menu ]═══════════╗")
    print("║(1) Exibir Mapa               ║")
    print("║(2) Adicionar Local           ║")
    print("║(3) Listar pontos registrados ║")
    print("║(4) Buscar Waypoint           ║")
    print("║(5) Atualizar Waypoint        ║")
    print("║(9) {Remover Waypoint}        ║")
    print("║(0) Sair                      ║")
    print("╚══════════════════════════════╝")

if __name__ == "__main__":
  mapa = Mapas()

  while True:
    menu()
    op = input("\n> ")

    # Mostrar Mapa
    if op == '1':
      display(mapa.mostrar_mapa())

    # Adicinar Local
    elif op == '2':
      local = input("Nome do local: ")
      lat = float(input("Latitude: "))
      lon = float(input("Longitude: "))
      desc = input("Descrição: ")
      mapa.adicionar_local(local, lat, lon, desc)
      print("Local adicionado com sucesso!")

    # Listar pontos registrados
    elif op == '3':
      mapa.listar_waypoints()

    # Buscar Waypoint
    elif op == '4':
      local = input("Nome do local: ")
      waypoint = mapa.buscar_waypoint(local)
      if waypoint:
        print(f"Local: {local}")
        print(f"Latitude: {waypoint['latitude']}")
        print(f"Longitude: {waypoint['longitude']}")
        print(f"Descrição: {waypoint['descricao']}")
      else:
        print("Local não encontrado.")

    # Atualizar Waypoint
    elif op == '5':
      local = input("Nome do local: ")
      nova_desc = input("Nova descrição: ")
      mapa.atualizar_waypoint(local, None, None, nova_desc)
      print("Local atualizado com sucesso!")

    # Remover Waypoint
    elif op == '9':
      local = input("Nome do local: ")
      mapa.remover_waypoint(local)
      print("Local removido com sucesso!")

    # Sair
    elif op == '0':
      print("Saindo...")
      break

    else:
      print("Opção inválida!")