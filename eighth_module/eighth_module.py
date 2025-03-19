import sqlite3

conn = sqlite3.connect('db_sqlite.sqlite')

cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        surname TEXT NOT NULL, 
        age INTEGER, 
        city TEXT NOT NULL
    )
    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        time_start TEXT NOT NULL, 
        time_end TEXT NOT NULL
    )
    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Student_courses (
        student_id INTEGER, 
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES Students(id),
        FOREIGN KEY (course_id) REFERENCES Courses(id)
    )
    '''
)

cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", [
    (1, 'python', '21.07.21', '21.08.21'),
    (2, 'java', '13.07.21', '16.08.21')
])

cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", [
    (1, 'Max', 'Brooks', 24, 'Spb'),
    (2, 'John', 'Stones', 15, 'Spb'),
    (3, 'Andy', 'Wings', 45, 'Manhester'),
    (4, 'Kate', 'Brooks', 34, 'Spb')
])

cursor.executemany("INSERT INTO Student_courses VALUES (?, ?)", [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2)
])


cursor.execute("SELECT name, surname FROM Students WHERE age > 30")
print("Студенты старше 30 лет: ", cursor.fetchall())
# [('Andy', 'Wings'), ('Kate', 'Brooks')]

cursor.execute(
    '''
        SELECT Students.name, Students.surname
        FROM Students
        JOIN Student_courses ON Students.id = Student_courses.student_id
        JOIN Courses ON Courses.id = Student_courses.course_id
        WHERE Courses.name = 'python'
    '''
)
print("Студенты, которые проходят курс по python: ", cursor.fetchall())
# [('Max', 'Brooks'), ('John', 'Stones'), ('Andy', 'Wings')]

cursor.execute(
    '''
        SELECT Students.name, Students.surname
        FROM Students
        JOIN Student_courses ON Students.id = Student_courses.student_id
        JOIN Courses ON Courses.id = Student_courses.course_id
        WHERE Courses.name = 'python' AND Students.city = 'Spb'
    '''
)
print("Студенты, которые проходят курс по python и из Spb: ", cursor.fetchall())
# [('Max', 'Brooks'), ('John', 'Stones')]

conn.commit()
conn.close()
