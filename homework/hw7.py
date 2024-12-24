
#добавить функции которые в запросе будут использовать INNER JOIN FULL OUTER JOIN

import sqlite3

from classwork.classw6 import connect, cursor

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

def create_db():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                userid INTEGER PRIMAY KET AUTOINCREMENT,
                fio VARCHAR(100) NOT NULL,
                age INTEGER NOT NULL,
                hobby TEXT
            )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades(
                gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
                userid INTEGER,
                subject VARCHAR(100) NOT NULL,
                grade INTEGER NOT NULL,
                FOREIGN KEY(userid) REFERENCES users(userid)
                )
    ''')
    connect.commit()

#create_db()

def add_user(fio, age, hobby):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio, age, hobby))
    connect.commit()
    print(f"Пользователь {fio}, добавлен")

add_user('Charli', 22, 'Баскетбол')
add_user('Kazuma', 25, 'Гонщик')
add_user('Mao', 22, 'Рисовать')
add_user('Van Nam',25, 'Футбол')
add_user('Aliza', 20, 'Плавать')
add_user('Chjuge Lyan', 22, 'Гольф')


def delete_user_by_id(id):
    cursor.execute(
        'DELETE FROM users WHERE userid = ?',
        (id,)
    )
    connect.commit()

delete_user_by_id(1)

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

#    return print(users)

    if users:
        print(f"Список всех пользователь:")
        for user in users:
            print(f"FIO: {user[1]}, AGE: {user[2]}")
    else:
        print(f"Список пользователей пуст.")

get_all_users()

def get_user_by_age(age):
    cursor.execute('SELECT * FROM users WHERE age = ?', (age,))
    users = cursor.fetchall()
    print(f"Пользователи по возрасту: {age}")
    for user in users:
        print(f'FIO: {user[1]}, AGE {user[2]}')

get_user_by_age(25)

def update_user_age_by_id(id, fio):
    cursor.execute(
        'UPDATE users SET fio = ? WHERE userid = ?',
        (fio, id)
    )
    connect.commit()

update_user_age_by_id(3, 'Djahen')
get_all_users()


def add_grade(user_id, subject, grade):
    cursor.execute(
        "INTEGER INTO grades (userid, subject, grade VALUES (?, ?, ?)",
        (user_id, subject, grade)
    )

    connect.commit()

add_grade(2, "История", 4)
add_grade(4, "История", 5)
add_grade(6, "История", 5)


def get_users_with_grades():
    cursor.execute("""
    SElECT users.fio, grades.subject, grades.grade
    FROM users INNER JOIN grades On users.userid = grades.userid
    """)
    rows = cursor.fetchall()

    print(f"Пользователи с оценками:")
    for row in rows:
        print(f"FIO: {row[0]}, SUBJECT: {row[2]}, GRADE: {row[3]}")

def get_users_with_grades_full_outer():
    cursor.execute("""
    SELECT users.fio, grades. subject, grades.grade
    FROM grades LEFT JOIN users ON users.userid = grades.userid
    """)

    left_join = cursor.fetchall()
    cursor.execute("""
        SELECT users.fio, grades. subject, grades.grade
        FROM grades LEFT JOIN users ON users.userid = grades.userid
        """)

    right_join = cursor.fetchall()

    full_outer = left_join + right_join

    print(f"Пользователи с оценками(FULL OUTER JOIN):")

    for row in full_outer:
        print(f"FIO: {row[0]}, SUBJECT: {row[2]}, GRADE: {row[3]}")

get_all_users()
get_users_with_grades()


connect.close()













