from logging import currentframe
import gkeepapi
import CREDENTIALS


# TODO: добавить исключения и мб возвращать True или False в случае ошибок при выходу из фукнции
class GKeepNotes:

    def __init__(self, user_login: str, user_passwd: str):
        self.user_login = user_login
        self.user_passwd = user_passwd
        self.keep = gkeepapi.Keep()
        self.login = self.keep.login(user_login, user_passwd)
        # login = self.keep.login(CREDENTIALS.user_login, CREDENTIALS.user_passwd)

    def get_all_notes(self) -> dict:
        self.notes = dict()
        self.gnotes_list = self.keep.all()
        for note in self.gnotes_list:
            self.notes[note.title] = note.text
        return self.notes

    def get_titles(self) -> list:
        self.titles = list()
        self.gnotes_list = self.keep.all()
        for note in self.gnotes_list:
            self.titles.append(note.title)
        return self.titles

    def get_current_note(self, title: str) -> dict:
        current_note = dict()
        self.gnote = self.keep.get(str(title))
        current_note[self.gnote.title] = self.gnote.text
        return current_note

    def create_note(self, title: str, text: str):
        create_note = self.keep.createNote(title, text)
        self.keep.sync()
