from datetime import datetime
from notes import controller, note


class View:
    def __init__(self, _controller):
        self.__controller = _controller

    def run(self):
        while True:
            command = str(input('Введите команду (введите команду "help", чтобы посмотреть все команды)\n>>> '))
            if command.lower() == 'exit':
                return

            if command.lower() == 'create':
                title = str(input('Введите заголовок заметки\n>>> '))
                msg = str(input('Введите текст заметки\n>>> '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.save_note(
                        note.Note('0', title, msg, str(datetime.now().strftime("%Y.%m.%d %H:%M:%S"))))
                else:
                    print('Ошибка 15!')

            elif command.lower() == 'read':
                note_id = str(input('Введите ID\n>>> '))
                if isinstance(self.__controller, controller.Controller):
                    _note = self.__controller.read_note(note_id)
                    print(f'ID: {_note.get_id()}')
                    print(f'Title: {_note.get_title()}')
                    print(f'Message: {_note.get_msg()}')
                    print(f'Date modified: {_note.get_date()}')
                else:
                    print('Ошибка 16!')

            elif command.lower() == 'list':
                if isinstance(self.__controller, controller.Controller):
                    notes = self.__controller.read_notes()
                    notes.sort()
                    for _note in notes:
                        print(_note)
                else:
                    print('Ошибка 17')

            elif command.lower() == 'find':
                while True:
                    date_start = input('Введите следующий формат даты "YYYY.MM.DD HH:MM:SS"\n>>> ')
                    try:
                        datetime.strptime(date_start, '%Y.%m.%d %H:%M:%S')
                        break
                    except:
                        print('Некорректный ввод даты, попробуйте еще раз\n>>> ')
                while True:
                    date_end = input('Введите следующий формат даты "YYYY.MM.DD HH:MM:SS"\n>>> ')
                    try:
                        datetime.strptime(date_end, '%Y.%m.%d %H:%M:%S')
                        break
                    except:
                        print('Некорректный ввод даты, попробуйте еще раз')
                if isinstance(self.__controller, controller.Controller):
                    notes = self.__controller.find_notes_by_date(date_start, date_end)
                    notes.sort()
                    for _note in notes:
                        print(_note)
                else:
                    print('Ошибка 16')

            elif command.lower() == 'delete':
                note_id = str(input('Введите ID\n>>> '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.delete_note(note_id)
                else:
                    print('Ошибка 17')

            elif command.lower() == 'edit':
                note_id = str(input('Введите ID\n>>> '))
                title = str(input('Введите заголовок заметки\n>>> '))
                msg = str(input('Введите текст заметки\n>>> '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.edit_note(
                        note.Note(note_id, title, msg, str(datetime.now().strftime("%Y.%m.%d %H:%M:%S"))))

            elif command.lower() == 'help':
                print('Список команд:')
                print('list - показать все заметки по дате последних изменений')
                print('read - показать все заметки по ID')
                print('find - найти заметку по дате')
                print('create - создать новую заметку')
                print('edit - изменить заметку по ID')
                print('delete - удалить заметку по ID')
                print('exit - выйти из программы')
            else:
                print('Команда не найдена!')