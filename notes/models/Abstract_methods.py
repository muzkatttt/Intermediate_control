from abc import ABC, abstractmethod


class Abstract_methods(ABC):
    pass
    @abstractmethod
    def create_note(self): # создать заметку
        pass

    @abstractmethod
    def save_notes(self): # сохранить заметку
        pass

    @abstractmethod
    def read_notes(self): # чтение списка заметок
        pass

    @abstractmethod
    def edit_note(self): # редактировать заметку
        pass

    @abstractmethod
    def delete_note(self):
        pass