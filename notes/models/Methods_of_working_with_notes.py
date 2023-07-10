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

