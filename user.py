from backend import Backend


class User(object):
    def __init__(self, user_id, password, balance):
        self.user_id = user_id
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

    def get_balance(self):
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
        self.balance = amount

