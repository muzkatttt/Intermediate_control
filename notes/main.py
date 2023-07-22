"""
Задание 1. Приложение заметки (Python)
Необходимо написать проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её, читать список заметок,
редактировать заметку, удалять заметку.
"""


from notes.controller.Controller import Controller


def main():
    controller = Controller()
    controller.start()


if __name__ == '__main__':
    main()
