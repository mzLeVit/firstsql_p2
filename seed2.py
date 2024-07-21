import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from my_models import Base, Student, Group, Teacher, Subject, Grade


DATABASE_URL = "sqlite:///university.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_teacher(name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    print(f"Teacher '{name}' created.")

def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"ID: {teacher.id}, Name: {teacher.name}")

def update_teacher(teacher_id, name):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        teacher.name = name
        session.commit()
        print(f"Teacher with ID {teacher_id} updated to '{name}'.")
    else:
        print(f"Teacher with ID {teacher_id} not found.")

def remove_teacher(teacher_id):
    teacher = session.query(Teacher).get(teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher with ID {teacher_id} removed.")
    else:
        print(f"Teacher with ID {teacher_id} not found.")

def main():
    parser = argparse.ArgumentParser(description="CLI for CRUD operations with database.")
    parser.add_argument('--action', '-a', required=True, help='Action to perform (create, list, update, remove)')
    parser.add_argument('--model', '-m', required=True, help='Model to perform action on (Teacher, Student, Group, Subject, Grade)')
    parser.add_argument('--id', type=int, help='ID of the record to update or remove')
    parser.add_argument('--name', help='Name of the teacher to create or update')

    args = parser.parse_args()

    if args.model == 'Teacher':
        if args.action == 'create':
            if args.name:
                create_teacher(args.name)
            else:
                print("Name is required for create action.")
        elif args.action == 'list':
            list_teachers()
        elif args.action == 'update':
            if args.id and args.name:
                update_teacher(args.id, args.name)
            else:
                print("ID and Name are required for update action.")
        elif args.action == 'remove':
            if args.id:
                remove_teacher(args.id)
            else:
                print("ID is required for remove action.")
        else:
            print(f"Unknown action: {args.action}")



if __name__ == "__main__":
    main()
