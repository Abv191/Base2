# seed.py
import random
from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import Base, Group, Student, Teacher, Subject, Grade
from db import engine, Session

faker = Faker()

# Налаштування сесії
session = Session()

# Створення таблиць
Base.metadata.create_all(engine)

# Заповнення таблиць даними
group_names = ["Group A", "Group B", "Group C"]
for name in group_names:
    session.add(Group(name=name))

teachers = [Teacher(name=faker.name()) for _ in range(5)]
session.add_all(teachers)

subjects = ["Math", "History", "Physics", "Chemistry", "Biology", "Literature", "Art", "Computer Science"]
for name in subjects:
    teacher_id = random.choice(teachers).id
    session.add(Subject(name=name, teacher_id=teacher_id))

groups = session.query(Group).all()
students = []
for _ in range(50):
    name = faker.name()
    group_id = random.choice(groups).id
    students.append(Student(name=name, group_id=group_id))
session.add_all(students)

students = session.query(Student).all()
subjects = session.query(Subject).all()
for _ in range(1000):
    student_id = random.choice(students).id
    subject_id = random.choice(subjects).id
    grade = random.randint(1, 10)
    date = faker.date_this_year()
    session.add(Grade(student_id=student_id, subject_id=subject_id, grade=grade, date=date))

# Збереження змін
session.commit()
session.close()
