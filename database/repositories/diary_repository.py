from database.database import DatabaseManager
from datetime import datetime


class DiaryRepository:
    """
    Handles all Diary database operations.
    """

    def __init__(self):

        self.db = DatabaseManager()

        self.connection = self.db.connect()

        self.cursor = self.db.cursor

    # -------------------------
    # Add Entry
    # -------------------------

    def add_entry(
        self,
        title,
        content,
        mood,
        created_at,
        updated_at,
        tags="",
        image_path="",
        voice_path="",
        favorite=0
    ):

        self.cursor.execute(
            """
            INSERT INTO diary
            (
                title,
                content,
                mood,
                created_at,
                updated_at,
                tags,
                image_path,
                voice_path,
                favorite
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                title,
                content,
                mood,
                created_at,
                updated_at,
                tags,
                image_path,
                voice_path,
                favorite
            )
        )

        self.db.commit()

        print("✅ Diary Entry Saved")

    def get_all_entries(self):

        self.cursor.execute(
            """
            SELECT *
            FROM diary
            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()
    
    def search_entries(self, keyword):

        self.cursor.execute(
            """
            SELECT *
            FROM diary
            WHERE title LIKE ?
            OR content LIKE ?
            ORDER BY id DESC
            """,
            (
                f"%{keyword}%",
                f"%{keyword}%"
            )
        )

        return self.cursor.fetchall()
    
    def get_entry_by_id(self, entry_id):

        self.cursor.execute(
            "SELECT * FROM diary WHERE id = ?",
            (entry_id,)
        )

        return self.cursor.fetchone()
    
    def get_favorite_entries(self):

        self.cursor.execute(
            """
            SELECT *
            FROM diary
            WHERE favorite = 1
            ORDER BY updated_at DESC
            """
        )

        return self.cursor.fetchall()
    
    def update_entry(
        self,
        entry_id,
        title,
        content,
        mood,
        updated_at
    ):

        self.cursor.execute(
            """
            UPDATE diary
            SET
                title = ?,
                content = ?,
                mood = ?,
                updated_at = ?
            WHERE id = ?
            """,
            (
                title,
                content,
                mood,
                updated_at,
                entry_id
            )
        )

        self.db.commit()

        print("✅ Diary Entry Updated")

    # -------------------------
    # Toggle Favorite
    # -------------------------

    def toggle_favorite(self, entry_id, favorite):

        self.cursor.execute(
            """
            UPDATE diary
            SET favorite = ?
            WHERE id = ?
            """,
            (
                favorite,
                entry_id
            )
        )

        self.db.commit()

        print("⭐ Favorite Updated")
        
    def delete_entry(self, entry_id):

        self.cursor.execute(
            "DELETE FROM diary WHERE id = ?",
            (entry_id,)
        )

        self.db.commit()

        print("🗑 Diary Entry Deleted")

    # -------------------------
    # Close Database
    # -------------------------

    def close(self):

        self.db.close()

if __name__ == "__main__":

    diary = DiaryRepository()

    now = datetime.now().strftime("%d-%m-%Y %H:%M")

    diary.add_entry(

        title="First Entry",

        content="Today I completed Day 4 backend of LifeBook AI.",

        mood="😊 Happy",

        created_at=now,

        updated_at=now,

        tags="backend,day4"

    )

    entries = diary.get_all_entries()

    print("\n📖 Diary Entries\n")

    for entry in entries:

        print(entry)

    diary.close()

    