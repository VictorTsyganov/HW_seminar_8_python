def chek_user_num_input(min_val, max_val):
    while True:
        try:
            user_input = int(input('Input number '))
            if user_input in range(min_val, max_val):
                return user_input
            else:
                print('Wrong_input')
                
        except:
            print('Wrong_input')

def chek_user_sub_input():
    control_list = ['математика', 'химия', 'физика']
    while True:
        try:
            user_input = input('Input subject name ')
            if user_input.lower() in control_list:
                return user_input
            else:
                print('Wrong_input. This subject not in list.')
                
        except:
            print('Wrong_input. This subject not in list.')

def main_menu():
    print('Menu_list')
    menu_list = [
        'Show_students_and_grades',
        'Choice_student_who_will_answer',
        'Save_grades',
        'Exit'
    ]

    for i in range(len(menu_list)):
        print(f'\t{i+1}. {menu_list[i]}')

    print('Enter_command: ')
    user_input = chek_user_num_input(1, 5)
    return user_input

def show_all(db: dict):
    print()
    for i, key, in enumerate(db, 1):
        print(f"{i}. Student {key} have grades {db.get(key)}")
    print()

def choice_class_and_subject():
    print(f'\tSchool Journal. Select class and subject:')
    user_input = []
    print('Enter class number: ')
    user_input.append(str(chek_user_num_input(7, 9)))
    print('Enter subject: ')
    user_input.append(chek_user_sub_input())
    print('Success operation!')
    return user_input

def exit_program():
    print('Mission completed!')
    exit()

def student_who_will_answer(db: dict):
    show_all(db)
    print('Select_student_who_will_answer: ')
    student = chek_user_num_input(1, len(db.items()) + 1)
    print("Select_student's_grade: ")
    grade = chek_user_num_input(1, 6)
    for i, key, in enumerate(db, 1):
        if student == i:
            db.get(key).append(grade)
    return db

def success_save():
    print(f'\tGrades saved!')