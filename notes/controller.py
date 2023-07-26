from notes import repository
from notes import note


class Controller:
    def __init__(self, _repository):
        self.__repository = _repository

    def read_note(self, note_id):
        if isinstance(self.__repository, repository.Repository):
            notes = self.__repository.get_all_notes()
            for _note in notes:
                if isinstance(_note, note.Note):
                    if _note.get_id() == note_id:
                        return _note
                else:
                    print('Ошибка при чтении заметки!')
        else:
            print('Ошибка 1')
        print('Заметка не найдена!')

    def read_notes(self):
        if isinstance(self.__repository, repository.Repository):
            return self.__repository.get_all_notes()
        else:
            print('Ошибка 2!')

    def validate_note_data(self, _note):
        if isinstance(_note, note.Note):
            if not _note.get_title() or not _note.get_msg() or not _note.get_date():
                print('Поля заметки пустые')
                return False
            else:
                return True
        else:
            print('Ошибка 3!')
            return False

    def save_note(self, _note):
        if Controller.validate_note_data(self, _note):
            if isinstance(self.__repository, repository.Repository):
                self.__repository.create_note(_note)
                print('Заметка сохранена')
            else:
                print('Ошибка 4!')

    def delete_note(self, note_id):
        if isinstance(self.__repository, repository.Repository):
            self.__repository.delete_note(note_id)
        else:
            print('Ошибка 5!')

    def edit_note(self, _note):
        if Controller.validate_note_data(self, _note):
            if isinstance(self.__repository, repository.Repository):
                self.__repository.edit_note(_note)
            else:
                print('Ошибка 6!')

    def find_notes_by_date(self, date_start, date_end):
        if isinstance(self.__repository, repository.Repository):
            notes = self.__repository.get_all_notes()
            if date_start > date_end:
                tmp = date_start
                date_start = date_end
                date_end = tmp
            find_notes = []
            for _note in notes:
                if isinstance(_note, note.Note):
                    if date_start <= _note.get_date() <= date_end:
                        find_notes.append(_note)
                else:
                    print('Ошибка 7!')
            if not find_notes:
                print('Заметка не найдена!')
            return find_notes
        else:
            print('Ошибка 8!')