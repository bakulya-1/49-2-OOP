
#1) Нужно создать функцию create_grate_statistics_view в которой будет создаваться ваше
# представление(view) statistic_view в БД
#2)Ваше представление statistic_view(view) должно возвращать статистику по предметам
# среднюю оценку, максимальную оценку и минимальную оценку.
#3) Создать функцию get_statistic которая будет вызывать ваше представление.

import sqlite3


connect = sqlite3.connect('users.db')
cursor = connect.cursor()

#Создание таблиц
def create_db():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                userid INTEGER PRIMARY KEY AUTOINCREMENT,
                fio VARCHAR(100) NOT NULL,
                age INTEGER NOT NULL,
                hobby TEXT
            )
        ''')

#
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades(
                gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
                userid INTEGER,
                subject VARCHAR(100) NOT NULL,
                grade INTEGER NOT NULL,
                FOREIGN KEY (userid) REFERENCES users(userid)
            )
        ''')
    connect.commit()

create_db()

def add_user(fio, age, hobby =""):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio,age,hobby))
    connect.commit()
    print(f"Пользователь {fio} добавлен.")

"""""
def delete_user_by_id(user_id):
    cursor.execute('DELETE FROM users WHERE userid = ?', (user_id,))
    connect.commit()
    print(f"Пользователь с ID {user_id} удалён")

delete_user_by_id(3)
"""""

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print(f"Список всех пользователей:")
        for user in users:
            print(f"ID: {user[0]}, Fio: {user[1]}, Age: {user[2]}, Hobby: {user[3]}")
    else:
        print(f"Список пользователей пуст")

#get_all_users()

def get_user_by_age(age):
    cursor.execute('SELECT * FROM users WHERE age = ?', (age,))
    users = cursor.fetchall()
    print(f"Пользователи с возрастом {age}:")
    for user in users:
        print(f"ID: {user[0]}, Fio: {user[1]}, Age: {user[2]}, Hobby: {user[3]}")

get_user_by_age(24)

def update_user_age_by_id(user_id, fio):
    cursor.execute('UPDATE users SET fio = ? WHERE userid = ?', (fio, user_id))
    connect.commit()
    print(f"ФИО пользователя с ID {user_id} обновлено.")

# update_user_age_by_id(4, "Miko")
# get_all_users()

def add_grade(user_id, subject, grade):
    cursor.execute('INSERT INTO grades (userid, subject, grade) VALUES (?, ?, ?)', (user_id, subject, grade))
    connect.commit()
    print(f" Оценка добавлена для пользователя с ID {user_id}")

def get_users_with_grades():
    cursor.execute('''
    SELECT users.fio, users.age, grades.subject, grades.grade
    FROM users
    INNER JOIN grades ON users.userid = grades.userid
    ''')
    rows = cursor.fetchall()
    print(f"Пользователи с оценками:")
    for row in rows:
        print(f"Fio: {row[0]}, Age: {row[1]}, Subject: {row[2]}, Grade: {row[3]}")

def get_users_with_left_join():
    cursor.execute('''
    SELECT users.fio, users.age, grades.subject, grades.grade
    FROM users
    LEFT JOIN grades ON users.userid = grades.userid
    ''')
    rows = cursor.fetchall()
    print(f"Пользователи с оценками (LEFT JOIN):")
    for row in rows:
        print(f"Fio: {row[0]}, Age: {row[1]}, Subject: {row[2]}, Grade: {row[3]}")

def get_average_age():
    cursor.execute('SELECT AVG(age) FROM users')
    avg_age = cursor.fetchone()[0]
    print(f"Средний возраст пользователей: {avg_age}")

def get_grade_statistics():
    cursor.execute('''
    SELECT subject, AVG(grade) as AVG_grade, MAX(garde) as max_grade, MIN(grade) as min_grade
    FROM grades
    GROUP BY subject
    ''')
    stats = cursor.fetchall()
    print(f"Статистика по оценкам:")
    for stat in stats:
        print(f"Предмет: {stat[0]}, Средняя оценка: {stat[1]}, Максимальная оценка: {stat[2]}, Минимальная оценка: {stat[3]}")

# get_average_age()
# get_grade_statistics()

def create_statistic_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS statistic_view AS
        SELECT
            subject,
            AVG(grade) AS average_grade,
            MAX(grade) AS max_grade,
            MIN(grade) AS min_grade
        FROM grades
        GROUP BY subject;
    ''')
    connect.commit()
    print(f"Представление statistic_view успешно создано.")

def get_statistic():
    cursor.execute('SELECT * FROM statistic_view')
    stats = cursor.fetchall()
    print(f"Статистика по предметам:")
    for stat in stats:
        print(f"Предмет: {stat[0]}, Средняя оценка: {stat[1]}, Максимальная оценка: {stat[2]}, Минимальная оценка: {stat[3]}")

create_db()
add_user('Hioshi', 24, 'фехтование')
add_user('Naoko', 23, 'сёрф')
add_user('Yuri', 23, 'рисование')
add_user('Hana', 24, 'плавание')
add_user('Toshi', 25, 'баскетбол')
add_user('Kazuma', 24, 'чтение')

add_grade(4, 'Химия', 5)
add_grade(6, 'Физика', 4)
add_grade(1, 'Алгебра', 5)
add_grade(5, 'Химия', 5)

create_statistic_view()
get_statistic()