from my_select import *


def main():
    print("5 students with the highest average score:")
    for result in select_1():
        print(result)

    subject_id = 1  # subject ID
    print(f"\nStudent with the highest average score in subject {subject_id}:")
    print(select_2(subject_id))

    print(f"\nAverage score in groups for subject {subject_id}:")
    for result in select_3(subject_id):
        print(result)

    print("\nAverage score across all grades:")
    print(select_4())

    teacher_id = 1  # teacher ID
    print(f"\nCourses taught by teacher {teacher_id}:")
    for result in select_5(teacher_id):
        print(result)

    group_id = 1  # group ID
    print(f"\nStudents in group {group_id}:")
    for result in select_6(group_id):
        print(result)

    print(f"\nGrades of students in group {group_id} for subject {subject_id}:")
    for result in select_7(group_id, subject_id):
        print(result)

    print(f"\nAverage score given by teacher {teacher_id}:")
    print(select_8(teacher_id))

    student_id = 1  # student ID
    print(f"\nCourses attended by student {student_id}:")
    for result in select_9(student_id):
        print(result)

    print(f"\nCourses taught by teacher {teacher_id} to student {student_id}:")
    for result in select_10(student_id, teacher_id):
        print(result)


if __name__ == '__main__':
    main()
