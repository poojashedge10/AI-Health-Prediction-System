import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="health_prediction_db"
    )

    return connection