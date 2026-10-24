import os

import psycopg
from dotenv import load_dotenv

load_dotenv(override=True)

def test_database_connection_and_query():
    "Проверяю подключение к Postgres и выполнение запроса."

    with psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        connect_timeout=5,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT NOW()")
            result = cursor.fetchone()

    assert result is not None
    assert result[0] is not None
