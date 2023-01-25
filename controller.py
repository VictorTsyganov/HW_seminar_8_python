from model import Journal
import view

def input_handler(inp: int, journal, choice_list):
    if inp == 1:
        view.show_all(journal)
    if inp == 2:
        view.student_who_will_answer(journal)
    if inp == 3:
        Journal(choice_list[0], choice_list[1]).save_db()
        view.success_save()
    if inp == 4:
        view.exit_program()
    else:
        pass

def start():
    choice_list = view.choice_class_and_subject()
    journal = Journal(choice_list[0], choice_list[1]).read_db()
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp, journal, choice_list)