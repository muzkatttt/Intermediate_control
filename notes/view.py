from models import Methods


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
        title_note = self.enter_text_to_note(input('Введите заголовок >>> '))
        msg = self.enter_text_to_note(input('Введите заметку >>> '))
        return Methods(title_note=title_note, msg=msg)


    @staticmethod
    def ending(text: str = 'Приложение Notes закрыто'):
        print(text)