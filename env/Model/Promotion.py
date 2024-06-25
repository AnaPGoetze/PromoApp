class Promotion:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS promocoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            valor_promocao REAL NOT NULL,
            vigencia_inicial DATE NOT NULL,
            vigencia_final DATE NOT NULL,
            cancelado BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY (produto_id) REFERENCES produto(id)
        )
        '''
        self.db.cursor.execute(query)
        self.db.commit()

    def add_promotion(self, produto_id, valor_promocao, vigencia_inicial, vigencia_final, cancelado=False):
        query = '''
        INSERT INTO promocoes (produto_id, valor_promocao, vigencia_inicial, vigencia_final, cancelado)
        VALUES (?, ?, ?, ?, ?)
        '''
        self.db.cursor.execute(query, (produto_id, valor_promocao, vigencia_inicial, vigencia_final, cancelado))
        self.db.commit()

    def get_promotion(self, promotion_id):
        query = "SELECT * FROM promocoes WHERE id = ?"
        self.db.cursor.execute(query, (promotion_id,))
        return self.db.cursor.fetchone()
