from typing import Any, NoReturn

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
    def model(self, model: Any) -> NoReturn:
        self.__model = model

    @property
    def view(self) -> Any:
        return self.__view

    @view.setter
    def view(self, view: Any) -> NoReturn:
        self.__view = view

    def start(self) -> NoReturn:
        #from_user = ''
        # while from_user != '7':
            View.menu()
            from_user = input().strip()
            if from_user == '1':
                # вчера закончила работу здесь, доделать 19.07
                pass

