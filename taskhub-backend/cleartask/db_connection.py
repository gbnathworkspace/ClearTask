
# db_connection.py

import os
import django
import psycopg2

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskhubmain.settings')
django.setup()

from django.conf import settings

# Fetch database connection parameters from Django settings
DB_NAME = settings.DATABASES['default']['NAME']
DB_USER = settings.DATABASES['default']['USER']
DB_PASSWORD = settings.DATABASES['default']['PASSWORD']
DB_HOST = settings.DATABASES['default']['HOST']
DB_PORT = settings.DATABASES['default']['PORT']

def get_db_connection():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        print("Database connection initialized successfully.")
        return conn
    except Exception as e:
        print(f"Error initializing database: {e}")
        return None

# Initialize the connection at the start of the project
db_connection = get_db_connection()