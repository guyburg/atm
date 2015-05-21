import sqlite3
import settings


class Backend(object):
    def __init__(self):
        self.con = sqlite3.connect(settings.USERS_DB)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()
