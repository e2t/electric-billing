# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(954, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.edt_new1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.edt_new1.setObjectName("edt_new1")
        self.gridLayout_2.addWidget(self.edt_new1, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.edt_new0 = QtWidgets.QLineEdit(self.groupBox_2)
        self.edt_new0.setText("")
        self.edt_new0.setReadOnly(False)
        self.edt_new0.setObjectName("edt_new0")
        self.gridLayout_2.addWidget(self.edt_new0, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.edt_old1 = QtWidgets.QLineEdit(self.groupBox_5)
        self.edt_old1.setText("")
        self.edt_old1.setObjectName("edt_old1")
        self.gridLayout_5.addWidget(self.edt_old1, 1, 0, 1, 1)
        self.edt_old0 = QtWidgets.QLineEdit(self.groupBox_5)
        self.edt_old0.setText("")
        self.edt_old0.setReadOnly(False)
        self.edt_old0.setObjectName("edt_old0")
        self.gridLayout_5.addWidget(self.edt_old0, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_5)
        self.horizontalLayout_7.addWidget(self.groupBox_5)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.edt_coef0 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edt_coef0.setText("")
        self.edt_coef0.setReadOnly(True)
        self.edt_coef0.setObjectName("edt_coef0")
        self.gridLayout_3.addWidget(self.edt_coef0, 0, 0, 1, 1)
        self.edt_coef1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edt_coef1.setText("")
        self.edt_coef1.setObjectName("edt_coef1")
        self.gridLayout_3.addWidget(self.edt_coef1, 1, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.horizontalLayout_7.addWidget(self.groupBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.edt_price0 = QtWidgets.QLineEdit(self.groupBox)
        self.edt_price0.setText("")
        self.edt_price0.setObjectName("edt_price0")
        self.gridLayout.addWidget(self.edt_price0, 0, 3, 1, 1)
        self.edt_limit0 = QtWidgets.QLineEdit(self.groupBox)
        self.edt_limit0.setText("")
        self.edt_limit0.setReadOnly(True)
        self.edt_limit0.setObjectName("edt_limit0")
        self.gridLayout.addWidget(self.edt_limit0, 0, 1, 1, 1)
        self.edt_limit1 = QtWidgets.QLineEdit(self.groupBox)
        self.edt_limit1.setText("")
        self.edt_limit1.setObjectName("edt_limit1")
        self.gridLayout.addWidget(self.edt_limit1, 1, 1, 1, 1)
        self.edt_limit2 = QtWidgets.QLineEdit(self.groupBox)
        self.edt_limit2.setText("")
        self.edt_limit2.setObjectName("edt_limit2")
        self.gridLayout.addWidget(self.edt_limit2, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.edt_price2 = QtWidgets.QLineEdit(self.groupBox)
        self.edt_price2.setText("")
        self.edt_price2.setObjectName("edt_price2")
        self.gridLayout.addWidget(self.edt_price2, 2, 3, 1, 1)
        self.edt_price1 = QtWidgets.QLineEdit(self.groupBox)
        self.edt_price1.setText("")
        self.edt_price1.setObjectName("edt_price1")
        self.gridLayout.addWidget(self.edt_price1, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 4, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.edt_result = QtWidgets.QLineEdit(self.groupBox_4)
        self.edt_result.setReadOnly(True)
        self.edt_result.setObjectName("edt_result")
        self.horizontalLayout_6.addWidget(self.edt_result)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_run = QtWidgets.QPushButton(Form)
        self.btn_run.setObjectName("btn_run")
        self.gridLayout_4.addWidget(self.btn_run, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 0, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_history = QtWidgets.QTableView(Form)
        self.tbl_history.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_history.setObjectName("tbl_history")
        self.verticalLayout_2.addWidget(self.tbl_history)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setEnabled(False)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_8.addWidget(self.btn_save)
        spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.btn_delete = QtWidgets.QPushButton(Form)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_8.addWidget(self.btn_delete)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.edt_new0, self.edt_new1)
        Form.setTabOrder(self.edt_new1, self.edt_old0)
        Form.setTabOrder(self.edt_old0, self.edt_old1)
        Form.setTabOrder(self.edt_old1, self.edt_coef0)
        Form.setTabOrder(self.edt_coef0, self.edt_coef1)
        Form.setTabOrder(self.edt_coef1, self.edt_limit0)
        Form.setTabOrder(self.edt_limit0, self.edt_limit1)
        Form.setTabOrder(self.edt_limit1, self.edt_limit2)
        Form.setTabOrder(self.edt_limit2, self.edt_price0)
        Form.setTabOrder(self.edt_price0, self.edt_price1)
        Form.setTabOrder(self.edt_price1, self.edt_price2)
        Form.setTabOrder(self.edt_price2, self.edt_result)
        Form.setTabOrder(self.edt_result, self.btn_run)
        Form.setTabOrder(self.btn_run, self.tbl_history)
        Form.setTabOrder(self.tbl_history, self.btn_save)
        Form.setTabOrder(self.btn_save, self.btn_delete)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_2.setTitle(_translate("Form", "Новые показания, кВт"))
        self.edt_new1.setText(_translate("Form", "0"))
        self.label_12.setText(_translate("Form", "Дневные"))
        self.label_7.setText(_translate("Form", "Ночные"))
        self.groupBox_5.setTitle(_translate("Form", "Старые показания, кВт"))
        self.groupBox_3.setTitle(_translate("Form", "Коэффициент"))
        self.groupBox.setTitle(_translate("Form", "Тарифы"))
        self.label_3.setText(_translate("Form", "Свыше"))
        self.label_4.setText(_translate("Form", "кВт по"))
        self.label_8.setText(_translate("Form", "коп. за 1 кВт*час"))
        self.label_6.setText(_translate("Form", "кВт по"))
        self.label_2.setText(_translate("Form", "кВт по"))
        self.label_5.setText(_translate("Form", "Свыше"))
        self.label.setText(_translate("Form", "Свыше"))
        self.label_9.setText(_translate("Form", "коп. за 1 кВт*час"))
        self.label_10.setText(_translate("Form", "коп. за 1 кВт*час"))
        self.groupBox_4.setTitle(_translate("Form", "Сумма к оплате, грн"))
        self.btn_run.setText(_translate("Form", "Выполнить"))
        self.btn_save.setToolTip(_translate("Form", "Сохранить показания в таблицу"))
        self.btn_save.setText(_translate("Form", "Сохранить"))
        self.btn_delete.setToolTip(_translate("Form", "Удалить строку из таблицы"))
        self.btn_delete.setText(_translate("Form", "Удалить"))
