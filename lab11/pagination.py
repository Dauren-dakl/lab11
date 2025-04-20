import psycopg2
from config import load_config
import keyboard
import os

def query_pagination():
    config = load_config()
    limit = 2
    pointer = 0

    try:
        while True:
            key = keyboard.read_event(suppress=True)
            if key.event_type == keyboard.KEY_DOWN:
                if key.name == "right":
                    pointer += limit
                elif key.name == "left":
                    pointer -= limit
                    if pointer < 0:
                        pointer = 0
                elif key.name == "esc":
                    print("Выход...")
                    break

                os.system('cls' if os.name == 'nt' else 'clear')

                with psycopg2.connect(**config) as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(
                            "SELECT * FROM phone_book ORDER BY Phone_Number LIMIT %s OFFSET %s",
                            (limit, pointer)
                        )
                        rows = cursor.fetchall()
                        if rows:
                            print(f"Показаны записи с {pointer + 1} по {pointer + len(rows)}:\n")
                            for row in rows:
                                print(row)
                        else:
                            print("Больше записей нет.")
                            pointer -= limit  # вернуться назад
    except Exception as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    query_pagination()
