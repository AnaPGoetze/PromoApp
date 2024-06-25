class Client:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS clientes (
            cpf TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            endereco_id INTEGER NOT NULL,
            data_cadastro DATE NOT NULL,
            data_nascimento DATE NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            FOREIGN KEY (endereco_id) REFERENCES addresses(id)
        )
        '''
        self.db.cursor.execute(query)
        self.db.commit()

    def add_client(self, cpf, nome, endereco_id, data_cadastro, data_nascimento, email, senha):
        query = '''
        INSERT INTO clientes (cpf, nome, endereco_id, data_cadastro, data_nascimento, email, senha)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.db.cursor.execute(query, (cpf, nome, endereco_id, data_cadastro, data_nascimento, email, senha))
        self.db.commit()

    def get_client(self, cpf):
        query = "SELECT * FROM clientes WHERE cpf = ?"
        self.db.cursor.execute(query, (cpf,))
        return self.db.cursor.fetchone()
