import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QComboBox, QPushButton)
from PyQt5.QtGui import QPixmap, QFont


class CBR_API(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def days(self):
        """
        Выпадающий список дней.
        """

        # Создаем выпадающий список.
        self.days_combo = QComboBox(self)

        # Заголовок списка.
        day_label = QLabel("День", self)
        day_label.move(20, 170)

        for day in range(1, 31):
            # Наполняем список.
            self.days_combo.addItem('%d' % day)

        # Фиксируем список.
        self.days_combo.move(20, 200)

    def month(self):
        """
        Выпадающий список месяцев.
        """

        # Создаем выпадающий список.
        self.month_combo = QComboBox(self)

        # Заголовок списка.
        month_label = QLabel("Месяц", self)
        month_label.move(80, 170)

        for month_num in range(1, 13):
            # Наполняем список.
            self.month_combo.addItem('%d' % month_num)

        # Фиксируем список.
        self.month_combo.move(80, 200)

    def year(self):
        """
        Выпадающий список годов.
        """

        # Создаем выпадающий список.
        self.year_combo = QComboBox(self)

        # Заголовок списка.
        month_label = QLabel("Год", self)
        month_label.move(140, 170)

        for year_num in range(2005, 2020):
            # Наполняем список.
            self.year_combo.addItem('%d' % year_num)

        # Фиксируем список.
        self.year_combo.move(140, 200)

    def initUI(self):
        # Загружаем лого нашей программы.
        logo_label = QLabel(self)
        logo_label.setPixmap(QPixmap("img/logo.png"))
        logo_label.move(0, 0)

        # Загружаем выпадающие списки для дней, месяцев и годов.
        self.days()
        self.month()
        self.year()

        # Создаем кнопку "OK".
        ok_button = QPushButton('ОК', self)
        ok_button.resize(50, 25)
        ok_button.move(220, 200)

        # Каждый клик кнопки вызывает метод "makeRequest"
        ok_button.clicked.connect(self.makeRequest)

        self.setFixedSize(300, 400)
        self.setWindowTitle('История курса рубля')
        self.show()

    def makeRequest(self):
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    money = CBR_API()
    sys.exit(app.exec_())