from PySide6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Signal
from UI.mainUI import Ui_MainWindow
from authWin import Auth
from clickMonitor import WidgetClickMonitor
from TestWidget1 import FlyingBallController
from Timer import ThreadTimer
from graphWidget import SplitGraphWidget
from datetime import datetime
import random
import locale
import time

class window(QMainWindow):
    doGetHistory = Signal()
    ansGetHistory = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.authForm = Auth()
        self._timer = ThreadTimer()
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
        self.testView = FlyingBallController(self.ui.graphicsView)
        self.graph = SplitGraphWidget(self.ui.widget_17)
        self.speedReact:list[float] = []
        self.mistakes:int = 0
        self.time:int = 10
        self.plotData:list = [[0],[0]]
        self.p_time:int
        r = random.randint(0,100)
        random.seed(hash(str(r)))
        if not self.ui.widget_17.layout():
            layout = QVBoxLayout(self.ui.widget_17)
            layout.setContentsMargins(0, 0, 0, 0)
        else:
            layout = self.ui.widget_17.layout()
        
        # Очищаем layout и добавляем график
        self.clear_layout(layout)
        layout.addWidget(self.graph)
        
        # Устанавливаем данные
        # self.update_graph_data()


        try:
    # Попробуем установить русскую локаль
            print("Устанавливаю")
            locale.setlocale(locale.LC_TIME, 'ru_RU')  # для Linux/Mac
            print("Установил")
        except Exception:
            pass
        self.connectSignals()


    def clear_layout(self, layout):
        """Очищает layout от всех виджетов"""
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

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
        self.testView.ball_clicked.connect(self.ball_clicked)
        self.testView.background_clicked.connect(self.back_clicked)

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

    def ball_clicked(self):
        n = time.time()
        self.speedReact.append(n-self.p_time)
        self.testView.ball_item.setPos(random.randint(0,self.geometry().width()-100),random.randint(0,self.geometry().height()-180))
        self.p_time = time.time()

    def back_clicked(self):
        self.mistakes += 1

    def tickClock(self):
        if self.time > 0:
            self.time -= 1
            if self.time >= 10:
                self.ui.label_42.setText(f"00:{self.time}")
            else:
                self.ui.label_42.setText(f"00:0{self.time}")
            self._timer.start(1,self.tickClock)
        else:
            self.showResults()
        # print(self.time)

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
        self.speedReact:list[float] = []
        self.mistakes:int = 0
        print(self.shoosedTest)
        if self.time >= 10:
            self.ui.label_42.setText(f"00:{self.time}")
        else:
            self.ui.label_42.setText(f"00:0{self.time}")
        if self.shoosedTest == 1:
            self.startSecondTest()

    def startFirstTest(self):
        pass

    def startSecondTest(self):
        self.ui.label_40.setText("Duck shoot")
        self.ui.stackedWidget.setCurrentIndex(3)
        self.testView.set_Size([0,0,self.geometry().width()-70,self.geometry().height()-160])
        self.p_time = time.time()
        self._timer.start(1,self.tickClock)

    def startThirdTest(self):
        pass

    def showResults(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        if self.shoosedTest == 1:
            self.ui.label_60.setText('Вы прошли тест:"Duck shoot"')
        self.ui.label_62.setText(str(len(self.speedReact)))
        if len(self.speedReact) == 0:
            self.speedReact.append(10)
        self.ui.label_64.setText(str(sum(self.speedReact)/len(self.speedReact)))
        print(self.speedReact, sum(self.speedReact),len(self.speedReact), sum(self.speedReact)/len(self.speedReact))
        self.ui.label_64.setText(str(self.mistakes))
        s = sum(self.speedReact)
        self.plotData[0].append(s/len(self.speedReact))
        self.plotData[1].append(self.mistakes)
        self.graph.set_titles("Прогресс скорости", "Прогресс точности")
        data1 = [list(range(len(self.plotData[0]))),self.plotData[0]]
        data2 = [list(range(len(self.plotData[1]))),self.plotData[1]]
        
        self.graph.set_data(data1, data2)

