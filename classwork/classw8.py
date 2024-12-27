
#Агрегационные функции,группировка данных, вложенные запросы и представления (Views)


import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()


# Создание базы данных и таблиц с различными связями
# Один к одному, Один ко многим, Многие к одному, Многие ко многим
# Joins: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN

def create_db():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                userid INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор пользователя
                fio VARCHAR(100) NOT NULL,                -- ФИО пользователя
                age INTEGER NOT NULL,
                hobby TEXT
            )
        ''')

    # Создание таблицы 'grades'
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                gradeid INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор записи о оценке
                userid INTEGER,                            -- Внешний ключ, который ссылается на userid из таблицы 'users'
                subject VARCHAR(100) NOT NULL,             -- Название предмета
                grade INTEGER NOT NULL,                    -- Оценка
                FOREIGN KEY (userid) REFERENCES users(userid) -- Определяем связь с таблицей 'users'
            )
        ''')

    connect.commit()


create_db()


# CRUD - Create Read Update Delete

def add_user(fio, age, hobby=""):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio, age, hobby))
    connect.commit()
    print(f"Пользователь {fio} добавлен")


# add_user('Илья Муромец', 25, 'фехтование')
# add_user('John Doe1', 26, 'плавание')
# add_user('John Doe2', 27, 'шахматы')
# add_user('John Doe3', 28, 'чтение')
# add_user('John Doe4', 35, 'шахматы')
# add_user('John Doe5', 33, 'чтение')

def delete_user_by_id(user_id):
    cursor.execute('DELETE FROM users WHERE userid = ?', (user_id,))
    connect.commit()
    print(f"Пользователь с ID {user_id} удален")


# delete_user_by_id(3)

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print("Список всех пользователей:")
        for user in users:
            print(f"ID: {user[0]}, FIO: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}")
    else:
        print("Список пользователей пуст")


 #get_all_users()

def get_user_by_age(age):
    cursor.execute('SELECT * FROM users WHERE age = ?', (age,))
    users = cursor.fetchall()
    print(f"Пользователи с возрастом {age}:")
    for user in users:
        print(f"ID: {user[0]}, FIO: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}")


# get_user_by_age(25)

def update_user_age_by_id(user_id, fio):
    cursor.execute('UPDATE users SET fio = ? WHERE userid = ?', (fio, user_id))
    connect.commit()
    print(f"ФИО пользователя с ID {user_id} обновлено")


# update_user_age_by_id(4, "Арзыбек Абды")
# get_all_users()

def add_grade(user_id, subject, grade):
    cursor.execute('INSERT INTO grades (userid, subject, grade) VALUES (?, ?, ?)', (user_id, subject, grade))
    connect.commit()
    print(f"Оценка добавлена для пользователя с ID {user_id}")


# add_grade(7, "Алгебра", 3)
# add_grade(8, "Геометрия", 3)
# add_grade(9, "Физика", 3)

def get_users_with_grades():
    cursor.execute('''
    SELECT users.fio, users.age, grades.subject, grades.grade
    FROM users
    INNER JOIN grades ON users.userid = grades.userid
    ''')

    rows = cursor.fetchall()
    print("Пользователи с их оценками:")
    for row in rows:
        print(f"FIO: {row[0]}, AGE: {row[1]}, SUBJECT: {row[2]}, GRADE: {row[3]}")


def get_users_with_left_join():
    cursor.execute('''
    SELECT users.fio, users.age, grades.subject, grades.grade
    FROM users
    LEFT JOIN grades ON users.userid = grades.userid
    ''')

    rows = cursor.fetchall()
    print("Пользователи с их оценками (LEFT JOIN):")
    for row in rows:
        print(f"FIO: {row[0]}, AGE: {row[1]}, SUBJECT: {row[2]}, GRADE: {row[3]}")


# Агрегационные функции и группировка данных
def get_average_age():
    cursor.execute('SELECT SUM(age) FROM users')
    avg_age = cursor.fetchone()[0]
    print(f"Средний воозраст юзера {avg_age}")


def get_grade_statistics():
    cursor.execute('''
    SELECT subject, AVG(grade) as avg_grade, MAX(grade) as max_grade, MIN(grade) as min_grade
    FROM grades
    GROUP BY subject
    ''')

    stats = cursor.fetchall()
    print(f"Статистика по Оценкам: \n")
    print(stats)
    for stat in stats:
        print(f"SUBJECT: {stat[0]}, AVG: {stat[1]}, MAX: {stat[2]}, MIN: {stat[3]}")


# print("\n--- Агрегационные функции ---")
# get_average_age()
# get_grade_statistics()

# Вложенные запросы
def get_users_with_highest_grade():
    cursor.execute("""
        SELECT fio, subject, grade
        FROM users JOIN grades ON users.userid = grades.userid
        WHERE grade = (SELECT MAX(grade) FROM grades)
    """)

    users = cursor.fetchall()
    print(f"Пользователи с максимальным баллом")
    usr = users.objects.all()
    usr.fio.filter(id=1)

    for i in users:
        print(f"FIO: {i[0]}, SUB: {i[1]}, GR: {i[2]}")


# print(f"--------Вложенные запросы---------")
# get_users_with_highest_grade()


# Views (Представления)
def create_users_view():
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS user_view AS
        SELECT fio, age, hobby
        FROM users
        WHERE age < 26

    """)
    users = cursor.fetchall()
    print("молодые пользователи")


def get_young_users():
    cursor.execute('SELECT * FROM user_view')
    young_users = cursor.fetchall()
    print("Молодые пользователи (моложе 30 лет):")
    for user in young_users:
        print(f"FIO: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")

# print('наше Views (Представления)')
# create_users_view()
# get_young_users()




