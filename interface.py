from PyQt6 import QtCore, QtGui, QtWidgets
from res_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(25, 30, 39);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 43, 56);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(46, 55, 72);\n"
"padding: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 73, 94);\n"
"}\n"
"QTextEdit {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 36, 47);\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(46, 55, 72);\n"
"}\n"
"QTextBrowser {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 36, 47);\n"
"border-radius: 7px;\n"
"border: 2px solid rgb(46, 55, 72);\n"
"}\n"
"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 36, 47);\n"
"border-radius: 7px;\n"
"border: 2px solid rgb(46, 55, 72);\n"
"}\n"
"QScrollBar{\n"
"border: none;\n"
"width: 14px;\n"
"}\n"
"QScrollBar:handle{\n"
"background-color: rgb(46, 55, 72);\n"
"min-height: 30px;\n"
"border-radius: 7px;\n"
"margin: 15px 0 15px 0;\n"
"}\n"
"QScrollBar:handle:hover{\n"
"background-color: rgb(60, 73, 94);\n"
"}\n"
"QScrollBar:add-page, QScrollBar:sub-page{\n"
"background: none;\n"
"}\n"
"QScrollBar:add-line, QScrollBar:sub-line{\n"
"border: none;\n"
"background:  none;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.text4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text4.setObjectName("text4")
        self.gridLayout_2.addWidget(self.text4, 4, 2, 1, 2)
        self.themeEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.themeEdit.setObjectName("themeEdit")
        self.gridLayout_2.addWidget(self.themeEdit, 5, 2, 1, 2)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 11, 0, 1, 2)
        self.sendButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sendButton.setStyleSheet("")
        self.sendButton.setObjectName("sendButton")
        self.gridLayout_2.addWidget(self.sendButton, 11, 2, 1, 2)
        self.text2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text2.setStyleSheet("color: rgb(255, 255, 255);")
        self.text2.setObjectName("text2")
        self.gridLayout_2.addWidget(self.text2, 0, 2, 1, 2)
        self.mailsEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.mailsEdit.setStyleSheet("")
        self.mailsEdit.setObjectName("mailsEdit")
        self.gridLayout_2.addWidget(self.mailsEdit, 1, 0, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 1, 2, 1, 2)
        self.logsBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.logsBrowser.setStyleSheet("")
        self.logsBrowser.setObjectName("logsBrowser")
        self.gridLayout_2.addWidget(self.logsBrowser, 9, 2, 1, 2)
        self.text3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text3.setStyleSheet("color: rgb(255, 255, 255);")
        self.text3.setObjectName("text3")
        self.gridLayout_2.addWidget(self.text3, 8, 2, 1, 2)
        self.text1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.text1.setStyleSheet("color: rgb(255, 255, 255);")
        self.text1.setObjectName("text1")
        self.gridLayout_2.addWidget(self.text1, 0, 0, 1, 2)
        self.mailsSaveButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mailsSaveButton.setStyleSheet("")
        self.mailsSaveButton.setObjectName("mailsSaveButton")
        self.gridLayout_2.addWidget(self.mailsSaveButton, 2, 0, 1, 1)
        self.mailsLoadButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mailsLoadButton.setStyleSheet("")
        self.mailsLoadButton.setObjectName("mailsLoadButton")
        self.gridLayout_2.addWidget(self.mailsLoadButton, 2, 1, 1, 1)
        self.textSaveButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.textSaveButton.setStyleSheet("")
        self.textSaveButton.setObjectName("textSaveButton")
        self.gridLayout_2.addWidget(self.textSaveButton, 2, 2, 1, 1)
        self.textLoadButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.textLoadButton.setStyleSheet("")
        self.textLoadButton.setObjectName("textLoadButton")
        self.gridLayout_2.addWidget(self.textLoadButton, 2, 3, 1, 1)
        self.loginWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.loginWidget.setObjectName("loginWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.loginWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget3 = QtWidgets.QWidget(parent=self.loginWidget)
        self.widget3.setObjectName("widget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text8 = QtWidgets.QLabel(parent=self.widget3)
        self.text8.setObjectName("text8")
        self.verticalLayout_3.addWidget(self.text8)
        self.passwordEdit = QtWidgets.QLineEdit(parent=self.widget3)
        self.passwordEdit.setObjectName("passwordEdit")
        self.verticalLayout_3.addWidget(self.passwordEdit)
        self.gridLayout.addWidget(self.widget3, 3, 1, 1, 1)
        self.widget = QtWidgets.QWidget(parent=self.loginWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text7 = QtWidgets.QLabel(parent=self.widget)
        self.text7.setObjectName("text7")
        self.verticalLayout.addWidget(self.text7)
        self.mailEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.mailEdit.setObjectName("mailEdit")
        self.verticalLayout.addWidget(self.mailEdit)
        self.gridLayout.addWidget(self.widget, 3, 0, 1, 1)
        self.widget4 = QtWidgets.QWidget(parent=self.loginWidget)
        self.widget4.setObjectName("widget4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(parent=self.widget4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.smtpEdit = QtWidgets.QLineEdit(parent=self.widget4)
        self.smtpEdit.setObjectName("smtpEdit")
        self.verticalLayout_4.addWidget(self.smtpEdit)
        self.gridLayout.addWidget(self.widget4, 2, 0, 1, 1)
        self.widget2 = QtWidgets.QWidget(parent=self.loginWidget)
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text6 = QtWidgets.QLabel(parent=self.widget2)
        self.text6.setObjectName("text6")
        self.verticalLayout_2.addWidget(self.text6)
        self.portEdit = QtWidgets.QLineEdit(parent=self.widget2)
        self.portEdit.setObjectName("portEdit")
        self.verticalLayout_2.addWidget(self.portEdit)
        self.gridLayout.addWidget(self.widget2, 2, 1, 1, 1)
        self.logoText = QtWidgets.QLabel(parent=self.loginWidget)
        self.logoText.setStyleSheet("color: rgb(0, 0, 0);")
        self.logoText.setObjectName("logoText")
        self.gridLayout.addWidget(self.logoText, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.loginWidget, 5, 0, 5, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DarkMailer"))
        self.text4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Тема письма</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Войти в почту"))
        self.sendButton.setText(_translate("MainWindow", "Разослать письма"))
        self.text2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Текст</p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Логи</p></body></html>"))
        self.text1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Почты</p></body></html>"))
        self.mailsSaveButton.setText(_translate("MainWindow", "Сохранить файл"))
        self.mailsLoadButton.setText(_translate("MainWindow", "Загрузить файл"))
        self.textSaveButton.setText(_translate("MainWindow", "Сохранить файл"))
        self.textLoadButton.setText(_translate("MainWindow", "Загрузить файл"))
        self.text8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Пароль</p></body></html>"))
        self.text7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Почта</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">SMTP сервер</p></body></html>"))
        self.text6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Порт</p></body></html>"))
        self.logoText.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">DarkMailer</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
