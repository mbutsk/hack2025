import sqlite3
import os

# То, что стирается мимолетно, хранилось в State, данные, которые сопроваждают пользователя на протяжении всей игры, хранятся в SQL датабазе
class Database():
    def __init__(self, name='db.db'):
        os.makedirs("db", exist_ok=True)
        self.connection = sqlite3.connect("db/" + name)
        self.cursor = self.connection.cursor()

    def select(self, columns: list, table, where: str | None = None):
        columns = ", ".join(columns)
        if where:
            query = f"SELECT {columns} FROM {table} WHERE {where}"
        else:
            query = f"SELECT {columns} FROM {table}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        return rows
    
    def create(self, table, **columns):
        columns_def = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table} ({columns_def})"
        self.cursor.execute(query)
        self.connection.commit()
    
    def insert(self, table, **kwargs):
        columns = ", ".join(kwargs.keys())
        placeholders = ", ".join(["?" for _ in kwargs.values()])
        values = tuple(kwargs.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()
    
    def delete(self, table, where: str):
        self.cursor.execute(f"DELETE FROM {table} WHERE {where}")
        self.connection.commit()

    def close(self):
        self.connection.close()