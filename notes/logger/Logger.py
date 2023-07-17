
class Logger:
    log_result = ''

    def __init__(self, log):
        self.choice = None
        self.log = log

    def ask_from_user(self, string):
        self.choice = input(string)
        if self.choice == 'y':
            self.save_to_file('note.json')

    def save_to_file(self, fileName):
        append = open(fileName, 'a')
        reader = open(fileName, 'r')
        append.write(self.log + '\n')
        append.close()
        return reader.readline()

    def history(self):
        reader = open('log.txt', 'r')
        log_result = reader.read()
        reader.close()
        return log_result