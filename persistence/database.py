
import os
import psycopg2
from psycopg2 import sql

DATABASE_URL = os.getenv('DATABASE_URL')

def get_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def create_jobs_table():
    conn = get_connection()
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS jobs (
        id SERIAL PRIMARY KEY,
        job_type VARCHAR(255) NOT NULL,
        priority VARCHAR(50) NOT NULL,
        expiry_date TIMESTAMP NOT NULL,
        state VARCHAR(50) NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_jobs_table()
