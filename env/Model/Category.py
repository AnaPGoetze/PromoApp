class Category:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
        '''
        self.db.cursor.execute(query)
        self.db.commit()

    def add_category(self, nome):
        query = "INSERT INTO categories (nome) VALUES (?)"
        self.db.cursor.execute(query, (nome,))
        self.db.commit()

    def get_category(self, category_id):
        query = "SELECT * FROM categories WHERE id = ?"
        self.db.cursor.execute(query, (category_id,))
        return self.db.cursor.fetchone()
