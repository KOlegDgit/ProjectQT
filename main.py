import sys
from PyQt5.Qt import QPalette, QColor, Qt
from PyQt5.QtGui import QIcon
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from detect import Detect


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainForm.ui', self)  # Загружаем дизайн
        self.radioButton_img.setChecked(True)
        self.setWindowIcon(QIcon('data\ok.png'))
        self.pushButton_img.clicked.connect(self.run)

    def run(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.img_label.setPixmap(QPixmap(fname))
        detect_img = Detect(fname)
        detect_img.get_image()
        self.label_number.setPixmap(QPixmap('frame.jpg'))



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

    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())










