import sqlite3
import pandas as pd
from konfigurasi import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id

def fetch_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_dataframe(query, params=None):
    conn = get_connection()
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df
