import psycopg2
from config import load_config
from csv import DictReader
def insert_data(phone_number, name, second_name):
    check_sql = """SELECT 1 FROM phone_book WHERE 
                   phone_number = %s AND name = %s AND second_name = %s;"""
    insert_sql = """INSERT INTO phone_book(phone_number, name, second_name)
                    VALUES (%s, %s, %s);"""

    config = load_config()

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                # Проверка: есть ли такая запись
                cursor.execute(check_sql, (phone_number, name, second_name))
                if cursor.fetchone():
                    print(f"Запись уже существует: {name} {second_name} - {phone_number}")
                else:
                    cursor.execute(insert_sql, (phone_number, name, second_name))
                    connection.commit()
                    print(f"Добавлено: {name} {second_name} - {phone_number}")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при вставке:", error)

if __name__ == '__main__':
    if input("console/csv: ") == "csv".lower():
        with open("lab-sql/contacts.csv", mode="r", newline="") as data:
            contacts = DictReader(data)
        
            for contact in contacts:
                insert_data(contact["phone_number"], contact["name"], contact["second_name"])
    else:
        name = input("Name: ")
        second = input("Second Name: ")
        phone = input("Phone Numebr: ")
        insert_data(phone, name, second)
