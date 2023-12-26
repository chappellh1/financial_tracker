import sqlite3

class Income:
    def __init__(self, amount=0.0, timeframe='', state='', source=''):
        self.amount = amount
        self.timeframe = timeframe
        self.state = state
        self.source = source

    # ... [other methods] ...

    def save_to_db(self, db_path):
        try:
            print("Connecting to database at:", db_path)
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            print("Connected to database.")

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS income (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL,
                    timeframe TEXT,
                    state TEXT,
                    source TEXT
                )
            ''')
            print("Table created or already exists.")

            cursor.execute('''
                INSERT INTO income (amount, timeframe, state, source) 
                VALUES (?, ?, ?, ?)
            ''', (self.amount, self.timeframe, self.state, self.source))
            print("Data inserted:", self.amount, self.timeframe, self.state, self.source)

            conn.commit()
            print("Changes committed to database.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
            print("Connection closed.")
