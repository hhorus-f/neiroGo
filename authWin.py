from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from UI.authForm import Ui_Dialog


class Auth(QDialog):
    doCreateAccount = Signal(dict)
    createAccountStatus = Signal(bool)
    doSignIn = Signal(dict)
    SignInStatus = Signal(bool)


    Succ = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connectSignal()

    def connectSignal(self):
        self.ui.pushButton_4.clicked.connect(lambda e:self.switchModes(0))
        self.ui.pushButton.clicked.connect(lambda e:self.switchModes(1))
        self.ui.pushButton_2.clicked.connect(lambda e:self.createAccount())
        self.createAccountStatus.connect(self.createAccount)
        self.ui.pushButton_3.clicked.connect(lambda e:self.signInAccount())
        self.SignInStatus.connect(self.signInAccount)          

    def switchModes(self,ind:int):
        self.ui.stackedWidget.setCurrentIndex(ind)
        self.ui.label_2.setText("Создайте аккаунт для отслеживания прогресса")
        self.ui.label_10.setText("Войдите в аккаунт для отслеживания прогресса")
        self.ui.label_2.setStyleSheet("color:black")
        self.ui.label_10.setStyleSheet("color:black")
    
    def createAccount(self,data:bool | None = None):
        name = self.ui.lineEdit.text()
        password = self.ui.lineEdit_3.text()
        agree = self.ui.checkBox.isChecked()
        if data is None:
            if name != "" and password != "" and agree:
                print("попытка")
                self.doCreateAccount.emit({"name":name,"password":password})
        else:
            if data:
                self.Succ.emit(name)
                self.close()
                print("удача")
            else:
                print("нет")
                self.ui.label_2.setText("Это имя занято")
                self.ui.label_2.setStyleSheet("color:red")

    def signInAccount(self, data: bool | None = None):
        name = self.ui.lineEdit_5.text()
        password = self.ui.lineEdit_6.text()
        if data is None:
            if name != "" and password != "":
                print("попытка")
                self.doSignIn.emit({"name":name,"password":password})
        else:
            if data:
                print("удача")
                self.Succ.emit(name)
                self.close()
                
            else:
                print("нет")
                self.ui.label_10.setText("Неверное имя пользователя или пароль")
                self.ui.label_10.setStyleSheet("color:red")