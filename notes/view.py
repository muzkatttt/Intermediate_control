
class View:
    @staticmethod
    def menu():
        print('Выберите действие \nДобавить заметку >>> 1 \n'
                'Редактировать заметку >>> 2 \n'
                'Удалить заметку >>> 3 \n'
                'Показать все заметки по дате добавления >>> 4 \n'
                'Показать все заметки по Id >>> 5 \n'
                'Закрыть программу >>> 0 \n >>> ')


    def create(self):
        title_note = input('Введите заголовок >>> ')
        msg = input('Введите заметку >>> ')
        return title_note, msg


    @staticmethod
    def ending(text: str = 'Приложение Notes закрыто'):
        print(text)