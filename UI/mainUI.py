# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ГлавнаяyfDrTj.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1763, 1044)
        MainWindow.setStyleSheet(u"background-color:white;\n"
"color:black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(3)
        self.stackedWidget.setMidLineWidth(3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 19, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(self.page)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 2))
        self.progressBar.setMaximumSize(QSize(16777215, 4))
        self.progressBar.setStyleSheet(u"*::chunk {\n"
"                background-color: #005cb3;   \n"
"                border-radius: 5px;                                     \n"
"            }")
        self.progressBar.setValue(100)
        self.progressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"color:#333333;\n"
"font-size: 32px;\n"
"font-weight:800;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:#333333;\n"
"font-size: 16px;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_4.addWidget(self.label_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border: 2px solid #cee7ff;\n"
"border-radius:15px;")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(40, -1, -1, -1)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_6.setStyleSheet(u"*{color:#333333;\n"
"font-size: 15px;\n"
"border-color: transparent;}\n"
"*::hover{\n"
"background-color:#cee7ff;\n"
"}")

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"*{\n"
"color:#333333;\n"
"font-size: 15px;\n"
"border-color: transparent;\n"
"}\n"
"\n"
"*::hover{\n"
"background-color:#cee7ff;\n"
"}")

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"*{\n"
"color:#333333;\n"
"font-size: 15px;\n"
"border-color: transparent;\n"
"}\n"
"\n"
"*::hover{\n"
"background-color:#cee7ff;\n"
"}")

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"*{\n"
"color:#333333;\n"
"font-size: 15px;\n"
"border-color: transparent;\n"
"}\n"
"\n"
"*::hover{\n"
"background-color:#cee7ff;\n"
"}")

        self.verticalLayout_5.addWidget(self.label_5)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"*{color:white;\n"
"font-size: 18px;\n"
"font-weight: bold;	\n"
"background-color:#005cb3;\n"
"border:1px solid transparent;\n"
"border-radius:25px;\n"
"}\n"
"*::hover{\n"
"background-color:#003b73;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"*{\n"
"color:#005cb3;\n"
"background-color:#ffffff;\n"
"border:2px solid #005cb3;\n"
"font-size: 18px;\n"
"font-weight: bold;	\n"
"}\n"
"*::hover{\n"
"color:white;\n"
"background-color:#003b73;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setStyleSheet(u"color:#666666;\n"
"font-size: 13px;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.pushButton_9 = QPushButton(self.page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"color:#005cb3;\n"
"text-decoration: underline #005cb3;\n"
"font-size: 13px;\n"
"border:none;")

        self.horizontalLayout_3.addWidget(self.pushButton_9)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setStyleSheet(u"color:#999999;\n"
"font-size: 11px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setStyleSheet(u"color:#005cb3;\n"
"font-size: 32px;\n"
"font-weight:800;")

        self.verticalLayout_6.addWidget(self.label_11)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.line_3 = QFrame(self.page_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color:blue;")
        self.line_3.setLineWidth(3)
        self.line_3.setMidLineWidth(3)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.horizontalWidget = QWidget(self.page_2)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_13 = QLabel(self.horizontalWidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setStyleSheet(u"font-size: 16px;\n"
"font-weight: 600;")

        self.verticalLayout_8.addWidget(self.label_13)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_14 = QLabel(self.horizontalWidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setStyleSheet(u"color:#666666;\n"
"font-size: 13px;")

        self.horizontalLayout_6.addWidget(self.label_14)

        self.label_15 = QLabel(self.horizontalWidget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setStyleSheet(u"color:#666666;\n"
"font-size: 13px;")

        self.horizontalLayout_6.addWidget(self.label_15)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)


        self.verticalLayout_6.addWidget(self.horizontalWidget)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pushButton_6 = QPushButton(self.page_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy4)
        self.pushButton_6.setMinimumSize(QSize(0, 50))
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"*{text-align: left;\n"
"                padding: 0 20px;\n"
"                border-radius: 10px;\n"
"                font-size: 15px;\n"
"                font-weight: 500;\n"
"background-color:#cee7ff;\n"
"}\n"
"*::hover{\n"
"background-color: #005cb3;\n"
"color: white;\n"
"}")

        self.verticalLayout_19.addWidget(self.pushButton_6)

        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"*{text-align: left;\n"
"                padding: 0 20px;\n"
"                border-radius: 10px;\n"
"                font-size: 15px;\n"
"                font-weight: 500;\n"
"background-color:#cee7ff;\n"
"}\n"
"*::hover{\n"
"background-color: #005cb3;\n"
"color: white;\n"
"}")

        self.verticalLayout_19.addWidget(self.pushButton_3)

        self.pushButton_7 = QPushButton(self.page_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy4.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy4)
        self.pushButton_7.setMinimumSize(QSize(0, 50))
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"*{text-align: left;\n"
"                padding: 0 20px;\n"
"                border-radius: 10px;\n"
"                font-size: 15px;\n"
"                font-weight: 500;\n"
"background-color:#cee7ff;\n"
"}\n"
"*::hover{\n"
"background-color: #005cb3;\n"
"color: white;\n"
"}")

        self.verticalLayout_19.addWidget(self.pushButton_7)


        self.verticalLayout_16.addLayout(self.verticalLayout_19)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_16)

        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setStyleSheet(u"*{text-align: center;\n"
"background-color:white;\n"
"color:red;\n"
"                padding: 0 20px;\n"
"                border-radius: 10px;\n"
"                font-size: 15px;\n"
"                font-weight: 500;\n"
"border:2px solid red;}\n"
"*::hover{\n"
"background-color:red;\n"
"color:white;\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.line = QFrame(self.page_2)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color:blue;")
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(3)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.verticalWidget_2 = QWidget(self.page_2)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy5)
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_16 = QLabel(self.verticalWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font-size: 24px;\n"
"font-weight: 600;\n"
"color:#2c3e50;")

        self.horizontalLayout_7.addWidget(self.label_16)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_17 = QLabel(self.verticalWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font-size:16px;\n"
"\n"
"color:Gray;")

        self.horizontalLayout_7.addWidget(self.label_17)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_4 = QWidget(self.verticalWidget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"#widget_4{border:2px solid #cee7ff;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.widget_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setStyleSheet(u"font-size:18px;\n"
"color:Gray;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_10)

        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_12)


        self.horizontalLayout_8.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.verticalWidget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"#widget_3{border:2px solid #cee7ff;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.widget_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_19 = QLabel(self.widget_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font-size:18px;\n"
"color:Gray;")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_19)

        self.label_20 = QLabel(self.widget_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_20)


        self.horizontalLayout_8.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.verticalWidget_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"#widget_2{border:2px solid #cee7ff;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.widget_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_22 = QLabel(self.widget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font-size:18px;\n"
"color:Gray;")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_22)

        self.label_23 = QLabel(self.widget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_23)


        self.horizontalLayout_8.addWidget(self.widget_2)

        self.widget_6 = QWidget(self.verticalWidget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"#widget_6{border:2px solid #cee7ff;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.widget_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_28 = QLabel(self.widget_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font-size:18px;\n"
"color:Gray;")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_28)

        self.label_29 = QLabel(self.widget_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_29)


        self.horizontalLayout_8.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.verticalWidget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"#widget_5{border:2px solid #cee7ff;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_25 = QLabel(self.widget_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font-size:18px;\n"
"color:Gray;")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_25)

        self.label_26 = QLabel(self.widget_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_26)


        self.horizontalLayout_8.addWidget(self.widget_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.pushButton_8 = QPushButton(self.verticalWidget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 90))
        self.pushButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"*{background-color: #005cb3;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 20px;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"letter-spacing: 2px;\n"
"margin: 10px 0;\n"
"text-align:left;\n"
"}\n"
"*::hover{\n"
"background-color:#003b73;\n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_8 = QWidget(self.verticalWidget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"#widget_8{border:2px solid #cee7ff;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.widget_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_43 = QLabel(self.widget_8)
        self.label_43.setObjectName(u"label_43")
        sizePolicy3.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy3)
        self.label_43.setStyleSheet(u"font-size:32px;\n"
"color:#2c3e50;")

        self.verticalLayout_14.addWidget(self.label_43)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_18 = QLabel(self.widget_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;\n"
"color:#2c3e50;\n"
"padding-left:20px;")

        self.verticalLayout_18.addWidget(self.label_18)

        self.label_21 = QLabel(self.widget_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;\n"
"color:#2c3e50;\n"
"padding-left:20px;")

        self.verticalLayout_18.addWidget(self.label_21)

        self.label_24 = QLabel(self.widget_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;\n"
"color:#2c3e50;\n"
"padding-left:20px;")

        self.verticalLayout_18.addWidget(self.label_24)

        self.label_27 = QLabel(self.widget_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;\n"
"color:#2c3e50;\n"
"padding-left:20px;")

        self.verticalLayout_18.addWidget(self.label_27)

        self.label_30 = QLabel(self.widget_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;\n"
"color:#2c3e50;\n"
"padding-left:20px;")

        self.verticalLayout_18.addWidget(self.label_30)

        self.label_31 = QLabel(self.widget_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;\n"
"color:#2c3e50;\n"
"padding-left:20px;")

        self.verticalLayout_18.addWidget(self.label_31)

        self.label_32 = QLabel(self.widget_8)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;\n"
"color:#2c3e50;\n"
"padding-left:20px;")

        self.verticalLayout_18.addWidget(self.label_32)


        self.horizontalLayout_10.addLayout(self.verticalLayout_18)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_33 = QLabel(self.widget_8)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font-size:24px;\n"
"padding-right:20px;")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.label_33)

        self.label_34 = QLabel(self.widget_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font-size:24px;\n"
"padding-right:20px;")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.label_34)

        self.label_35 = QLabel(self.widget_8)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font-size:24px;\n"
"padding-right:20px;")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.label_35)

        self.label_36 = QLabel(self.widget_8)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"font-size:24px;\n"
"padding-right:20px;")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.label_36)

        self.label_37 = QLabel(self.widget_8)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font-size:24px;\n"
"padding-right:20px;")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.label_37)

        self.label_38 = QLabel(self.widget_8)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font-size:24px;\n"
"padding-right:20px;")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.label_38)

        self.label_39 = QLabel(self.widget_8)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"font-size:24px;\n"
"padding-right:20px;")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_17.addWidget(self.label_39)


        self.horizontalLayout_10.addLayout(self.verticalLayout_17)


        self.verticalLayout_14.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_9.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.verticalWidget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"#widget_7{border:2px solid #cee7ff;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.widget_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_44 = QLabel(self.widget_7)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font-size:32px;\n"
"color:#2c3e50;")

        self.verticalLayout_15.addWidget(self.label_44)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_5)


        self.horizontalLayout_11.addLayout(self.verticalLayout_20)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_6)


        self.horizontalLayout_11.addLayout(self.verticalLayout_22)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_7)


        self.horizontalLayout_11.addLayout(self.verticalLayout_21)


        self.verticalLayout_15.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_9.addWidget(self.widget_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_4.addWidget(self.verticalWidget_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_12 = QHBoxLayout(self.page_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_46 = QLabel(self.page_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"color:#005cb3;\n"
"font-size: 32px;\n"
"font-weight:800;")

        self.verticalLayout_23.addWidget(self.label_46)

        self.line_4 = QFrame(self.page_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color:blue;")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_23.addWidget(self.line_4)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_47 = QLabel(self.page_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font-size: 16px;\n"
"font-weight: 600;")

        self.verticalLayout_25.addWidget(self.label_47)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_56 = QLabel(self.page_3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"color:#666666;\n"
"font-size: 13px;")

        self.horizontalLayout_18.addWidget(self.label_56)

        self.label_48 = QLabel(self.page_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"color:#666666;\n"
"font-size: 13px;")

        self.horizontalLayout_18.addWidget(self.label_48)


        self.verticalLayout_25.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_15.addLayout(self.verticalLayout_25)


        self.verticalLayout_23.addLayout(self.horizontalLayout_15)

        self.pushButton_12 = QPushButton(self.page_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 50))
        self.pushButton_12.setStyleSheet(u"*{text-align: left;\n"
"                padding: 0 20px;\n"
"                border-radius: 10px;\n"
"                font-size: 15px;\n"
"                font-weight: 500;\n"
"background-color:#cee7ff;\n"
"}\n"
"*::hover{\n"
"background-color: #005cb3;\n"
"color: white;\n"
"}")

        self.verticalLayout_23.addWidget(self.pushButton_12)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_8)


        self.horizontalLayout_12.addLayout(self.verticalLayout_23)

        self.line_2 = QFrame(self.page_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color:blue;")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_2)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_45 = QLabel(self.page_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font-size: 24px;\n"
"font-weight: 600;\n"
"color:#2c3e50;")

        self.horizontalLayout_13.addWidget(self.label_45)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)


        self.verticalLayout_24.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_24.addItem(self.verticalSpacer_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_9 = QWidget(self.page_3)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.widget_9.setStyleSheet(u"#widget_9{border:2px solid #005cb3;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_29 = QVBoxLayout(self.widget_9)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_50 = QLabel(self.widget_9)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;")
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_50)

        self.label_53 = QLabel(self.widget_9)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font-size:18px;\n"
"font-weight:800;\n"
"color:Gray;")
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_53.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.label_53)


        self.horizontalLayout_14.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.page_3)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.widget_10.setStyleSheet(u"#widget_10{border:2px solid #005cb3;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_30 = QVBoxLayout(self.widget_10)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_51 = QLabel(self.widget_10)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;")
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_51)

        self.label_54 = QLabel(self.widget_10)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"font-size:18px;\n"
"font-weight:800;\n"
"color:Gray;")
        self.label_54.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_54.setWordWrap(True)

        self.verticalLayout_30.addWidget(self.label_54)


        self.horizontalLayout_14.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.page_3)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.widget_11.setStyleSheet(u"#widget_11{border:2px solid #005cb3;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_31 = QVBoxLayout(self.widget_11)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_52 = QLabel(self.widget_11)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;")
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_52)

        self.label_55 = QLabel(self.widget_11)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font-size:18px;\n"
"font-weight:800;\n"
"color:Gray;")
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_55.setWordWrap(True)

        self.verticalLayout_31.addWidget(self.label_55)


        self.horizontalLayout_14.addWidget(self.widget_11)


        self.verticalLayout_24.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_9)

        self.pushButton_5 = QPushButton(self.page_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 90))
        self.pushButton_5.setStyleSheet(u"*{background-color: #005cb3;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 20px;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"letter-spacing: 2px;\n"
"margin: 10px 0;\n"
"text-align:left;\n"
"}\n"
"*::hover{\n"
"background-color:#003b73;\n"
"}")

        self.verticalLayout_24.addWidget(self.pushButton_5)


        self.horizontalLayout_12.addLayout(self.verticalLayout_24)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_32 = QVBoxLayout(self.page_4)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_41 = QLabel(self.page_4)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"color:#005cb3;\n"
"font-size: 32px;\n"
"font-weight:800;")

        self.horizontalLayout_19.addWidget(self.label_41)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_8)

        self.label_40 = QLabel(self.page_4)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font-size: 24px;\n"
"font-weight: 600;\n"
"color:#2c3e50;")

        self.horizontalLayout_19.addWidget(self.label_40)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_9)


        self.verticalLayout_32.addLayout(self.horizontalLayout_19)

        self.line_5 = QFrame(self.page_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"background-color:blue;")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_32.addWidget(self.line_5)

        self.label_42 = QLabel(self.page_4)
        self.label_42.setObjectName(u"label_42")
        font = QFont()
        font.setPointSize(18)
        self.label_42.setFont(font)
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_42)

        self.graphicsView = QGraphicsView(self.page_4)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_32.addWidget(self.graphicsView)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_20 = QHBoxLayout(self.page_5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_49 = QLabel(self.page_5)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"color:#005cb3;\n"
"font-size: 32px;\n"
"font-weight:800;")

        self.verticalLayout_33.addWidget(self.label_49)

        self.line_7 = QFrame(self.page_5)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background-color:blue;")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_33.addWidget(self.line_7)

        self.widget_12 = QWidget(self.page_5)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_35 = QVBoxLayout(self.widget_12)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_57 = QLabel(self.widget_12)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"font-size: 16px;\n"
"font-weight: 600;")

        self.verticalLayout_35.addWidget(self.label_57)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_59 = QLabel(self.widget_12)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color:#666666;\n"
"font-size: 13px;")

        self.horizontalLayout_21.addWidget(self.label_59)

        self.label_58 = QLabel(self.widget_12)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"color:#666666;\n"
"font-size: 13px;")

        self.horizontalLayout_21.addWidget(self.label_58)


        self.verticalLayout_35.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_11)


        self.verticalLayout_33.addWidget(self.widget_12)


        self.horizontalLayout_20.addLayout(self.verticalLayout_33)

        self.line_6 = QFrame(self.page_5)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background-color:blue;")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_20.addWidget(self.line_6)

        self.verticalWidget_5 = QWidget(self.page_5)
        self.verticalWidget_5.setObjectName(u"verticalWidget_5")
        sizePolicy5.setHeightForWidth(self.verticalWidget_5.sizePolicy().hasHeightForWidth())
        self.verticalWidget_5.setSizePolicy(sizePolicy5)
        self.verticalLayout_34 = QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_60 = QLabel(self.verticalWidget_5)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"font-size: 24px;\n"
"font-weight: 600;\n"
"color:#2c3e50;")
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_60)

        self.widget_13 = QWidget(self.verticalWidget_5)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_36 = QVBoxLayout(self.widget_13)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.widget_16 = QWidget(self.widget_13)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setStyleSheet(u"#widget_16{border:2px solid #005cb3;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_37 = QVBoxLayout(self.widget_16)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_61 = QLabel(self.widget_16)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"font-size:18px;\n"
"color:Gray;")
        self.label_61.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_61)

        self.label_62 = QLabel(self.widget_16)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;")
        self.label_62.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_62)


        self.horizontalLayout_22.addWidget(self.widget_16)

        self.widget_15 = QWidget(self.widget_13)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"#widget_15{border:2px solid #005cb3;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_38 = QVBoxLayout(self.widget_15)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_63 = QLabel(self.widget_15)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"font-size:18px;\n"
"color:Gray;")
        self.label_63.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_63)

        self.label_64 = QLabel(self.widget_15)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;")
        self.label_64.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_64)


        self.horizontalLayout_22.addWidget(self.widget_15)

        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"#widget_14{border:2px solid #005cb3;\n"
"border-radius:25px;\n"
"}")
        self.verticalLayout_39 = QVBoxLayout(self.widget_14)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_65 = QLabel(self.widget_14)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"font-size:18px;\n"
"color:Gray;")
        self.label_65.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_65)

        self.label_66 = QLabel(self.widget_14)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"font-size:32px;\n"
"font-weight:800;")
        self.label_66.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_66)


        self.horizontalLayout_22.addWidget(self.widget_14)


        self.verticalLayout_36.addLayout(self.horizontalLayout_22)

        self.widget_17 = QWidget(self.widget_13)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy6)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")

        self.verticalLayout_36.addWidget(self.widget_17)


        self.verticalLayout_34.addWidget(self.widget_13)

        self.pushButton_10 = QPushButton(self.verticalWidget_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 90))
        self.pushButton_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.pushButton_10.setStyleSheet(u"*{background-color: #005cb3;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 20px;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"letter-spacing: 2px;\n"
"margin: 10px 0;\n"
"text-align:center;\n"
"}\n"
"*::hover{\n"
"background-color:#003b73;\n"
"}")

        self.verticalLayout_34.addWidget(self.pushButton_10)


        self.horizontalLayout_20.addWidget(self.verticalWidget_5)

        self.stackedWidget.addWidget(self.page_5)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1763, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.progressBar.setFormat("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"REACTION TEST", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044c \u0441\u0432\u043e\u044e \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u2713 \u0422\u043e\u0447\u043d\u043e\u0435 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u0435 \u0440\u0435\u0430\u043a\u0446\u0438\u0438", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u2713 \u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0438 \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u2713 \u0421\u043e\u0440\u0435\u0432\u043d\u0443\u0439\u0441\u044f \u0441 \u0434\u0440\u0443\u0437\u044c\u044f\u043c\u0438", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u2713 \u0420\u0430\u0437\u043d\u044b\u0435 \u0440\u0435\u0436\u0438\u043c\u044b \u0438\u0433\u0440\u044b", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0436\u0435 \u0435\u0441\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442? \u0412\u043e\u0439\u0442\u0438", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0425\u043e\u0442\u0438\u0442\u0435 \u043f\u043e\u043f\u0440\u043e\u0431\u043e\u0432\u0430\u0442\u044c \u0431\u0435\u0437 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438?", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0441\u0442\u0435\u0432\u043e\u0439 \u0432\u0445\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f 1.0.0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"REACTION TEST", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"HHorus", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c 1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"1250 \u043e\u0447\u043a\u043e\u0432", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u043a\u0430 \u043b\u0438\u0434\u0435\u0440\u043e\u0432", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 PDF", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u041f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c HHorus", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"28 \u0444\u0435\u0432\u0440\u0430\u043b\u044f 2026", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442\u043e\u0432 \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0443\u0447\u0448\u0435\u0435 \u0432\u0440\u0435\u043c\u044f", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"182", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0432\u0440\u0435\u043c\u044f", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e \u0432 \u0440\u0435\u0439\u0442\u0438\u043d\u0433\u0435", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043d\u0435\u0439 \u043f\u043e\u0434\u0440\u044f\u0434 \u0432 \u043f\u0440\u0438\u043b\u043b\u043e\u0436\u0435\u043d\u0438\u0438", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"  \u041d\u0410\u0427\u0410\u0422\u042c \u0422\u0415\u0421\u0422", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u0437\u0430 \u043d\u0435\u0434\u0435\u043b\u044e", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043d", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0422", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0420", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0422", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0422", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0411", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0421", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"245\u043c\u0441", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"245\u043c\u0441", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"245\u043c\u0441", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"245\u043c\u0441", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"245\u043c\u0441", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"245\u043c\u0441", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"245\u043c\u0441", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"REACTION TEST", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0442\u0435\u0441\u0442", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Go/No go", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0430\u0440\u0430\u0439\u0442\u0435\u0441\u044c \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e \u0438 \u0431\u044b\u0441\u0442\u0440\u043e \u043d\u0430\u0436\u0438\u043c\u0430\u0442\u044c \u043d\u0430 \u0446\u0435\u043b\u044c \u043f\u043e\u0441\u0440\u0435\u0434\u0438 \u044d\u043a\u0440\u0430\u043d\u0430", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Duck shoot", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043f\u0430\u0434\u0438\u0442\u0435 \u043f\u043e \u043b\u0435\u0442\u0430\u044e\u0449\u0438\u043c \u0446\u0435\u043b\u044f\u043c \u0432\u044b\u043b\u0435\u0442\u0430\u044e\u0449\u0438\u043c \u0434\u0440\u0443\u0433 \u0437\u0430 \u0434\u0440\u0443\u0433\u043e\u043c", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Hit baloons", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043b\u0438 \u043f\u043e\u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u0438 \u0438\u0441\u0447\u0435\u0437\u0430\u044e\u0442 \u043f\u043e\u0441\u0442\u0430\u0440\u0430\u0439\u0442\u0435\u0441\u044c \u043f\u043e\u0439\u043c\u0430\u0442\u044c \u043a\u0430\u043a \u043c\u043e\u0436\u043d\u043e \u0431\u043e\u043b\u044c\u0448\u0435", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"  \u041d\u0410\u0427\u0410\u0422\u042c \u0422\u0415\u0421\u0422", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"REACTION TEST", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"REACTION TEST", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u043f\u0430\u0434\u0430\u043d\u0438\u0439", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0432\u0440\u0435\u043c\u044f", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0448\u0438\u0431\u043e\u043a", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0433\u043b\u0430\u0432\u043d\u0443\u044e", None))
    # retranslateUi

