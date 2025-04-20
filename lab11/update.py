import psycopg2
from config import load_config

def update_data(phone_number, name):
    sql = """UPDATE phone_book 
                SET Phone_Number = %s
                WHERE Name = %s"""

    config = load_config()

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, (phone_number, name))
                connection.commit()
                print("Данные успешно обновлены.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при вставке:", error)

if __name__ == '__main__':
    update_data("87477522525", "Kanagat")
