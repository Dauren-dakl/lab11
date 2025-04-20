import psycopg2
from config import load_config


def pattern(condition,value):
    sql = f"SELECT * FROM phone_book WHERE {condition} LIKE '%{value}%'"

    config = load_config()
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
                for row in rows:    
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при запросе:", error)


if __name__ == '__main__':
    pattern("Phone_Number", "80000000000")
