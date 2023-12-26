import sqlite3

class Income:
    def __init__(self, amount=0.0, timeframe='', state='', source=''):
        self.amount = amount
        self.timeframe = timeframe
        self.state = state
        self.source = source

    # ... [other methods] ...

    def save_to_db(self, db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS income (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                timeframe TEXT,
                state TEXT,
                source TEXT
            )
        ''')

        # Insert data
        cursor.execute('''
            INSERT INTO income (amount, timeframe, state, source) 
            VALUES (?, ?, ?, ?)
        ''', (self.amount, self.timeframe, self.state, self.source))

        conn.commit()
        conn.close()

# Example usage (outside the Income class)
my_income = Income(5000, 'Monthly', 'CA', 'Software Engineer')
my_income.save_to_db('my_finances.db')
