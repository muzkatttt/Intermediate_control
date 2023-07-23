from typing import Any
from view import View


class Controller:
    __model: Any
    __view: Any

    def __init__(self):
        self.model = Methods
        self.view = View()

    @property
    def model(self) -> Any:
        return self.__model

    @model.setter
    def model(self, model: Any):
        self.__model = model

    @property
    def view(self) -> Any:
        return self.__view

    @view.setter
    def view(self, view: Any):
        self.__view = view

    def start(self):
        choice = ''
        '''
        while choice != '0':
            View.menu()
            choice = input().strip()
            if choice == '1':
                Methods.add_note(self)

            if choice == '2':
                Methods.show(self)
                Methods.edit_note(self)

            if choice == '3':
                Methods.show(self)
                Methods.delete_note(self)

            if choice == '4':
                Methods.show(self)
                Methods.show(self)

            if choice == '5':
                Methods.show(self)
                Methods.show(self)

            if choice == '0':
                View.ending(self)
                break
'''
        while choice != '0':
            View.menu()
            choice = input().strip()
            match choice:
                case '1':
                    Methods.add_note(self)
                    return 'notes.csv'

                case '2':
                    Methods.show(self)
                    return Methods.edit_note(self)

                case '3':
                    Methods.show(self)
                    return Methods.delete_note(self)

                case '4':
                    Methods.show(self)
                    return Methods.show(self)

                case '5':
                    Methods.show(self)
                    return Methods.show(self)

                case '0':
                    View.ending(self)
                    break

                case _:
                    raise Exception

    def add_note():
        note: None = create_note()
        array = Work_file.read_doc
        array.append(note)
        Work_file.write_doc(array, 'a')
        print('Заметка добавлена')

    def show(self, text):
        flag = True
        array = Work_file.read_doc
        if text == 'date':
            date = input('Введите дату заметки в формате дд.мм.гггг: >>> ')
            for notes in array:
                if text == 'all':
                    flag = False
                    print(Notes.print_note)
                if text == 'id_note':
                    flag = False
                    print('Id заметки: ' + get_id_note(notes))
                if text == 'date':
                    flag = False
                    if date in get_date_note(notes):
                        print(print_note(notes))
        if flag:
            print('Заметок не найдено')

    def edit_note(self):
        id_note = input('Введите Id заметки >>> ')
        array = Work_file.read_doc
        flag = True
        for notes in array:
            if id_note == get_id_note(notes):
                flag = False
                if text == 'edit_note':
                    note = create_note()
                    Notes.set_title_note(notes, note.get_title_note())
                    Notes.set_msg(notes, note.get_msg)
                    Notes.set_date_note(notes)
                    print('Изменения внесены')
                if text == 'delete':
                    array.remove(notes)
                    print('Удалено успешно')
                if text == 'show':
                    print(Notes.print_note)
        if flag:
            print('Заметки нет, введите корректный Id и повторите ввод')
        Work_file.write_doc(array, 'a')
