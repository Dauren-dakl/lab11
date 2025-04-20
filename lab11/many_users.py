""" 
Create procedure to insert many new users by list of name and phone.
Use loop and if statement in stored procedure. 
Check correctness of phone in procedure and return all incorrect data. """

import psycopg2
from config import load_config
from csv import DictReader
def insert_many_data(lst):
    

        
        config = load_config()

        try:
            with psycopg2.connect(**config) as connection:
                with connection.cursor() as cursor:
                    for user in lst:
                        name = user["Name"]
                        phone_number = user["Phone_Number"]
                        second_name = user["Second_Name"]

                        check_sql = f"""SELECT 1 FROM phone_book 
                                   WHERE phone_number = %s AND name = %s AND second_name = %s;"""
                    
                        # Проверка: есть ли такая запись
                        cursor.execute(check_sql, (phone_number, name, second_name))
                        if cursor.fetchone():
                            print(f"Запись уже существует: {name} {second_name} - {phone_number}")
                        else:
                            if not phone_number.startswith("8") or not phone_number[1:].isdigit():
                                print(f"Неверный номер: {phone_number} пользователя {name}")
                                continue
                            insert_sql = """INSERT INTO phone_book(phone_number, name, second_name)
                                    VALUES (%s, %s, %s);"""
                            cursor.execute(insert_sql, (phone_number, name, second_name))
                            connection.commit()
                            print(f"Добавлено: {name} {second_name} - {phone_number}")
        except (psycopg2.DatabaseError, Exception) as error:
            print("Ошибка при вставке:", error)

if __name__ == '__main__':
    many_users = [
    {"Name": "Krasavchik", "Phone_Number": "977011111111", "Second_Name": "Johnson"},
    {"Name": "Bob", "Phone_Number": "877022222222", "Second_Name": "Smith"},
    {"Name": "Charlie", "Phone_Number": "877033333333", "Second_Name": "Brown"},
    {"Name": "Diana", "Phone_Number": "877044444444", "Second_Name": "Williams"},
]

    insert_many_data(many_users)

