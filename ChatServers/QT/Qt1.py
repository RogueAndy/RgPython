import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)

# class MyWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#
# app = QtWidgets.QApplication(sys.argv)
# windows = MyWindow()
# label = QtWidgets.QLabel(windows)
# label.setText('新世界')
# windows.show()
# sys.exit(app.exec_())

class Exmaple(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('测试而已')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Exmaple()
    sys.exit(app.exec_())




# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         lcd = QLCDNumber(self)
#         sld = QSlider(Qt.Horizontal, self)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)
#
#         self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Signal & slot')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())