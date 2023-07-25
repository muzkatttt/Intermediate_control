import datetime


class View:
    @staticmethod
    def menu():
        print('Выберите действие \nДобавить заметку >>> 1 \n'
                'Редактировать заметку >>> 2 \n'
                'Показать все заметки по дате добавления >>> 3 \n'
                'Показать все заметки по Id >>> 4 \n'
                'Закрыть программу >>> 0 \n >>> ')


    def create(self, note):
        note.append(
            dict(
                title_note=input('Введите заголовок >>> '),
                msg=input('Введите заметку >>> '),
                time=datetime.date.today()
            )
        )
        return note

    @staticmethod
    def ending(text: str = 'Приложение Notes закрыто'):
        print(text)