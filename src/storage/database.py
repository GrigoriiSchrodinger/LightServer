import os
import sqlite3
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def push(self, query, param):
        pass

    @abstractmethod
    def get(self, query):
        pass


class SqlManager(Database):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._database_file = "src/storage/database.db"
        os.makedirs(os.path.dirname(self._database_file), exist_ok=True)

        self._connection = sqlite3.connect(self._database_file)
        self._create_table_lamps()

    def _create_table_lamps(self):
        with open(f'src/storage/sql_query/create_table.sql', 'r') as sqlite_file:
            file = sqlite_file.read()
            self._connection.executescript(file)

    def push(self, query: str, param: tuple):
        cursor = self._connection.cursor()
        cursor.execute(query, param)
        self._connection.commit()

    def get(self, query: str):
        cursor = self._connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def __del__(self):
        self._connection.close()


class LampsManager(SqlManager):
    _QUERY_ADD_LAMP: str = "INSERT INTO lamps (ip, name, status) VALUES (?, ?, ?)"
    _QUERY_UPDATE_LAMP_STATUS: str = "UPDATE lamps SET status=? WHERE ip=?"
    _QUERY_GET_ALL_LAMPS: str = "SELECT ip, name, status FROM lamps;"

    def add_lamp(self, ip: str, name: str, status: str):
        self.push(self._QUERY_ADD_LAMP, (ip, name, status,))

    def update_lamp_status(self, ip: str, status: str):
        self.push(self._QUERY_UPDATE_LAMP_STATUS, (status, ip,))

    def get_lamps(self):
        return self.get(self._QUERY_GET_ALL_LAMPS)


