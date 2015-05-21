from menus import Login


if __name__ == '__main__':

    from backend import Backend

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

    menu = Login()
    menu.go()