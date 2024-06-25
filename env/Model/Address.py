class Address:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS addresses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cep TEXT NOT NULL,
            logradouro TEXT NOT NULL,
            numero INTEGER NOT NULL,
            complemento TEXT,
            bairro TEXT NOT NULL,
            latitude REAL,
            longitude REAL
        )
        '''
        self.db.cursor.execute(query)
        self.db.commit()

    def add_address(self, cep, logradouro, numero, complemento, bairro, latitude, longitude):
        query = '''
        INSERT INTO addresses (cep, logradouro, numero, complemento, bairro, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.db.cursor.execute(query, (cep, logradouro, numero, complemento, bairro, latitude, longitude))
        self.db.commit()

    def get_address(self, address_id):
        query = "SELECT * FROM addresses WHERE id = ?"
        self.db.cursor.execute(query, (address_id,))
        return self.db.cursor.fetchone()
