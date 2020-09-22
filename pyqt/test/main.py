import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QComboBox, QPushButton)
from PyQt5.QtGui import QPixmap, QFont
import requests
import xml.etree.cElementTree as ET

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

        for year_num in range(2005, 2018):
            # Наполняем список.
            self.year_combo.addItem('%d' % year_num)

        # Фиксируем список.
        self.year_combo.move(140, 200)

    def load_result_image(self):
        # Настройки фонта текста.
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(18)

        # Загружаем иконку доллара.
        dollar_label = QLabel(self)
        dollar_label.setPixmap(QPixmap("img/dollar.png"))
        dollar_label.move(60, 260)

        # Текст с выводом курса доллара.
        self.dollar_value = QLabel("0 руб.", self)
        self.dollar_value.setFont(font)
        self.dollar_value.move(130, 263)

        # Загружаем иконку евро.
        euro_label = QLabel(self)
        euro_label.setPixmap(QPixmap("img/euro.png"))
        euro_label.move(50, 320)

        # Текст с выводом курса евро.
        self.euro_value = QLabel("0 руб.", self)
        self.euro_value.setFont(font)
        self.euro_value.move(130, 320)

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

        # Загружаем иконки валют и текст с курсом.
        self.load_result_image()

        self.setFixedSize(300, 400)
        self.setWindowTitle('История курса рубля')
        self.show()

    def getResult(self, day, month, year):
        """
        Выполняет запрос к API Банка России.

        :param day: Выбранный день.
        :param month: Выбранный номер месяца.
        :param year: Выбранный код
        :return: dict
        """

        result = {
            'usd': 0,
            'eur': 0,
        }

        if int(day) < 10:
            day = '0%s' % day

        if int(month) < 10:
            month = '0%s' % month

        try:
            # Выполняем запрос к API.
            get_xml = requests.get(
                'http://www.cbr.ru/scripts/XML_daily.asp?date_req=%s/%s/%s' % (day, month, year)
            )

            # Парсинг XML используя ElementTree
            structure = ET.fromstring(get_xml.content)
        except:
            return result

        try:
            # Поиск курса доллара (USD ID: R01235)
            dollar = structure.find("./*[@ID='R01235']/Value")
            result['dollar'] = dollar.text.replace(',', '.')
        except:
            result['dollar'] = 'x'

        try:
            # Поиск курса евро (EUR ID: R01239)
            euro = structure.find("./*[@ID='R01239']/Value")
            result['euro'] = euro.text.replace(',', '.')
        except:
            result['euro'] = 'x'

        return result

    def makeRequest(self):
        """
        После нажатия на "ОК" выполняется запрос к API с выбранными данными.
        """
        # Получаем текущие значения из выпадающих списках.
        day_value = self.days_combo.currentText()
        month_value = self.month_combo.currentText()
        year_value = self.year_combo.currentText()

        # Выполняем запрос к API с выбранными данными.
        result = self.getResult(day_value, month_value, year_value)

        # Заменяем текст для доллара.
        self.dollar_value.setText('%s руб.' % result['dollar'])
        self.dollar_value.adjustSize()

        # Заменяем текст для евро.
        self.euro_value.setText('%s руб.' % result['euro'])
        self.euro_value.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    money = CBR_API()
    sys.exit(app.exec_())