from notes.models.Abstract_methods import Abstract_methods

class Methods_of_working_with_notes(Abstract_methods):
    __note: str

    def __init__(self, note: str):
        super().__init__()
        self.note = note

    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    def create_note(self):
        #return f = open('note.txt', 'w')
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