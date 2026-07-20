import sqlite3
import numpy as np

def get_connection():
    conn = sqlite3.connect("knowledge.db")
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            embedding BLOB NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_chunk(text, embedding):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chunks (text, embedding) VALUES (?, ?)",
        (text, embedding.tobytes())
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("Table created.")

    test_embedding = np.array([0.1, 0.2, 0.3], dtype=np.float32)
    save_chunk("This is a test chunk", test_embedding)
    print("Test chunk saved.")