from backend import Backend


class User(object):
    def __init__(self, id, password, balance):
        self.user_id = id
        self.password = password
        self.balance = balance

    @staticmethod
    def get_user(password):
        with Backend() as db:
            cur_obj = db.cur.execute("SELECT * FROM Users WHERE Password=:password", {"password": password})
            try:
                cur_user = cur_obj.next()
                return User(cur_user[0], cur_user[1], cur_user[2])
            except StopIteration:
                return None

    def balance(self):
        return self.balance

    def deposit(self, amount):
        amount = self.balance + amount
        self._change_balance(amount)

    def withdraw(self, amount):
        amount = self.balance - amount  # Allowing overdraft
        self._change_balance(amount)

    def _change_balance(self, amount):
        with Backend() as db:
            db.cur.execute("UPDATE Users SET Balance=? WHERE Id=?", (amount, self.user_id))
            db.con.commit()


if __name__ == '__main__':
    users = (
        ('aaa', 33),
        ('bbb', 44),
        ('ccc', 754745)
    )
    with Backend() as db:
        db.cur.execute('DROP TABLE IF EXISTS Users')
        db.cur.execute('CREATE TABLE IF NOT EXISTS Users(Id INTEGER PRIMARY KEY AUTOINCREMENT, Password TEXT NOT NULL UNIQUE, Balance INT)')
        db.cur.executemany("INSERT INTO Users(Password, Balance) VALUES(?, ?)", users)
        db.con.commit()
    user = User.get_user('aaa')
    user.deposit(300)
