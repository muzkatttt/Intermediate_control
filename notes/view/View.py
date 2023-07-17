class View:
    @staticmethod
    def input_from_user() -> str:
        note = input('Выберите действие (create_note - 1 \n '
                     'save_notes - 2 \n'
                     'read_notes - 3 \n'
                     'edit_note - 4 \n'
                     'delete_note - 5: >>> \n')
        return note

    @staticmethod
    def print_result(note):
        print(note)
