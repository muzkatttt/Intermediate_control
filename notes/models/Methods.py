import datetime
import uuid
from abc import ABC

from notes import view
from notes.models.Abstract_methods import Abstract_methods
import notes.view.View


class Notes(Abstract_methods, ABC):
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


class Methods(Abstract_methods, ABC):

    def add_note(self):
        note: None = view.create_note(self)
        array = Work_file.read_doc
        for notes in array:
            if get_id_note(note) == get_id_note(notes):
                Notes.set_id_note(note)
        array.append(note)
        Work_file.write_doc(self, array, 'a')
        print('Заметка добавлена')

    def show(self, text):
        flag = True
        array = Work_file.read_doc
        if text == 'date':
            date = input('Введите дату заметки в формате дд.мм.гггг: >>> ')
            for notes in array:
                if text == 'all':
                    flag = False
                    print(Notes.print_note(notes))
                if text == 'id_note':
                    flag = False
                    print('Id заметки: ' + get_id_note(notes))
                if text == 'date':
                    flag = False
                    if date in get_date_note(notes):
                        print(print_note(notes))
        if flag:
            print('Заметок не найдено')

    def edit_note(self):
        id_note = input('Введите Id заметки >>> ')
        array = Work_file.read_doc
        flag = True
        for notes in array:
            if id_note == Notes.get_id_note(notes):
                flag = False
                if text == 'edit_note':
                    note = View.create_note
                    Notes.set_title_note(notes, note.get_title_note())
                    Notes.set_msg(notes, note.get_msg)
                    Notes.set_date_note(notes)
                    print('Изменения внесены')
                if text == 'delete':
                    array.remove(notes)
                    print('Удалено успешно')
                if text == 'show':
                    print(Notes.print_note(notes))
        if flag:
            print('Заметки нет, введите корректный Id и повторите ввод')
        Work_file.write_doc(array, 'a')

class Work_file():

    def write_doc(self, array, mode):
        array = []
        #f = open('notes.csv', mode='w', encoding='utf-8')
        # f.seek(1)
        #f.close()
        f.open('notes.csv', mode=mode, encoding='utf-8')
        for note in array:
            f.write(to_string(note))
            f.write('\n')
        f.close()

    @property
    def read_doc(self):
        try:
            array = []
            f = open('notes.csv', 'r', encoding='utf-8')
            notes = f.read().strip().split('\n')
            for i in notes:
                str_split = i.split('.')
                note = Notes(id_note=str_split[0], title_note=str_split[1], msg=str_split[2], date_note=str_split[3])
        except Exception:
            print('Сохраненных заметок не найдено')
        finally:
            return note
