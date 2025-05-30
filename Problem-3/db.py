import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "zeta_db"),
        user=os.getenv("DB_USER", "zeta"),
        password=os.getenv("DB_PASSWORD", "secret"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
    )
