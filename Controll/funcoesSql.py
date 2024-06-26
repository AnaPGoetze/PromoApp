import pandas as pd
import sqlite3

# ------------------------/ Funções relacionadas ao banco de dados

class funcoesSql:
    def criarBancodeDados(self):
        # cria o banco de dados e a tabela se não existirem
        conn = sqlite3.connect('C:\\SQLite\\testemapa.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS temp_data (
            LOCAL TEXT,
            LATITUDE REAL,
            LONGITUDE REAL,
            DESCRICAO TEXT
        )''')

        conn.commit()
        conn.close()


    def inserirDadosNoSQLite(local, latitude, longitude, descricao, nome_tabela='temp_data'):
        # insere novas "lojas" no banco de dados
        conn = sqlite3.connect('C:\\SQLite\\testemapa.db')
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO {nome_tabela} VALUES (?, ?, ?, ?)"
                       , (local, latitude, longitude, descricao))

        conn.commit()
        conn.close()

    def editarDadosNoSQLite(local, nova_descricao, nome_tabela='temp_data'):
        # edita a descrição de um local no banco de dados
        conn = sqlite3.connect('C:\\SQLite\\testemapa.db')
        cursor = conn.cursor()  # Corrigido: conn.cursor()

        cursor.execute(f"UPDATE {nome_tabela} SET DESCRICAO = ? WHERE LOCAL = ?", (nova_descricao, local))

        conn.commit()
        conn.close()

    def excluirDadosNoSQLite(local, nome_tabela='temp_data'):
        # exclui um local do banco de dados
        conn = sqlite3.connect('C:\\SQLite\\testemapa.db')
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM {nome_tabela} WHERE LOCAL = ?", (local,))

        conn.commit()
        conn.close()

    def listarDadosNoSQLite(nome_tabela='temp_data'):
        conn = sqlite3.connect('C:\\SQLite\\testemapa.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT LOCAL, DESCRICAO FROM {nome_tabela}")
        registros = cursor.fetchall()

        conn.close()

        return registros