from typing import Any
from notes import models
from notes.models.Methods import Methods
from notes.view.View import View


class Controller:
    __model: Any
    __view: Any

    def __init__(self):
        self.model = models.Methods
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

    @property
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
