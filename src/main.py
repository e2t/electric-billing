#!/usr/bin/env python3
import sys
from datetime import datetime
from typing import Dict
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QKeyEvent
sys.path.append('..')
import gui
import saving
import billing
from manifest import VERSION, DESCRIPTION
from dry.qt import stop_in_lineedit, BaseMainWindow, msgbox, get_float_number
from dry.core import InputException


WRN_OLD_MORE_NEW = 'Старое показание больше нового'
FORMAT_DATE = '%d-%m-%Y'


def get_positive_number_or_zero(lineedit: QtWidgets.QLineEdit) -> float:
    return get_float_number(lineedit, (0, True), None)


class MainWindow(BaseMainWindow, gui.Ui_Form):
    def __init__(self) -> None:
        BaseMainWindow.__init__(self, DESCRIPTION, VERSION)

    def init_widgets(self) -> None:
        self.restore_history()
        self.restore_data()

    def get_last_readings(self) -> None:
        self.edt_old0.setText(self.tbl_history.model().item(0, 0).text())
        self.edt_old1.setText(self.tbl_history.model().item(0, 1).text())

    def get_last_readings_or_zero(self) -> None:
        if self.tbl_history.model().rowCount():
            self.get_last_readings()
        else:
            self.edt_old0.setText('0')
            self.edt_old1.setText('0')

    def restore_data(self) -> None:
        data = saving.restore_data()
        self.get_last_readings_or_zero()
        self.edt_coef0.setText(data['coef0'])
        self.edt_coef1.setText(data['coef1'])
        self.edt_limit0.setText(data['limit0'])
        self.edt_limit1.setText(data['limit1'])
        self.edt_limit2.setText(data['limit2'])
        self.edt_price0.setText(data['price0'])
        self.edt_price1.setText(data['price1'])
        self.edt_price2.setText(data['price2'])

    def save_data(self) -> None:
        data = {}
        data['coef0'] = self.edt_coef0.text()
        data['coef1'] = self.edt_coef1.text()
        data['limit0'] = self.edt_limit0.text()
        data['limit1'] = self.edt_limit1.text()
        data['limit2'] = self.edt_limit2.text()
        data['price0'] = self.edt_price0.text()
        data['price1'] = self.edt_price1.text()
        data['price2'] = self.edt_price2.text()
        saving.save_data(data)

    def restore_history(self) -> None:
        history = saving.restore_history()
        self.tbl_history.setModel(QStandardItemModel())

        self.tbl_history.model().setHorizontalHeaderLabels(
            ['Показания (Д)', 'Показания (Н)', 'Сумма'])

        if history:
            for row in sorted([int(i) for i in history]):
                self.insert_to_history(row, history[str(row)])
        else:
            self.insert_newline(0, datetime.now())

        self.tbl_history.resizeColumnsToContents()
        self.tbl_history.setFixedWidth(
            self.tbl_history.horizontalHeader().length() +
            self.tbl_history.verticalHeader().sizeHint().width() + 2)

        if not history:
            self.tbl_history.model().removeRow(0)

    def save_history(self) -> None:
        history: Dict[str, saving.HistoryLine] = {}
        for row in range(self.tbl_history.model().rowCount()):
            history[str(row)] = {
                'date': datetime.strptime(
                    self.tbl_history.model().verticalHeaderItem(0).text(),
                    FORMAT_DATE),
                'new0': self.tbl_history.model().item(row, 0).text(),
                'new1': self.tbl_history.model().item(row, 1).text(),
                'payment': self.tbl_history.model().item(row, 2).text()}
        saving.save_history(history)

    def insert_current_to_history(self) -> None:
        self.insert_to_history(0, {
            'date': datetime.now(), 'new0': self.edt_new0.text(),
            'new1': self.edt_new1.text(), 'payment': self.edt_result.text()})
        self.get_last_readings()
        self.edt_new0.setText('')
        self.edt_new1.setText('0')
        self.btn_save.setEnabled(False)
        self.edt_new0.setFocus()

    def insert_newline(self, row: int, date: datetime) -> None:
        self.tbl_history.model().insertRow(row)
        self.tbl_history.model().setVerticalHeaderItem(row, QStandardItem(
            date.strftime(FORMAT_DATE)))
        self.tbl_history.resizeRowToContents(row)

    def insert_to_history(
            self, row: int, history_line: saving.HistoryLine) -> None:
        date = history_line['date']
        assert isinstance(date, datetime), 'date is not datetime'
        self.insert_newline(row, date)

        self.tbl_history.model().setItem(
            row, 0, QStandardItem(history_line['new0']))
        self.tbl_history.model().setItem(
            row, 1, QStandardItem(history_line['new1']))
        self.tbl_history.model().setItem(
            row, 2, QStandardItem(history_line['payment']))

    def remove_selected_lines(self) -> None:
        for i in self.tbl_history.selectionModel().selectedRows():
            self.tbl_history.model().removeRow(i.row())
        self.get_last_readings_or_zero()

    def connect_actions(self) -> None:
        self.btn_run.clicked.connect(self.run)
        self.btn_save.clicked.connect(self.insert_current_to_history)
        self.btn_delete.clicked.connect(self.remove_selected_lines)

    def run(self) -> None:
        try:
            new0 = get_positive_number_or_zero(self.edt_new0)
            new1 = get_positive_number_or_zero(self.edt_new1)
            old0 = get_positive_number_or_zero(self.edt_old0)
            if old0 > new0:
                stop_in_lineedit(self.edt_old0, WRN_OLD_MORE_NEW)
            old1 = get_positive_number_or_zero(self.edt_old1)
            if old1 > new1:
                stop_in_lineedit(self.edt_old1, WRN_OLD_MORE_NEW)
            kws = (new0 - old0, new1 - old1)
            if not sum(kws):
                stop_in_lineedit(self.edt_new0, 'Показания не изменились')
            factors = (get_positive_number_or_zero(self.edt_coef0),
                       get_positive_number_or_zero(self.edt_coef1))
            limits = (get_positive_number_or_zero(self.edt_limit0),
                      get_positive_number_or_zero(self.edt_limit1),
                      get_positive_number_or_zero(self.edt_limit2))
            if len(limits) != len(set(limits)):
                stop_in_lineedit(self.edt_limit1,
                                 'Одинаковые границы интервалов')
            prices = {limits[0]: get_positive_number_or_zero(self.edt_price0),
                      limits[1]: get_positive_number_or_zero(self.edt_price1),
                      limits[2]: get_positive_number_or_zero(self.edt_price2)}
            self.edt_result.setText(
                '{0:.2f}'.format(billing.cost(kws, factors, prices)))
            self.btn_save.setEnabled(True)
        except InputException as excp:
            self.btn_save.setEnabled(False)
            msgbox(str(excp))

    def keyPressEvent(  # pylint: disable = C0103
            self, key_event: QKeyEvent) -> None:
        if key_event.key() == Qt.Key_Escape:
            self.closeEvent(None)
        QtWidgets.QDialog.keyPressEvent(self, key_event)

    def closeEvent(self, _event: QKeyEvent) -> None:  # pylint: disable = C0103
        self.save_data()
        self.save_history()


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
