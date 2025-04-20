import psycopg2
from config import load_config


def query(condition,value):
    sql = f'SELECT * FROM phone_book WHERE {condition} = %s'

    config = load_config()
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, (value,))
                rows = cursor.fetchall()
                for row in rows:    
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при запросе:", error)


if __name__ == '__main__':
    query("Phone_Number", "87018654555")
