import datetime
import uuid
from abc import ABC, abstractmethod

import view


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
    def __init__(self, title_note, msg, date_note):
        super().__init__()
        self.id_note = str(uuid.UUID()[0:3])
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
            ';\n Заметка >>> \n' + self.msg + ';\n Дата >>> \n' + self.date_note

class WorkFile():
    def write(self, array, mode):
        array = []
        #f = open('notes.csv', mode='w', encoding='utf-8')
        # f.seek(1)
        #f.close()
        f.open('notes.csv', mode=mode, encoding='utf-8')
        for note in array:
            f.write(str(note))
            f.write('\n')
        f.close()

    def read(self):
        try:
            array = []
            f = open('notes.csv', 'r', encoding='utf-8')
            notes = f.read().strip().split('\n')
            for i in notes:
                str_split = i.split(';')
                note = Notes(id_note=str_split[0], title_note=str_split[1], msg=str_split[2], date_note=str_split[3])
        except Exception:
            print('Сохраненных заметок не найдено')
        finally:
            return note
