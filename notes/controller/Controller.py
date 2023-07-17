from typing import Any, NoReturn

from notes.models.Methods_of_working_with_notes import Methods_of_working_with_notes
from notes.view.View import View


class Controller:
    __model: Any
    __view: Any

    def __init__(self) -> object:
        self.model = Methods_of_working_with_notes()
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
        values = self.view.input_from_user()
        result = self.model(*values).get_result()
        self.view.print_result(result)

    # def ask_for_log(self):
    #     if self.log_result == '':
    #         return
    #     log_result = Logger(self.log_result)
    #     log_result.ask_from_user('Cохранить в log.txt? [y/n]\n')