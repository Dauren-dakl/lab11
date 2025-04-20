import psycopg2
from config import load_config

def delete_data(name):
    sql = """DELETE FROM phone_book 
                WHERE Name = %s """

    config = load_config()

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, (name,))
                connection.commit()
                print("Данные успешно удалены.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при вставке:", error)

if __name__ == '__main__':
    delete_data("Egor")
