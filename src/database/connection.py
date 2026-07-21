import mysql.connector
from mysql.connector import Error

from src.utils.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)


def get_connection():
    """
    Create and return a connection to the Guardian AI database.
    Returns None if the connection fails.
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )

        

        return connection

    except Error as e:
        print(f"Database connection failed: {e}")
        return None
