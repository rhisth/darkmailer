import os
import sys
import codecs
import smtplib
from datetime import datetime, date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from PyQt6 import QtCore, QtGui, QtWidgets
import interface

ready = 0
input = []

if not os.path.exists("logs"):
    os.mkdir("logs")

class MailThread(QtCore.QThread):
    def __init__(self, window, parent=None):
        super().__init__()
        self.window = window

    def run(self):
        self.window.sendButton.setEnabled(False)
        self.window.pushButton.setEnabled(False)
        list = self.window.mailsEdit.toPlainText().splitlines()
        text = self.window.textEdit.toPlainText()
        subject = self.window.themeEdit.text()
        for mail in list:
            try:
                server = smtplib.SMTP(input[0], input[1])
                server.starttls()
                server.login(input[2], input[3])
                message = MIMEMultipart()
                message["Subject"] = subject
                message["From"] = input[2]
                message["To"] = mail
                message.attach(MIMEText(text, "html"))
            except Exception as ex:
                self.window.logsBrowser.append(f"Ошибка при подключении к {smtp}:{port}")
                with open(f"logs/{date.today()}.txt", "a") as f:
                    f.write(f"{datetime.now()} - {ex}\n")
                self.window.sendButton.setEnabled(False)
                self.window.pushButton.setEnabled(False)
                return
            try:
                server.sendmail(input[2], mail, message.as_string())
                self.window.logsBrowser.append(f"Отправлено на адрес {mail}")
            except Exception as ex:
                self.window.logsBrowser.append(f"Ошибка при отправлении на адрес {mail}")
                with open(f"logs/{date.today()}.txt", "a") as f:
                    f.write(f"{datetime.now()} - {ex}\n")
            server.quit()
        self.window.sendButton.setEnabled(True)
        self.window.pushButton.setEnabled(True)


class LoginThread(QtCore.QThread):
        def __init__(self, window, parent=None):
            super().__init__()
            self.window = window

        def run(self):
            self.window.pushButton.setEnabled(False)
            global ready
            global input
            smtp = self.window.smtpEdit.text()
            port = self.window.portEdit.text()
            mail = self.window.mailEdit.text()
            password = self.window.passwordEdit.text()
            try:
                server = smtplib.SMTP(smtp, int(port))
                self.window.logsBrowser.append(f"Подключено к {smtp}:{port}")
                server.starttls()
            except Exception as ex:
                self.window.logsBrowser.append(f"Ошибка при подключении к {smtp}:{port}")
                with open(f"logs/{date.today()}.txt", "a") as f:
                    f.write(f"{datetime.now()} - {ex}\n")
                self.window.pushButton.setEnabled(True)
                return
            try:
                server.login(mail, password)
                self.window.logsBrowser.append(f"Выполнен вход в почту {mail}")
            except Exception as ex:
                self.window.logsBrowser.append(f"Ошибка при попытке входа в почту {mail}")
                with open(f"logs/{date.today()}.txt", "a") as f:
                    f.write(f"{datetime.now()} - {ex}\n")
                self.window.pushButton.setEnabled(True)
                return
            server.quit()
            ready = 1
            input = [smtp, port, mail, password]
            self.window.pushButton.setEnabled(True)

class App(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mailsLoadButton.clicked.connect(self.loadmails)
        self.mailsSaveButton.clicked.connect(self.savemails)
        self.textLoadButton.clicked.connect(self.loadtext)
        self.textSaveButton.clicked.connect(self.savetext)
        self.sendButton.clicked.connect(self.sendmails)
        self.pushButton.clicked.connect(self.login)
        self.mailingthread = MailThread(window=self)
        self.loginingthread = LoginThread(window=self)

    def loadmails(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        if file[0]:
            self.mailsEdit.clear()
            f = codecs.open(file[0], "r", "utf-8")
            text = f.read()
            self.mailsEdit.appendPlainText(text)
            f.close()

    def savemails(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", ".", "Text Files (*.txt);;All Files (*)")
        if file[0]:
            f = codecs.open(file[0], "w", "utf-8")
            f.write(self.mailsEdit.toPlainText())
            f.close()

    def loadtext(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        if file[0]:
            self.textEdit.clear()
            f = codecs.open(file[0], "r", "utf-8")
            text = f.read()
            self.textEdit.appendPlainText(text)
            f.close()

    def savetext(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", ".", "Text Files (*.txt);;All Files (*)")
        if file[0]:
            f = codecs.open(file[0], "w", "utf-8")
            f.write(self.textEdit.toPlainText())
            f.close()

    def sendmails(self):
        if ready == 0:
            self.logsBrowser.append(f"Не выполнен вход в почту для отправки писем")
            return
        list = self.mailsEdit.toPlainText().splitlines()
        text = self.textEdit.toPlainText()
        subject = self.themeEdit.text()
        if list and text:
            self.mailingthread.start()

    def login(self):
        smtp = self.smtpEdit.text()
        port = self.portEdit.text()
        mail = self.mailEdit.text()
        password = self.passwordEdit.text()
        if smtp and port and mail and password:
            self.loginingthread.start()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
