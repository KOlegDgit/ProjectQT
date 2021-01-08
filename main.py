import sys
from PyQt5.Qt import QPalette, QColor, Qt
from PyQt5.QtGui import QIcon
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from detect import Detect
from veb_capture import Detect_cam
from sqLite import SqLite


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/Ui/login.ui', self)  # Загружаем дизайн
        self.setWindowIcon(QIcon('data/img/ok.png'))
        self.pushButton_in.clicked.connect(self.enter)
        self.pushButton_reg.clicked.connect(self.registration)

    def enter(self):
        new_pass = self.textEdit_fio.toPlainText()

        # hashed_password = hash_password(new_pass)
        # print('Строка для хранения в базе данных: ' + hashed_password)
        # old_pass = input('Введите пароль еще раз для проверки: ')
        #
        # if check_password(hashed_password, old_pass):
        #     print('Вы ввели правильный пароль')
        # else:
        #     print('Извините, но пароли не совпадают')
        if new_pass == '1':
            self.main_form = MainForm()
            self.main_form.show()
            self.close()

    def registration(self):
        self.registration = Registration()
        self.registration.show()
        self.close()


class Registration(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/Ui/Registration.ui', self)  # Загружаем дизайн
        self.setWindowIcon(QIcon('data/img/ok.png'))
        self.pushButton_regetr.clicked.connect(self.registration)

    def registration(self):
        db = SqLite()
        if db.add_elem(self, self.textEdit_fio.toPlainText(), self.textEdit_password.toPlainText()):
            self.login = Login()
            self.login.show()
            self.close()


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/Ui/MainForm.ui', self)  # Загружаем дизайн
        self.setWindowIcon(QIcon('data/img/ok.png'))
        self.pushButton_img.clicked.connect(self.download_img)
        self.pushButton_cam.clicked.connect(self.download_cam)
        self.pushButton_detect_img.clicked.connect(self.detect_img)

        self.label.setPixmap(QPixmap('data/img/Car1.jpg'))
        self.label_2.setPixmap(QPixmap('data/img/Car2.png'))
        self.label_3.setPixmap(QPixmap('data/img/Car3.jpg'))
        self.label_4.setPixmap(QPixmap('data/img/Car4.jpg'))

    def download_img(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.img_label.setPixmap(QPixmap(self.fname))

    def detect_img(self):
        detect_img = Detect(self.fname)
        detect_img.get_image(self.label_number_img)

    def download_cam(self):
        detect_cam = Detect_cam()
        detect_cam.detect(self.cam_label)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    # тёмная тема
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    login = Login()
    login.show()

    sys.exit(app.exec_())
