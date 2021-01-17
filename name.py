import sqlite3

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE saper
                  (id integer, time integer)
               """)
# Вставляем данные в таблицу
cursor.execute("""INSERT INTO saper
                  VALUES (1, 30
                  )"""
               )

# Сохраняем изменения
conn.commit()
