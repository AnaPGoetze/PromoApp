class Product:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            valor_tabela REAL NOT NULL,
            descricao TEXT,
            loja_id TEXT NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (loja_id) REFERENCES stores(cnpj),
            FOREIGN KEY (categoria_id) REFERENCES categories(id)
        )
        '''
        self.db.cursor.execute(query)
        self.db.commit()

    def add_product(self, nome, valor_tabela, descricao, loja_id, categoria_id):
        query = '''
        INSERT INTO produto (nome, valor_tabela, descricao, loja_id, categoria_id)
        VALUES (?, ?, ?, ?, ?)
        '''
        self.db.cursor.execute(query, (nome, valor_tabela, descricao, loja_id, categoria_id))
        self.db.commit()

    def get_product(self, product_id):
        query = "SELECT * FROM produto WHERE id = ?"
        self.db.cursor.execute(query, (product_id,))
        return self.db.cursor.fetchone()
