from notes import file_operation, mapper_csv, note


class Repository:
    def __init__(self, _file_operation):
        self.__mapper = mapper_csv.MapperCsv()
        self.__file_operation = _file_operation

    def get_all_notes(self):
        notes = []
        if isinstance(self.__file_operation, file_operation.FileOperation):
            lines = self.__file_operation.read_all_lines()
            for line in lines:
                notes.append(self.__mapper.map_from_str(line))
        else:
            print('Ошибка 9!')
        return notes

    def get_max_id(self, notes):
        note_id = 0
        for _note in notes:
            if isinstance(_note, note.Note):
                if int(_note.get_id()) > note_id:
                    note_id = int(_note.get_id())
            else:
                print('Ошибка 10!')
        return note_id

    def save_notes(self, notes):
        lines = []
        for _note in notes:
            lines.append(self.__mapper.map_to_str(_note))
        if isinstance(self.__file_operation, file_operation.FileOperation):
            self.__file_operation.save_all_lines(lines)
        else:
            print('Ошибка 11!')

    def save_note(self, _note, notes):
        notes.append(_note)
        Repository.save_notes(self, notes)

    def create_note(self, _note):
        notes = Repository.get_all_notes(self)
        note_id = Repository.get_max_id(self, notes)
        note_id += 1
        if isinstance(_note, note.Note):
            _note.set_id(note_id)
        else:
            print('Ошибка 12!')
        Repository.save_note(self, _note, notes)
        return str(note_id)

    def find_note(self, note_id, notes):
        for _note in notes:
            if isinstance(_note, note.Note):
                if _note.get_id() == note_id:
                    return _note
            else:
                print('Ошибка 13')
        print('Заметка не найдена')

    def delete_note(self, note_id):
        notes = Repository.get_all_notes(self)
        if Repository.find_note(self, note_id, notes) in notes:
            notes.remove(Repository.find_note(self, note_id, notes))
            Repository.save_notes(self, notes)
            print('Заметка удалена')

    def edit_note(self, _note):
        if isinstance(_note, note.Note):
            Repository.delete_note(self, _note.get_id())
        else:
            print('Ошибка 14!')
        notes = Repository.get_all_notes(self)
        Repository.save_note(self, _note, notes)