from PySide6.QtCore import QThread, Signal
from dB import SimpleUserDB
import bcrypt

class dataWorker(QThread):
    doCreateAccount = Signal(dict)
    createAccountStatus = Signal(bool)
    doSignIn = Signal(dict)
    SignInStatus = Signal(bool)
    doGetHistory = Signal()
    ansGetHistory = Signal(dict)
    doSaveHistory = Signal(dict)
    def __init__(self, db, parent = None):
        super().__init__(parent)
        self.db:SimpleUserDB = db
        self.isRun:bool = False
        self.uid:int
        self.connectSignals()

    def connectSignals(self):
        self.doCreateAccount.connect(self.createAccount)
        self.doSignIn.connect(self.signInAccount)
        self.doGetHistory.connect(self.getHistory)
        self.doSaveHistory.connect(self.saveHistory)

    def createAccount(self,data:dict):
        name = data["name"]
        password = data["password"]
        password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
        answer = self.db.get_uid_by_username(name)
        if answer is not None and answer != "":
            print(answer)
            self.createAccountStatus.emit(False)
            print(f"нет :{answer}")
        else:
            self.uid = self.db.create_user(name,password)
            self.createAccountStatus.emit(True)
            print("да")

    def signInAccount(self,data:dict):
        name = data["name"]
        password = data["password"]
        answer = self.db.get_uid_by_username(name)
        corr_p = self.db.get_password(answer)
        print("password equals",password, corr_p)
        is_valid = bcrypt.checkpw(password.encode('utf-8'), corr_p)
        if is_valid:
            self.uid = answer
            self.SignInStatus.emit(True)
        else:
            self.SignInStatus.emit(False)
    
    def getHistory(self):
        print("get")
        history = self.db.get_history(self.uid)
        print("history")
        self.ansGetHistory.emit(history)

    def saveHistory(self,data:dict):
        hist = self.db.get_history(self.uid)
        id = len(hist)
        hist[id] = data
        print(hist)
        self.db.set_history(self.uid,hist)

    def run(self):
        self.isRun = True
        while self.isRun:
            pass
    
    def stop(self):
        self.isRun = False

    