from database.database import DatabaseManager


class DatabaseModels:
    """
    Creates all database tables.
    """

    def __init__(self):

        self.db = DatabaseManager()

        self.connection = self.db.connect()

        self.cursor = self.db.cursor

    def create_diary_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS diary (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            content TEXT NOT NULL,

            mood TEXT,

            created_at TEXT,

            updated_at TEXT,

            tags TEXT,

            image_path TEXT,

            voice_path TEXT,

            favorite INTEGER DEFAULT 0

        )
        """)

        self.db.commit()

        print("✅ Diary Table Created")

    def create_all_tables(self):

        self.create_diary_table()

    def close(self):

        self.db.close()


# ==========================
# Testing
# ==========================

if __name__ == "__main__":

    models = DatabaseModels()

    models.create_all_tables()

    models.close()