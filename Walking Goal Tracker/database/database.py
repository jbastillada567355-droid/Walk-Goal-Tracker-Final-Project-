import sqlite3

class Database:
    def __init__(self, db_name="tracker_database.db"):
        self.db_name = db_name


    def connect(self):
        return sqlite3.connect(self.db_name)


    def initialize_database(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS goals (
                title TEXT NOT NULL PRIMARY KEY,
                days INTEGER NOT NULL,
                distance FLOAT NOT NULL
            )
        """)
        connection.commit()
        cursor.close()
        connection.close()


    def get_all_goals(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT title, days, distance FROM goals")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return [{"title": r[0], "days": r[1], "distance": r[2]} for r in rows]


    def save_goal(self, title, days, distance):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO goals (title, days, distance) VALUES (?, ?, ?)",
            (title, days, distance)
        )
        connection.commit()
        cursor.close()
        connection.close()


    def update_goal(self, old_title, title, days, distance):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE goals SET title=?, days=?, distance=? WHERE title=?",
            (title, days, distance, old_title)
        )
        connection.commit()
        cursor.close()
        connection.close()


    def delete_goal(self, title):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM goals WHERE title=?", (title,))
        connection.commit()
        cursor.close()
        connection.close()