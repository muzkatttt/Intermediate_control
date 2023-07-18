import datetime
import uuid

from notes.models.Abstract_methods import Abstract_methods


class Methods(Abstract_methods):
    __id_note: str
    __title_note: str
    __msg: str
    __date_note: datetime.date.today().strftime('%d.%m.%y %H:%M:%S')

    def __init__(self, id_note, title_note, msg, date_note):
        super().__init__()
        self.__id_note = id_note
        self.__title_note = title_note
        self.__msg = msg
        self.__date_note = date_note

    @property
    def get_id_note(self):
        return self.id_note

    @get_id_note.setter
    def set_id_note(self, id_note: str(uuid.uuid1())[0:5]):
        self.__id_note = id_note

    @property
    def get_title_note(self):
        return self.title_note

    @get_title_note.setter
    def set_title_note(self, title_note: str):
        self.__title_note = title_note

    @property
    def get_msg(self):
        return self.__msg

    @get_msg.setter
    def set_msg(self, msg: str):
        self.__msg = msg

    @property
    def get_date_note(self):
        return self.__date_note

    @get_date_note.setter
    def set_date_note(self, date_note: datetime.date.today().strftime('%d.%m.%y %H:%M:%S')):
        self.__date_note = str(datetime.date.today().strftime('%d.%m.%y %H:%M:%S'))

    def to_string(self):
        return self.get_id_note() + ';\n' + self.get_title_note() + ';\n' + self.get_msg() + ';\n' + self.__date_note()

    def print_note(self):
        return 'Id ' + self.get_id_note() + ';\n Тема заметки >>> \n' + self.get_title_note() + \
            ';\n Заметка >>> \n' + self.get_msg() + ';\n Дата >>> \n' + self.__date_note()

"""
    def create_note(self):
        # return f = open('note.txt', 'w')
        pass

    def save_notes(self):
        pass

    def read_notes(self):
        pass

    def edit_note(self):
        pass

    def delete_note(self):
        pass

    def select_action(self):
        match self.__note:
            case '1':
                return self.create_note()

            case '2':
                return self.save_notes()

            case '3':
                return self.read_notes()

            case '4':
                return self.edit_note()

            case '5':
                return self.delete_note()

            case _:
                raise Exception

"""