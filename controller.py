import datetime
import controller
import models
import view

class Controller:

    def __init__(self):
        self.model = models.Notes
        self.view = view.View()

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, view):
        self.__view = view


    def add_note(self, note=models.Notes):
        note: None = view.create()
        self.model.WorkFile().write(note)
        print('Заметка добавлена')


    def show(self, note):
        my_note = dict(
            title_note='Заголовок',
            msg='Заметка',
            time='Дата'
        )
        print(str(note))


    def edit(self, note):
        Controller.show(note)
        number = int(input('Введите номер заметки для поиска\n>>> '))
        if number == note.id_note():
            input('редактировать заголовок заметки - 1\n'
                'редактировать заметку - 2\n'
                'удалить заметку - 3\n >>> ')
            choice = ''
            match choice:
                case '1':
                    title_note = input('Введите заголовок \n>>> ')
                    note.append(title_note=title_note)
                    models.WorkFile.save(note)
                case '2':
                    msg = input('Введите текст заметки \n>>> ')
                    note.append(msg=msg)
                    models.WorkFile.save(note)
                case '3':
                    note.remove(self)
                case _:
                    print('Данных недостаточно')
        else:
            print('Заметка не найдена')

    def start(self):
        choice = ''
        while choice != '0':
            self.view.menu()
            choice = input().strip()
            match choice:
                case '1':
                    Controller.add_note(self, note=models.Notes)
                    return 'notes.json'

                case '2':
                    Controller.show(self)
                    return Controller.edit()

                case '3':
                    return Controller.show(datetime)

                case '4':
                    return Controller.show()

                case '0':
                    self.view.ending()
                    break

                case _:
                    raise Exception