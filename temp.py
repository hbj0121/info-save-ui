# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QDialog(object):
    def setupUi(self, QDialog):
        QDialog.setObjectName("QDialog")
        QDialog.resize(500, 700)
        QDialog.setMinimumSize(QtCore.QSize(490, 700))
        QDialog.setMaximumSize(QtCore.QSize(500, 700))
        QDialog.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/temp_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QDialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(QDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 170, 471, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.recent_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.recent_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.recent_label.setObjectName("recent_label")
        self.verticalLayout.addWidget(self.recent_label)
        self.time_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.time_lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.time_lineEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.time_lineEdit.setReadOnly(True)
        self.time_lineEdit.setObjectName("time_lineEdit")
        self.verticalLayout.addWidget(self.time_lineEdit)
        self.tabWidget = QtWidgets.QTabWidget(QDialog)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 270, 471, 421))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 461, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.tab1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.tab1.setContentsMargins(0, 0, 0, 0)
        self.tab1.setObjectName("tab1")
        self.th_table = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.th_table.setObjectName("th_table")
        self.th_table.setColumnCount(3)
        self.th_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.th_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.th_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.th_table.setHorizontalHeaderItem(2, item)
        self.tab1.addWidget(self.th_table, 5, 0, 1, 1)
        self.Q_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Q_lineEdit.setEnabled(True)
        self.Q_lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.Q_lineEdit.setObjectName("Q_lineEdit")
        self.tab1.addWidget(self.Q_lineEdit, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.tab1.addWidget(self.label, 0, 0, 1, 1)
        self.search_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.search_pushButton.setMinimumSize(QtCore.QSize(75, 50))
        self.search_pushButton.setMaximumSize(QtCore.QSize(75, 50))
        self.search_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.search_pushButton.setMouseTracking(False)
        self.search_pushButton.setObjectName("search_pushButton")
        self.tab1.addWidget(self.search_pushButton, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.clear_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clear_pushButton.setMinimumSize(QtCore.QSize(75, 50))
        self.clear_pushButton.setMaximumSize(QtCore.QSize(75, 50))
        self.clear_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.verticalLayout_2.addWidget(self.clear_pushButton)
        self.tab1.addLayout(self.verticalLayout_2, 5, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(QDialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 471, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.baud_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.baud_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.baud_label.setObjectName("baud_label")
        self.gridLayout.addWidget(self.baud_label, 1, 1, 1, 1)
        self.on_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.on_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.on_pushButton.setObjectName("on_pushButton")
        self.gridLayout.addWidget(self.on_pushButton, 3, 0, 1, 1)
        self.off_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.off_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.off_pushButton.setObjectName("off_pushButton")
        self.gridLayout.addWidget(self.off_pushButton, 3, 1, 1, 1)
        self.baud_combobox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.baud_combobox.setMinimumSize(QtCore.QSize(190, 0))
        self.baud_combobox.setMaximumSize(QtCore.QSize(175, 16777215))
        self.baud_combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.baud_combobox.setObjectName("baud_combobox")
        self.baud_combobox.addItem("")
        self.baud_combobox.addItem("")
        self.baud_combobox.addItem("")
        self.baud_combobox.addItem("")
        self.baud_combobox.addItem("")
        self.baud_combobox.addItem("")
        self.baud_combobox.addItem("")
        self.baud_combobox.addItem("")
        self.gridLayout.addWidget(self.baud_combobox, 2, 1, 1, 1)
        self.port_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.port_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.port_label.setObjectName("port_label")
        self.gridLayout.addWidget(self.port_label, 1, 0, 1, 1)
        self.port_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port_lineEdit.sizePolicy().hasHeightForWidth())
        self.port_lineEdit.setSizePolicy(sizePolicy)
        self.port_lineEdit.setMinimumSize(QtCore.QSize(190, 0))
        self.port_lineEdit.setMaximumSize(QtCore.QSize(175, 16777215))
        self.port_lineEdit.setText("")
        self.port_lineEdit.setReadOnly(True)
        self.port_lineEdit.setObjectName("port_lineEdit")
        self.gridLayout.addWidget(self.port_lineEdit, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.check_label = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.check_label.setAlignment(QtCore.Qt.AlignCenter)
        self.check_label.setReadOnly(True)
        self.check_label.setObjectName("check_label")
        self.gridLayout.addWidget(self.check_label, 3, 2, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(QDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 100, 471, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.temp_textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.temp_textEdit.setMaximumSize(QtCore.QSize(100, 50))
        self.temp_textEdit.setReadOnly(True)
        self.temp_textEdit.setObjectName("temp_textEdit")
        self.horizontalLayout_2.addWidget(self.temp_textEdit)
        self.temp_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.temp_lineEdit.setMinimumSize(QtCore.QSize(150, 30))
        self.temp_lineEdit.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.temp_lineEdit.setFont(font)
        self.temp_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_lineEdit.setReadOnly(True)
        self.temp_lineEdit.setObjectName("temp_lineEdit")
        self.horizontalLayout_2.addWidget(self.temp_lineEdit)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.humid_textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.humid_textEdit.setMaximumSize(QtCore.QSize(100, 50))
        self.humid_textEdit.setReadOnly(True)
        self.humid_textEdit.setObjectName("humid_textEdit")
        self.horizontalLayout.addWidget(self.humid_textEdit)
        self.humid_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.humid_lineEdit.setMinimumSize(QtCore.QSize(150, 30))
        self.humid_lineEdit.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.humid_lineEdit.setFont(font)
        self.humid_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.humid_lineEdit.setReadOnly(True)
        self.humid_lineEdit.setObjectName("humid_lineEdit")
        self.horizontalLayout.addWidget(self.humid_lineEdit)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(QDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QDialog)

    def retranslateUi(self, QDialog):
        _translate = QtCore.QCoreApplication.translate
        QDialog.setWindowTitle(_translate("QDialog", "온도 습도 측정 프로그램"))
        self.recent_label.setText(_translate("QDialog", "최근 저장시간:"))
        item = self.th_table.horizontalHeaderItem(0)
        item.setText(_translate("QDialog", "Time"))
        item = self.th_table.horizontalHeaderItem(1)
        item.setText(_translate("QDialog", "Temperature"))
        item = self.th_table.horizontalHeaderItem(2)
        item.setText(_translate("QDialog", "Humid"))
        self.label.setText(_translate("QDialog", "YYYYMMDD 형식으로 써주세요"))
        self.search_pushButton.setText(_translate("QDialog", "검색"))
        self.clear_pushButton.setText(_translate("QDialog", "초기화"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("QDialog", "날짜 검색"))
        self.baud_label.setText(_translate("QDialog", "BAUD"))
        self.on_pushButton.setText(_translate("QDialog", "ON"))
        self.off_pushButton.setText(_translate("QDialog", "OFF"))
        self.baud_combobox.setItemText(0, _translate("QDialog", "4800"))
        self.baud_combobox.setItemText(1, _translate("QDialog", "9600"))
        self.baud_combobox.setItemText(2, _translate("QDialog", "14400"))
        self.baud_combobox.setItemText(3, _translate("QDialog", "19200"))
        self.baud_combobox.setItemText(4, _translate("QDialog", "38400"))
        self.baud_combobox.setItemText(5, _translate("QDialog", "56000"))
        self.baud_combobox.setItemText(6, _translate("QDialog", "57600"))
        self.baud_combobox.setItemText(7, _translate("QDialog", "115200"))
        self.port_label.setText(_translate("QDialog", "PORT"))
        self.label_2.setText(_translate("QDialog", "상태"))
        self.check_label.setText(_translate("QDialog", "OFF"))
        self.temp_textEdit.setHtml(_translate("QDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">온도</span></p></body></html>"))
        self.humid_textEdit.setHtml(_translate("QDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">습도</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QDialog = QtWidgets.QWidget()
    ui = Ui_QDialog()
    ui.setupUi(QDialog)
    QDialog.show()
    sys.exit(app.exec_())
