import json
from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def create_note(self):
        """
        создать заметку
        :return:
        """
        pass

    @abstractmethod
    def save_notes(self):
        """
        сохранить заметку
        :return:
        """
        pass

    @abstractmethod
    def read_notes(self):
        """
        чтение списка заметок
        :return:
        """
        pass

    @abstractmethod
    def edit_note(self):
        """
        редактировать заметку
        :return:
        """
        pass

    @abstractmethod
    def delete_note(self):
        """
        удалить заметку
        :return:
        """
        pass

class Notes(Abstract):
    def __init__(self, id_note, title_note, msg, datetime=None):
        super().__init__()
        self.id_note = id_note
        self.title_note = title_note
        self.msg = msg
        self.date_note = datetime.date.today().strftime('%d.%n.%y %H:%M:%S')

    @property
    def id_note(self):
        return self.__id_note

    @id_note.setter
    def id_note(self, id_note: str):
        self.__id_note = id_note

    @property
    def title_note(self):
        return self.__title_note

    @title_note.setter
    def title_note(self, title_note: str):
        self.__title_note = title_note

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return self.id_note + ';\n' + self.title_note + ';\n' + self.msg + ';\n' + self.date_note
    def __repr__(self):
        return 'Id ' + self.id_note + ';\n Тема заметки >>> \n' + self.title_note + \
            ';\n Дата >>> \n' + self.date_note

class WorkFile:
    def write(self, note: Notes):
        title = [note.text for title in note]
        with open(f'notes.json', 'a',) as file:  # Открываем json файл
            json.dump(note, file)  # И записываем туда список в формате json

    def read(self):
        with open('notes.json', 'r', encoding='utf-8') as file:  # открываем файл на чтение
            dict_notes = json.load(file)  # загружаем из файла данные в словарь
            dict_notes = sorted(dict_notes, key=lambda x: x['time'])
        return dict_notes

    def save(self, note: Notes):
        with open('notes.json', 'w', encoding='UTF-8') as file:
            json.dump(note, file, ensure_ascii=False, default=str)

