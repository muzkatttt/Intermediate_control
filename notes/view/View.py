import notes.models.Methods


class View:
    @staticmethod
    def menu():
        print('Выберите действие \nДобавить заметку >>> 1 \n'
                'Редактировать заметку >>> 2 \n'
                'Удалить заметку >>> 3 \n'
                'Показать все заметки по дате добавления >>> 4 \n'
                'Показать все заметки по Id >>> 5 \n'
                'Закрыть программу >>> 0 \n >>> ')


    def create_note(self):
        title_note = self.enter_text_to_note(input('Title >>> '))
        msg = self.enter_text_to_note(input('Enter message >>> '))
        return notes.Methods(title_note=title_note, msg=msg)


    @staticmethod
    def enter_text_to_note(text):
        while len(text) <= 10:
            print('Введите заметку')
            text = input('Введите текст >>>\n')

    def ending(self):
        print('Приложение Notes закрыто')