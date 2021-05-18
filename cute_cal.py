from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('cute_cal.ico'))
        MainWindow.setFixedSize(382, 408)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(42, 47, 48);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.screen = QtWidgets.QLabel(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(6, 10, 369, 40))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.screen.setFont(font)
        self.screen.setStyleSheet("background-color: rgb(191, 169, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(162, 138, 181);")
        self.screen.setObjectName("screen")
        self.number_0 = QtWidgets.QPushButton(self.centralwidget)
        self.number_0.setGeometry(QtCore.QRect(6, 335, 136, 70))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.number_0.setFont(font)
        self.number_0.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.number_0.setObjectName("number_0")
        self.number_ravno = QtWidgets.QPushButton(self.centralwidget)
        self.number_ravno.setGeometry(QtCore.QRect(148, 335, 136, 70))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.number_ravno.setFont(font)
        self.number_ravno.setStyleSheet("QPushButton{background-image: url(cat_ravno.png); background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(1, 186, 255);}")
        self.number_ravno.setObjectName("number_ravno")
        self.number_1 = QtWidgets.QPushButton(self.centralwidget)
        self.number_1.setGeometry(QtCore.QRect(6, 241, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.number_1.setFont(font)
        self.number_1.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.number_1.setObjectName("number_1")
        self.number_2 = QtWidgets.QPushButton(self.centralwidget)
        self.number_2.setGeometry(QtCore.QRect(100, 241, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.number_2.setFont(font)
        self.number_2.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.number_2.setObjectName("number_2")
        self.number_3 = QtWidgets.QPushButton(self.centralwidget)
        self.number_3.setGeometry(QtCore.QRect(194, 241, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.number_3.setFont(font)
        self.number_3.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.number_3.setObjectName("number_3")
        self.number_4 = QtWidgets.QPushButton(self.centralwidget)
        self.number_4.setGeometry(QtCore.QRect(6, 147, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.number_4.setFont(font)
        self.number_4.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.number_4.setObjectName("number_4")
        self.number_5 = QtWidgets.QPushButton(self.centralwidget)
        self.number_5.setGeometry(QtCore.QRect(100, 147, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.number_5.setFont(font)
        self.number_5.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.number_5.setObjectName("number_5")
        self.number_6 = QtWidgets.QPushButton(self.centralwidget)
        self.number_6.setGeometry(QtCore.QRect(194, 147, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.number_6.setFont(font)
        self.number_6.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.number_6.setObjectName("number_6")
        self.number_7 = QtWidgets.QPushButton(self.centralwidget)
        self.number_7.setGeometry(QtCore.QRect(6, 54, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.number_7.setFont(font)
        self.number_7.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.number_7.setObjectName("number_7")
        self.number_8 = QtWidgets.QPushButton(self.centralwidget)
        self.number_8.setGeometry(QtCore.QRect(100, 54, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.number_8.setFont(font)
        self.number_8.setStyleSheet("QPushButton{background-image: url(cute_cat_2.png);background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.number_8.setObjectName("number_8")
        self.number_9 = QtWidgets.QPushButton(self.centralwidget)
        self.number_9.setGeometry(QtCore.QRect(194, 54, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.number_9.setFont(font)
        self.number_9.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.number_9.setObjectName("number_9")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(288, 54, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.plus.setFont(font)
        self.plus.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(288, 147, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.minus.setFont(font)
        self.minus.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.minus.setObjectName("minus")
        self.umnojit = QtWidgets.QPushButton(self.centralwidget)
        self.umnojit.setGeometry(QtCore.QRect(288, 241, 88, 88))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.umnojit.setFont(font)
        self.umnojit.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 4px solid rgb(120, 186, 255);}")
        self.umnojit.setObjectName("umnojit")
        self.delit = QtWidgets.QPushButton(self.centralwidget)
        self.delit.setGeometry(QtCore.QRect(288, 335, 88, 70))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.delit.setFont(font)
        self.delit.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 2px solid rgb(165, 186, 255);}")
        self.delit.setObjectName("delit")

        self.delite = QtWidgets.QPushButton(self.centralwidget)
        self.delite.setGeometry(QtCore.QRect(340, 15, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(14)
        self.delite.setFont(font)
        self.delite.setStyleSheet("QPushButton{background-color: rgb(165, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px;} QPushButton:pressed{background-color: rgb(140, 186, 255);\n"
"color: rgb(255, 255, 255); border-radius: 6px; border: 2px solid rgb(165, 186, 255);}")
        self.delite.setObjectName("delite")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtWidgets.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))


        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Милый калькулятор - darrso"))
        self.screen.setText(_translate("MainWindow", "0"))
        self.number_0.setText(_translate("MainWindow", "0"))
        self.number_ravno.setText(_translate("MainWindow", "="))
        self.number_1.setText(_translate("MainWindow", "1"))
        self.number_2.setText(_translate("MainWindow", "2"))
        self.number_3.setText(_translate("MainWindow", "3"))
        self.number_4.setText(_translate("MainWindow", "4"))
        self.number_5.setText(_translate("MainWindow", "5"))
        self.number_6.setText(_translate("MainWindow", "6"))
        self.number_7.setText(_translate("MainWindow", "7"))
        self.number_8.setText(_translate("MainWindow", "8"))
        self.number_9.setText(_translate("MainWindow", "9"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.umnojit.setText(_translate("MainWindow", "*"))
        self.delit.setText(_translate("MainWindow", "/"))
        self.delite.setText(_translate("MainWindow", "X"))


    


#с этого момента мы дописываем все без программы
    def add_functions(self):
        self.number_0.clicked.connect(lambda: self.write_number(self.number_0.text()))
        self.number_1.clicked.connect(lambda: self.write_number(self.number_1.text()))
        self.number_2.clicked.connect(lambda: self.write_number(self.number_2.text()))
        self.number_3.clicked.connect(lambda: self.write_number(self.number_3.text()))
        self.number_4.clicked.connect(lambda: self.write_number(self.number_4.text()))
        self.number_5.clicked.connect(lambda: self.write_number(self.number_5.text()))
        self.number_6.clicked.connect(lambda: self.write_number(self.number_6.text()))
        self.number_7.clicked.connect(lambda: self.write_number(self.number_7.text()))
        self.number_8.clicked.connect(lambda: self.write_number(self.number_8.text()))
        self.number_9.clicked.connect(lambda: self.write_number(self.number_9.text()))
        self.plus.clicked.connect(lambda: self.write_number(self.plus.text()))
        self.minus.clicked.connect(lambda: self.write_number(self.minus.text()))
        self.umnojit.clicked.connect(lambda: self.write_number(self.umnojit.text()))
        self.delit.clicked.connect(lambda: self.write_number(self.delit.text()))
        self.number_ravno.clicked.connect(self.results)
        self.delite.clicked.connect(self.delite_function)

    def write_number(self, number):
        if (self.screen.text()[-1] in '*+-/' and number in '*+-/') or (self.screen.text() == '0' and number in '*/') or (number == '=' and self.screen.text()[-1] == '='):
                self.screen.setText('Error')
        elif (self.screen.text() == '0' and number not in '*/') or self.screen.text() == 'Error':
                self.screen.setText(number)
        elif self.screen.text()[0] == '=':
                self.screen.setText(number)
        else:
                self.screen.setText(self.screen.text() + number)

    def results(self):
            res = eval(self.screen.text())
            self.screen.setText('=' + str(res))

    def delite_function(self):
            self.screen.setText('0')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
