from typing import Any

from notes.models.Methods import Methods
from notes.view.View import View


class Controller:
    __model: Any
    __view: Any

    def __init__(self) -> object:
        self.model = Methods()
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
        from_user = ''
        while from_user != '6':
            View.menu()
            from_user = input().strip()
            match from_user:
                case '1':
                    return self.add_note()

                case '2':
                    return self.save_notes()

                case '3':
                    return self.edit_note()

                case '4':
                    return self.delete_note()

                case '5':
                    return self.show()

                case _:
                    raise Exception
