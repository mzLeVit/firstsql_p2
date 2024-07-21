from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import create_engine, func
from my_models import Student, Group, Teacher, Subject, Grade

DATABASE_URL = 'sqlite:///university.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    return session.query(Student.name, func.avg(Grade.score).label('average_score'))\
                  .join(Grade)\
                  .group_by(Student.id)\
                  .order_by(func.avg(Grade.score).desc())\
                  .limit(5)\
                  .all()

def select_2(subject_id):
    # Знайти студента із найвищим середнім балом з певного предмета.
    return session.query(Student.name, func.avg(Grade.score).label('average_score'))\
                  .join(Grade)\
                  .filter(Grade.subject_id == subject_id)\
                  .group_by(Student.id)\
                  .order_by(func.avg(Grade.score).desc())\
                  .first()

def select_3(subject_id):
    # Знайти середній бал у групах з певного предмета.
    return session.query(Group.name, func.avg(Grade.score).label('average_score'))\
                  .join(Student, Student.group_id == Group.id)\
                  .join(Grade, Grade.student_id == Student.id)\
                  .filter(Grade.subject_id == subject_id)\
                  .group_by(Group.id)\
                  .all()

def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    return session.query(func.avg(Grade.score)).scalar()

def select_5(teacher_id):
    # Знайти які курси читає певний викладач.
    return session.query(Subject.name)\
                  .filter(Subject.teacher_id == teacher_id)\
                  .all()

def select_6(group_id):
    # Знайти список студентів у певній групі.
    return session.query(Student.name)\
                  .filter(Student.group_id == group_id)\
                  .all()

def select_7(group_id, subject_id):
    # Знайти оцінки студентів у окремій групі з певного предмета.
    return session.query(Student.name, Grade.score)\
                  .join(Grade)\
                  .filter(Student.group_id == group_id, Grade.subject_id == subject_id)\
                  .all()

def select_8(teacher_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    return session.query(func.avg(Grade.score))\
                  .join(Subject)\
                  .filter(Subject.teacher_id == teacher_id)\
                  .scalar()

def select_9(student_id):
    # Знайти список курсів, які відвідує певний студент.
    return session.query(Subject.name)\
                  .join(Grade)\
                  .filter(Grade.student_id == student_id)\
                  .group_by(Subject.id)\
                  .all()

def select_10(student_id, teacher_id):
    # Список курсів, які певному студенту читає певний викладач.
    return session.query(Subject.name)\
                  .join(Grade)\
                  .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)\
                  .group_by(Subject.id)\
                  .all()

def avg_grade_by_teacher_for_student(student_id, teacher_id):
    # Середній бал, який певний викладач ставить певному студентові.
    return session.query(func.avg(Grade.score).label('average_score'))\
                  .join(Subject, Grade.subject_id == Subject.id)\
                  .join(Teacher, Subject.teacher_id == Teacher.id)\
                  .filter(Grade.student_id == student_id)\
                  .filter(Teacher.id == teacher_id)\
                  .scalar()

def grades_last_session_in_group(subject_id, group_id):
    # Оцінки студентів у певній групі з певного предмета на останньому занятті.
    subquery = (
        session.query(Grade.student_id, func.max(Grade.date).label('last_date'))
        .join(Student, Student.id == Grade.student_id)
        .filter(Student.group_id == group_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Grade.student_id)
        .subquery()
    )
    subquery_alias = aliased(subquery)


    return (
        session.query(Student.id, Student.name, Grade.score, Grade.date)
        .join(Grade, Grade.student_id == Student.id)
        .join(subquery_alias, (Grade.student_id == subquery_alias.c.student_id) & (Grade.date == subquery_alias.c.last_date))
        .filter(Student.group_id == group_id)
        .filter(Grade.subject_id == subject_id)
        .all()
    )
