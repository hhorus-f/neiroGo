from PySide6.QtWidgets import QMainWindow, QLabel, QWidget
from PySide6.QtCore import Signal
from UI.mainUI import Ui_MainWindow
from authWin import Auth
from clickMonitor import WidgetClickMonitor
from TestWidget1 import BallSceneManager
from datetime import datetime
import locale

class window(QMainWindow):
    doGetHistory = Signal()
    ansGetHistory = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.authForm = Auth()
        self.data:dict|None = None
        self.name:str
        self.streak = 0
        self.bestTime = 0
        self.rmsTime = 0
        self.mesto = "?"
        self.dayStreak = 0
        self.progress = [0,0,0,0,0,0,0]
        self.progressLabels = [self.ui.label_33,self.ui.label_34,self.ui.label_35,self.ui.label_36,self.ui.label_37,self.ui.label_38,self.ui.label_39]
        self.lastResult = []
        self.shoosedTest:int
        self.testWidgets = [self.ui.widget_9,self.ui.widget_10,self.ui.widget_11]
        self.w1 = WidgetClickMonitor(self.ui.widget_9)
        self.w2 = WidgetClickMonitor(self.ui.widget_10)
        self.w3 = WidgetClickMonitor(self.ui.widget_11)
        self.testView = BallSceneManager(self.ui.graphicsView)
        try:
    # Попробуем установить русскую локаль
            print("Устанавливаю")
            locale.setlocale(locale.LC_TIME, 'ru_RU')  # для Linux/Mac
            print("Установил")
        except Exception:
            pass
        self.connectSignals()
    
    def connectSignals(self):
        self.ui.pushButton_2.clicked.connect(lambda e:self.showAuth(0))
        self.ui.pushButton_4.clicked.connect(lambda e:self.showAuth(1))
        self.authForm.Succ.connect(self.showHome)
        self.ansGetHistory.connect(self.parseHistory)
        self.ui.pushButton_8.clicked.connect(self.showChooseTest)
        self.ui.pushButton_12.clicked.connect(lambda e:self.showHome(self.name))
        self.w1.clicked.connect(self.chooseTest)
        self.w2.clicked.connect(self.chooseTest)
        self.w3.clicked.connect(self.chooseTest)
        self.ui.pushButton_5.clicked.connect(self.startTests)

    def showAuth(self,ind:int):
        self.authForm.switchModes(ind)
        self.authForm.exec()

    def parseHistory(self,data:dict):
        print("data",data)
        self.data = data
        if data != {}:
            pass
        else:
            pass


    def showHome(self,name:str):
        self.name = name
        self.doGetHistory.emit()
        while self.data is None:
            pass
        self.ui.label_13.setText(self.name)
        self.ui.label_16.setText(f"Добро пожаловать {self.name}")
        self.ui.label_12.setText(str(self.streak))
        self.ui.label_20.setText(str(self.bestTime)+'мс')
        self.ui.label_23.setText(str(self.rmsTime)+'мс')
        self.ui.label_29.setText(str(self.mesto))
        self.ui.label_26.setText(str(self.dayStreak))
        for day in range(len(self.progress)):
            self.progressLabels[day].setText(str(self.progress[day]))
        k = 0
        if len(self.lastResult) > 8:
            k = len(self.lastResult) - 8
        for indres in range(min(8,len(self.lastResult))):
            res = self.lastResult[indres+k]
            c1 = self.ui.verticalLayout_20.count()
            self.ui.verticalLayout_20.insertWidget(c1-1,QLabel(res["text1"]))
            c2 = self.ui.verticalLayout_22.count()
            self.ui.verticalLayout_22.insertWidget(c2-1,QLabel(res["text2"]))
            c3 = self.ui.verticalLayout_21.count()
            self.ui.verticalLayout_21.insertWidget(c3-1,QLabel(res["text3"]))
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d %B %Y")
        self.ui.label_17.setText(formatted_date)
        self.ui.stackedWidget.setCurrentIndex(1)

    def chooseTest(self,obj:QWidget,obj2:object):
        obj.setStyleSheet(f"#{str(obj.objectName())}"+'{border:2px solid red;border-radius:25px;};')
        tests = list(self.testWidgets)
        tests.remove(obj)
        for test in tests:
            test.setStyleSheet(f"#{str(test.objectName())}"+'{border:2px solid #005cb3;border-radius:25px;};')
        if obj in self.testWidgets:
            self.shoosedTest = self.testWidgets.index(obj)
        print(f"self.shoosedTest = {self.shoosedTest}")

    def showChooseTest(self):
        self.ui.label_47.setText(self.name)
        self.ui.widget_9.setStyleSheet(f"#{str(self.ui.widget_9.objectName())}"+'{border:2px solid #005cb3;border-radius:25px;};')
        self.ui.widget_10.setStyleSheet(f"#{str(self.ui.widget_10.objectName())}"+'{border:2px solid #005cb3;border-radius:25px;};')
        self.ui.widget_11.setStyleSheet(f"#{str(self.ui.widget_11.objectName())}"+'{border:2px solid #005cb3;border-radius:25px;};')
        self.ui.stackedWidget.setCurrentIndex(2)

    def startTests(self):
        print(self.shoosedTest)
        if self.shoosedTest == 1:
            self.startSecondTest()

    def startFirstTest(self):
        pass

    def startSecondTest(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.testView.create_ball(radius=30, speed=5)
        self.testView.start_animation()