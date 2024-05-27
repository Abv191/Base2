# my_select.py
from sqlalchemy import func, desc
from models import Student, Grade, Subject, Group
from db import Session

# Налаштування сесії
session = Session()

def select_1():
    return session.query(
        Student.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_id):
    return session.query(
        Student.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()

def select_3(subject_id):
    return session.query(
        Group.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Student).join(Grade).filter(Grade.subject_id == subject_id).group_by(Group.id).all()

def select_4():
    return session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).all()

def select_5(teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

def select_6(group_id):
    return session.query(Student.name).filter(Student.group_id == group_id).all()

def select_7(group_id, subject_id):
    return session.query(
        Student.name,
        Grade.grade,
        Grade.date
    ).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()
