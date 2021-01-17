import sqlite3


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect('reserves.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS reserves(table_id integer, date text, telephone text, name text, email text, comments text);")
        self.conn.commit()

    def insert(self, name: str, telephone: str, date: str, email: str, table: int, comments: str):
        self.cursor.execute("INSERT INTO reserves VALUES(?,?,?,?,?,?)", (table, date, telephone, name, email, comments))
        self.conn.commit()

    def tableReserved(self, date: str, table: int):
        self.cursor.execute('SELECT * FROM reserves where table_id = ? and date = ?', (table, date))
        if self.cursor.fetchall():
            return True
        return False
