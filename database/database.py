import sqlite3
from pathlib import Path


class DatabaseManager:
    """
    Handles SQLite database connection.
    """

    def __init__(self):

        self.project_root = Path(__file__).resolve().parent
        self.db_path = self.project_root / "lifebook.db"

        self.connection = None
        self.cursor = None

    def connect(self):

        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

        print("✅ Database Connected")

        return self.connection

    def commit(self):

        if self.connection:
            self.connection.commit()

    def close(self):

        if self.connection:
            self.connection.close()
            print("🔒 Database Closed")


# ==========================
# Testing
# ==========================

if __name__ == "__main__":

    db = DatabaseManager()

    db.connect()

    db.close()