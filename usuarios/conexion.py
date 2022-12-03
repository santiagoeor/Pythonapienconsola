import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456789",
        database="db_apliconsola",
        port=3306
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]