import pandas as pd
import sqlite3

# ------------------------/ Funções relaciodas ao banco de dados

class funcoesSql:
    def criarBancodeDados(self):
        # cria o banco de dados e a tabela se não existirem
        conn = sqlite3.connect('C:\\SQLite\\testemapa.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS estabelecimento (
            NOME_ESTABELECIMENTO TEXT PRIMARY KEY,
            LATITUDE REAL,
            LONGITUDE REAL
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS cliente (
            CPF TEXT,
            NOME TEXT
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS promocao (
            NOME_PRODUTO TEXT,
            DESCRICAO TEXT,
            VALOR_PROMOCAO TEXT,
            DATA_FINAL DATE,
            ESTABELECIMENTO TEXT,
            FOREIGN KEY (ESTABELECIMENTO) REFERENCES estabelecimento(NOME_ESTABELECIMENTO)
        )''')

        conn.commit()
        conn.close()

    def inserirDadosNoSQLite(self, nome_estabelecimento, latitude, longitude, nome_tabela='estabelecimento'):
        # insere novas "lojas" no banco de dados
        conn = sqlite3.connect('C:\\SQLite\\testemapa.db')
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO {nome_tabela} VALUES (?, ?, ?)", (nome_estabelecimento, latitude, longitude))

        conn.commit()
        conn.close()

    def editarDadosNoSQLite(self, nome_estabelecimento, nova_descricao, nome_tabela='promocao'):
        # edita a descrição de uma promoção no banco de dados
        conn = sqlite3.connect('C:\\SQLite\\testemapa.db')
        cursor = conn.cursor()

        cursor.execute(f"UPDATE {nome_tabela} SET DESCRICAO = ? WHERE ESTABELECIMENTO = ?", (nova_descricao, nome_estabelecimento))

        conn.commit()
        conn.close()

    def excluirDadosNoSQLite(self, nome_estabelecimento, nome_tabela='estabelecimento'):
        # exclui um local do banco de dados
        conn = sqlite3.connect('C:\\SQLite\\testemapa.db')
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM {nome_tabela} WHERE NOME_ESTABELECIMENTO = ?", (nome_estabelecimento,))

        conn.commit()
        conn.close()

    def listarDadosNoSQLite(self, nome_tabela='estabelecimento'):
        conn = sqlite3.connect('C:\\SQLite\\testemapa.db')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {nome_tabela}")
        registros = cursor.fetchall()

        conn.close()

        return registros

    def excluirPromocaoNoSQLite(self, nome_estabelecimento, nome_tabela='promocao'):
        # exclui uma promoção do banco de dados
        conn = sqlite3.connect('C:\\SQLite\\testemapa.db')
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM {nome_tabela} WHERE ESTABELECIMENTO = ?", (nome_estabelecimento,))

        conn.commit()
        conn.close()

sql = funcoesSql()
sql.criarBancodeDados()