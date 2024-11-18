import sqlite3


class Database:
    def __init__(self, db):
        # Connect to the database
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        # Create table if it does not exist
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS parts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                part TEXT NOT NULL,
                customer TEXT NOT NULL,
                retailer TEXT NOT NULL,
                price TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def fetch(self):
        """Fetch all rows from the parts table."""
        self.cur.execute("SELECT * FROM parts ORDER BY id ASC")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        """Insert a new part into the database."""
        try:
            self.cur.execute(
                "INSERT INTO parts (part, customer, retailer, price) VALUES (?, ?, ?, ?)",
                (part, customer, retailer, price)
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database Insert Error: {e}")

    def remove(self, id):
        """Remove a part by ID."""
        try:
            self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database Remove Error: {e}")

    def update(self, id, part, customer, retailer, price):
        """Update an existing part by ID."""
        try:
            self.cur.execute("""
                UPDATE parts
                SET part = ?, customer = ?, retailer = ?, price = ?
                WHERE id = ?
            """, (part, customer, retailer, price, id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database Update Error: {e}")

    def __del__(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()


# db = Database('store.db')
# db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
# db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
# db.insert("500w PSU", "Karen Johnson", "Newegg", "80")
# db.insert("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
# db.insert("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
# db.insert("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
# db.insert("600w Corsair PSU", "Karen Johnson", "Newegg", "130")
