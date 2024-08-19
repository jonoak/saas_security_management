import sqlite3
import logging

class DataStorage:
    def __init__(self):
        self.connection = sqlite3.connect('saas_security.db')
        self.create_tables()

    def create_tables(self):
        query = '''CREATE TABLE IF NOT EXISTS security_data (
                        platform TEXT,
                        data TEXT
                    )'''
        try:
            self.connection.execute(query)
            self.connection.commit()
        except Exception as e:
            logging.error(f'Failed to create tables: {e}')

    def store_data(self, data):
        for platform, details in data.items():
            query = 'INSERT INTO security_data (platform, data) VALUES (?, ?)'
            self.connection.execute(query, (platform, str(details)))
        self.connection.commit()
