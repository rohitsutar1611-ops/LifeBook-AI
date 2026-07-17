from database.database import DatabaseManager


class MoodRepository:

    def __init__(self):

        self.db = DatabaseManager()

        self.connection = self.db.connect()

        self.cursor = self.db.cursor

    # -------------------------
    # Save Mood
    # -------------------------

    def add_mood(self, mood, note, created_at):

        self.cursor.execute(
            """
            INSERT INTO moods
            (
                mood,
                note,
                created_at
            )
            VALUES (?, ?, ?)
            """,
            (
                mood,
                note,
                created_at
            )
        )

        self.db.commit()

        print("✅ Mood Saved")

    # -------------------------
    # Get All Moods
    # -------------------------

    def get_all_moods(self):

        self.cursor.execute(
            """
            SELECT *
            FROM moods
            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()
    
    def get_latest_mood(self):

        self.cursor.execute("""
            SELECT *
            FROM moods
            ORDER BY id DESC
            LIMIT 1
        """)

        return self.cursor.fetchone()

    # -------------------------
    # Close
    # -------------------------

    def close(self):

        self.db.close()