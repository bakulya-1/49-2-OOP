
#Нужно реализовать функцию, которая будет возвращать нам пользователей из БД по их возрасту
# Нужно вывести все в Принт. Если пользователей несколько с одинаковым возрастном, то нужно будет вывести их все

import sqlite3

from classwork.classw6 import cursor

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    fio VARCHAR (100) NOT NULL,
    age INTEGER NOT NULL
    )    
""")

connect.commit()

def add_user(fio, age):
    cursor.execute('INSERT INTO users (fio, age) VALUES (?, ?)', (fio, age))
    connect.commit()
    print(f"Пользователь {fio} добавлен")

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print(f"Список всех пользователей:")
        for user in users:
            print(f'FIO: {user[0]}, AGE: {user[1]}')
    else:
        print(f"Список пользователей пуст.")

def get_users_by_age(age):
    cursor.execute('SELECT * FROM users WHERE age = ?', (age,))
    users = cursor.fetchall()

    if users:
        print(f"Пользователи с возрастом {age}:")
        for user in users:
            print(f"FIO: {user[0]}, AGE: {user[1]}")
    else:
        print(f"Нет пользователей с возрастом {age}")

add_user('Charli', 31)
add_user('Ce Lyan', 19)
add_user('Hua Chen', 21)
add_user('Shelli', 21)
add_user('Li Ven', 19)

get_all_users()

age_to_find = 21
get_users_by_age(age_to_find)

connect.close()





