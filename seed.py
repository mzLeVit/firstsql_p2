import random
from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from my_models import Base, Student, Group, Teacher, Subject, Grade

DATABASE_URL = 'sqlite:///university.db'

# engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Faker 2 work
fake = Faker()

def create_groups(num_groups=3):
    groups = [Group(name=f'Group {i+1}') for i in range(num_groups)]
    session.add_all(groups)
    session.commit()
    return groups

def create_teachers(num_teachers=5):
    teachers = [Teacher(name=fake.name()) for _ in range(num_teachers)]
    session.add_all(teachers)
    session.commit()
    return teachers

def create_subjects(teachers, num_subjects=8):
    subjects = [Subject(name=fake.word().capitalize(), teacher=random.choice(teachers)) for _ in range(num_subjects)]
    session.add_all(subjects)
    session.commit()
    return subjects

def create_students(groups, num_students=50):
    students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(num_students)]
    session.add_all(students)
    session.commit()
    return students

def create_grades(students, subjects, num_grades=20):
    grades = []
    for student in students:
        for _ in range(num_grades):
            grade = Grade(
                student=student,
                subject=random.choice(subjects),
                score=random.randint(1, 100),
                date=fake.date_between(start_date='-1y', end_date='today')
            )
            grades.append(grade)
    session.add_all(grades)
    session.commit()

def main():
    # Create tables
    Base.metadata.create_all(engine)

    # Generate random data
    groups = create_groups()
    teachers = create_teachers()
    subjects = create_subjects(teachers)
    students = create_students(groups)
    create_grades(students, subjects)

    print("Database generated successfully!")

if __name__ == '__main__':
    main()
