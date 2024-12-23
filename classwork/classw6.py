#Базы данных. Git


import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    fio VARCHAR (100) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
""")

connect.commit()


# CRUD - Create Reade Update Delete

def add_user(fio, age, hobby=""):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio, age, hobby))
    connect.commit()
    print(f"Пользователь {fio}, Добавлен")

# add_user('Илья Муровец', 26, 'Бегать')
# add_user('John Doe', 27, 'Спать')


def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print(f"Список всех пользователей:")
        for user in users:
            print(f'FIO: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}')
    else:
        print(f'Список пользователей пуст')


get_all_users()

connect.close()