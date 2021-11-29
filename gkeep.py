from logging import currentframe
import gkeepapi
import CREDENTIALS


class GKeepNotes():

    def __init__(self, user_login, user_passwd):
        self.user_login = user_login
        self.user_passwd = user_passwd
        self.keep = gkeepapi.Keep()
        login = self.keep.login(CREDENTIALS.user_login, CREDENTIALS.user_passwd)


    def get_all_notes(self):
        self.notes = dict()
        self.gnotes_list = self.keep.all()
        for note in self.gnotes_list:
            self.notes[note.title] = note.text
        return self.notes

    def get_titles(self):
        self.titles = list()
        self.gnotes_list = self.keep.all()
        for note in self.gnotes_list:
            self.titles.append(note.title)
        return self.titles

    def get_current_note(self, title):
        current_note = dict()
        self.gnote = self.keep.get(str(title))
        current_note[self.gnote.title] = self.gnote.text
        return current_note

    def create_note(self,title,text):
        create_note = self.keep.createNote(title, text)
        self.keep.sync()
