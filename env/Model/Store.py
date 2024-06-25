class Store:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS stores (
            cnpj TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            fantasia TEXT,
            endereco_id INTEGER,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            FOREIGN KEY (endereco_id) REFERENCES addresses(id)
        )
        '''
        self.db.cursor.execute(query)
        self.db.commit()

    def add_store(self, cnpj, nome, fantasia, endereco_id, email, senha):
        query = '''
        INSERT INTO stores (cnpj, nome, fantasia, endereco_id, email, senha)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.db.cursor.execute(query, (cnpj, nome, fantasia, endereco_id, email, senha))
        self.db.commit()

    def get_store(self, cnpj):
        query = "SELECT * FROM stores WHERE cnpj = ?"
        self.db.cursor.execute(query, (cnpj,))
        return self.db.cursor.fetchone()
