from peewee import *

database = SqliteDatabase('db_orm.sqlite')


class BaseModel(Model):
    class Meta:
        database = database


class Students(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    surname = CharField()
    age = IntegerField()
    city = CharField()


class Courses(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    time_start = CharField()
    time_end = CharField()


class StudentCourses(BaseModel):
    student_id = ForeignKeyField(Students, backref='students')
    course_id = ForeignKeyField(Courses, backref='courses')


database.connect()
database.create_tables([Students, Courses, StudentCourses])

students_data = [
    (1, 'Max', 'Brooks', 24, 'Spb'),
    (2, 'John', 'Stones', 15, 'Spb'),
    (3, 'Andy', 'Wings', 45, 'Manhester'),
    (4, 'Kate', 'Brooks', 34, 'Spb')
]

courses_data = [
    (1, 'python', '21.07.21', '21.08.21'),
    (2, 'java', '13.07.21', '16.08.21')
]

student_courses_data = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2)
]

# students = Students.insert_many(students_data).execute()
# courses = Courses.insert_many(courses_data).execute()
# student_courses = StudentCourses.insert_many(student_courses_data).execute()


def get_students_by_age(age):
    result = []
    query = Students.select().where(Students.age > age)

    for student in query:
        result.append(f'{student.name} {student.surname}')

    return result


def get_students_by_course(course):
    result = []
    query = Students.select().join(StudentCourses).join(
        Courses).where(Courses.name == course)

    for student in query:
        result.append(f'{student.name} {student.surname}')

    return result


def get_students_by_course_and_city(course, city):
    result = []
    query = Students.select().join(StudentCourses).join(
        Courses).where(Courses.name == course).where(Students.city == city)

    for student in query:
        result.append(f'{student.name} {student.surname}')

    return result


# Функция добавления студента на курс
def add_student_to_course(student_id, course_id):
    StudentCourses.create(student_id=student_id, course_id=course_id)


# Функция удаления студента и его записей о курсах
def delete_student(student_id):
    StudentCourses.delete().where(StudentCourses.student_id == student_id).execute()
    Students.get_by_id(student_id).delete_instance()


# print("Студенты старше 30 лет: ", get_students_by_age(30))
# ['Andy Wings', 'Kate Brooks']

# print("Студенты, которые проходят курс по python: ",
    #   get_students_by_course('python'))
# ['Max Brooks', 'John Stones', 'Andy Wings']

# print("Студенты, которые проходят курс по python и из Spb: ",
    #   get_students_by_course_and_city('python', 'Spb'))
# ['Max Brooks', 'John Stones']

database.close()
