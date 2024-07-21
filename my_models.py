from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    students = relationship('Student', back_populates='group')

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    subjects = relationship('Subject', back_populates='teacher')

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship('Teacher', back_populates='subjects')
    grades = relationship('Grade', back_populates='subject')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    score = Column(Integer, nullable=False)  # Ensure this column is defined
    date = Column(Date, nullable=False)

    student = relationship('Student', back_populates='grades')
    subject = relationship('Subject', back_populates='grades')


# Create an engine
engine = create_engine('sqlite:///university.db')

# Create all tables
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Example usage:
if __name__ == "__main__":
    # Add groups
    group1 = Group(name="Group 1")
    group2 = Group(name="Group 2")
    session.add(group1)
    session.add(group2)
    session.commit()

    # Add students
    student1 = Student(name="Student 1", group=group1)
    student2 = Student(name="Student 2", group=group2)
    session.add(student1)
    session.add(student2)
    session.commit()

    # Add teachers
    teacher1 = Teacher(name="Teacher 1")
    teacher2 = Teacher(name="Teacher 2")
    session.add(teacher1)
    session.add(teacher2)
    session.commit()

    # Add subjects
    subject1 = Subject(name="Math", teacher=teacher1)
    subject2 = Subject(name="History", teacher=teacher2)
    session.add(subject1)
    session.add(subject2)
    session.commit()

    # Add grades
    grade1 = Grade(student=student1, subject=subject1, grade=90.5)
    grade2 = Grade(student=student2, subject=subject2, grade=85.0)
    session.add(grade1)
    session.add(grade2)
    session.commit()

    # Query the database
    students = session.query(Student).all()
    for student in students:
        print(f"Student: {student.name}, Group: {student.group.name}")
        for grade in student.grades:
            print(f"  Subject: {grade.subject.name}, Grade: {grade.grade}, Date: {grade.date_received}")

    session.close()
