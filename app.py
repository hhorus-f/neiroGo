from PySide6.QtWidgets import QApplication
from window import window
from dB import SimpleUserDB
from dataWorker import dataWorker

class App:
    def __init__(self):
        self.app = QApplication()
        self.win = window()
        self.db = SimpleUserDB()
        self.dataW = dataWorker(self.db)
        self.connectSignal()

    def connectSignal(self):
        self.win.authForm.doCreateAccount.connect(self.dataW.doCreateAccount)
        self.dataW.createAccountStatus.connect(self.win.authForm.createAccountStatus)
        self.win.authForm.doSignIn.connect(self.dataW.doSignIn)
        self.dataW.SignInStatus.connect(self.win.authForm.SignInStatus)
        self.win.doGetHistory.connect(self.dataW.doGetHistory)
        self.dataW.ansGetHistory.connect(self.win.ansGetHistory)
        self.win.doSaveHistory.connect(self.dataW.doSaveHistory)

    def exec(self):
        self.win.show()
        self.app.exec()


if __name__ == "__main__":
    app = App()
    app.exec()