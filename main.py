from menus import Login
from user import User

if __name__ == '__main__':

    from backend import Backend

    # Create test users
    users = [
        ['aaa', 0],
        ['bbb', 0],
        ['ccc', 0]
    ]

    for user in users:
        user[0] = User.password_hash(user[0])

    with Backend() as db:
        db.cur.execute('DROP TABLE IF EXISTS Users')
        db.cur.execute('CREATE TABLE IF NOT EXISTS Users(Id INTEGER PRIMARY KEY AUTOINCREMENT, Password TEXT NOT NULL UNIQUE, Balance INT)')
        db.cur.executemany("INSERT INTO Users(Password, Balance) VALUES(?, ?)", users)
        db.con.commit()

    menu = Login()
    menu.go()