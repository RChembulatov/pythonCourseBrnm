import unittest
from peewee import SqliteDatabase
from eighth_module_orm import Students, Courses, StudentCourses, BaseModel, add_student_to_course, delete_student

test_db = SqliteDatabase(':memory:')

BaseModel._meta.database = test_db
Students._meta.database = test_db
Courses._meta.database = test_db
StudentCourses._meta.database = test_db


class TestORMOperations(unittest.TestCase):

    def setUp(self):
        test_db.bind([Students, Courses, StudentCourses])
        test_db.connect()
        test_db.create_tables([Students, Courses, StudentCourses])

    def tearDown(self):
        test_db.drop_tables([Students, Courses, StudentCourses])
        test_db.close()

    def test_add_student(self):
        Students.create(id=1, name='TestName',
                        surname='TestSurname', age=30, city='TestCity')
        student = Students.get(Students.id == 1)

        self.assertEqual(student.name, 'TestName')
        self.assertEqual(student.surname, 'TestSurname')
        self.assertEqual(student.age, 30)
        self.assertEqual(student.city, 'TestCity')

    def test_add_course(self):
        Courses.create(id=1, name='TestCourses',
                       time_start='01.01.25', time_end='01.02.25')
        course = Courses.get(Courses.id == 1)

        self.assertEqual(course.name, 'TestCourses')
        self.assertEqual(course.time_start, '01.01.25')
        self.assertEqual(course.time_end, '01.02.25')

    def test_delete_student(self):
        Students.create(id=2, name='TestName2',
                        surname='TestSurname2', age=30, city='TestCity2')
        student = Students.get(Students.id == 2)

        self.assertEqual(student.name, 'TestName2')

        student.delete_instance()

        with self.assertRaises(Students.DoesNotExist):
            Students.get(Students.id == 2)

    def test_add_and_delete_student_course(self):
        student = Students.create(
            id=1, name='TestName3', surname='TestSurname3', age=30, city='TestCity3')
        course = Courses.create(id=1, name='TestCourses3',
                                time_start='01.01.25', time_end='01.02.25')

        add_student_to_course(student.id, course.id)

        link = StudentCourses.get((StudentCourses.student_id == student.id) & (
            StudentCourses.course_id == course.id))

        self.assertEqual(link.student_id.id, student.id)
        self.assertEqual(link.course_id.id, course.id)

        delete_student(student.id)

        with self.assertRaises(Students.DoesNotExist):
            Students.get_by_id(student.id)

        self.assertEqual(StudentCourses.select().where(
            StudentCourses.student_id == student.id).count(), 0)


unittest.main()
