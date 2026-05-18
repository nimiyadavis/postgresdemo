import psycopg2
from psycopg2 import sql, OperationalError
import psycopg2.extras
import os
from dotenv import load_dotenv
load_dotenv()

conn = None
#Function to connect to the database
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host = os.getenv('HOST'),
            user = os.getenv('USER'),
            password = os.getenv('PASSWORD'),       
            database = os.getenv('DATABASE'),
            port = os.getenv('PORT')
        )
        print("Connection to the database was successful!")
        return conn
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        return None 
    
# conn = get_db_connection()