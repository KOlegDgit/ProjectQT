import sqlite3


class SqLite:
    def __init__(self):
        self.con = sqlite3.connect('data/DB/CarNum.db')

    def add_elem(self, windows, textEdit_fio, textEdit_password):
        cur = self.con.cursor()
        for i in cur.execute("select Login from LogIn").fetchall():
            if textEdit_fio == i[0]:
                windows.statusBar().showMessage('Такой login уже существует')
                return False

        if textEdit_fio != '':
            textEdit_fio = "'" + textEdit_fio + "'"
        if textEdit_password != '':
            textEdit_password = "'" + textEdit_password + "'"

        try:
            cur.execute(f"INSERT INTO LogIn VALUES (NULL, {textEdit_fio}, {textEdit_password})")
        except:
            windows.statusBar().showMessage("Необходимо заполнить все поля")
            return False
        else:
            self.con.commit()
            return True
