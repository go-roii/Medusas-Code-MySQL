import mysql.connector
from Modules.Config import mysqlConfig


class Connection:
    def __init__(self):
        self.mysqlConnection = mysql.connector.connect(**mysqlConfig)

    def closeConnection(self):
        self.mysqlConnection.close()

    def commit(self):
        self.mysqlConnection.commit()
