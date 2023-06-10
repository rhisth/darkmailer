import os
import sys
import codecs
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from PyQt6 import QtCore, QtGui, QtWidgets
import interface

ready = 0
input = []

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

    def loadmails(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        if file[0]:
            self.mailsEdit.clear()
            f = codecs.open(file[0], "r", "utf-8")
            text = f.read()
            self.mailsEdit.append(text)
            f.close()

    def savemails(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", ".", "Text Files (*.txt);;All Files (*)")
        print(file)
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
            self.textEdit.append(text)
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
                except:
                    self.logsBrowser.append(f"Ошибка при подключении к {smtp}:{port}")
                try:
                    server.sendmail(input[2], mail, message.as_string())
                    self.logsBrowser.append(f"Отправлено на адрес {mail}")
                except:
                    self.logsBrowser.append(f"Ошибка при отправлении на адрес {mail}")
                server.quit()

    def login(self):
        global ready
        global input
        smtp = self.smtpEdit.text()
        port = self.portEdit.text()
        mail = self.mailEdit.text()
        password = self.passwordEdit.text()
        if smtp and port and mail and password:
            try:
                server = smtplib.SMTP(smtp, int(port))
                self.logsBrowser.append(f"Подключено к {smtp}:{port}")
                server.starttls()
            except:
                self.logsBrowser.append(f"Ошибка при подключении к {smtp}:{port}")
                return
            try:
                server.login(mail, password)
                self.logsBrowser.append(f"Выполнен вход в почту {mail}")
            except:
                self.logsBrowser.append(f"Ошибка при попытке входа в почту {mail}")
                return
            server.quit()
            ready = 1
            input = [smtp, port, mail, password]

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
