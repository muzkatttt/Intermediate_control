from datetime import datetime
from typing import Any

from notes import models

import models
import view



class Controller:

    def __init__(self):
        self.model: models = models
        self.view = view.View()

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

    def add_note(self, note):
        note: None = self.view.create()
        self.model.WorkFile().write(note)
        print('Заметка добавлена')

    def show(self, note):
        array = self.model.WorkFile().read()
        choice = ''
        match choice:
            case 'all':
                self.view.ending(array)
            case 'id_note':
                print(sorted(array))
            case 'date':
                datetime.sort(array)
                print(array)
            case _:
                print('Сортировка не задана')

    def edit(self, note, flag=None):
        flag == True
        id_note = input('Введите Id заметки >>> ')
        array = self.model.read()
        if flag == id_note(note):
            input('редактировать заголовок заметки - 1\n'
                'редактировать заметку - 2\n'
                'удалить заметку - 3\n >>> ')
            choice = ''
            match choice:
                case '1':
                    title_note = input('Введите заголовок \n>>> ')
                    array.append(title_note)
                case '2':
                    msg = input('Введите текст заметки \n>>> ')
                    array.append(msg)
                case '3':
                    array.remove(note)
                case _:
                    print('Данных недостаточно')

    def start(self):
        choice = ''
        while choice != '0':
            self.view.menu()
            choice = input().strip()
            match choice:
                case '1':
                    self.model.add_note()
                    return 'notes.csv'

                case '2':
                    self.model.show()
                    return self.model.edit_note()

                case '3':
                    self.model.show()
                    return self.model.delete_note()

                case '4':
                    self.model.show()
                    return self.model.show('date')

                case '5':
                    self.model.show(text='id_note')
                    return self.model.show('id_note')

                case '0':
                    self.view.ending()
                    break

                case _:
                    raise Exception
