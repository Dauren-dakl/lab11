import psycopg2
from config import load_config

def create_table():
    config = load_config()
    command = """CREATE TABLE phone_book (
                    Phone_Number varchar(255),
                    Name varchar(255),
                    Second_Name varchar(255)
                );"""
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    
if __name__ == "__main__":
    create_table()