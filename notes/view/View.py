from notes.models.Methods import Notes


class View:
    @staticmethod
    def menu():
        print('Выберите действие (add_note - 1 \n '
                'save_notes - 2 \n'
                'read_notes - 3 \n'
                'edit_note - 4 \n'
                'delete_note - 5: >>> \n')

    def create_note(self, number):
        title_note = self.enter_text_to_note(input('Title >>> '), number)
        msg = self.enter_text_to_note(input('Enter message >>> '), number)
        return Notes(title_note=title_note, msg=msg)


    @staticmethod
    def enter_text_to_note(text):
        while len(text) <= 10:
            print('Введите заметку')
            text = input('Введите текст >>>\n')

    def ending(self):
        print('Приложение Notes закрыто')