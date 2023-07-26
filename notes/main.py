"""
Задание 1. Приложение заметки (Python)
Необходимо написать проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её, читать список заметок,
редактировать заметку, удалять заметку.
"""
from notes import repository
from notes import controller, file_operation
from notes import view

def main():
    file = file_operation.FileOperation('../notes.csv')
    repo = repository.Repository(file)
    _controller = controller.Controller(repo)
    _view = view.View(_controller)
    _view.run()

if __name__ == '__main__':
    main()
