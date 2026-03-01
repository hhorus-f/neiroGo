import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QPushButton, QFrame)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect
from PySide6.QtGui import QFont, QLinearGradient, QBrush, QPalette, QPainter, QColor

class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reaction Test - Добро пожаловать!")
        self.setFixedSize(1200, 1000)
        self.setup_ui()
        self.apply_styles()
    
    def setup_ui(self):
        # Главный layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 50, 30, 40)
        main_layout.setSpacing(25)
        
        # Верхняя декоративная полоса с градиентом
        top_bar = QFrame()
        top_bar.setFixedHeight(8)
        top_bar.setObjectName("topBar")
        main_layout.addWidget(top_bar)
        
        # Логотип с анимацией (статичная версия)
        logo_container = QFrame()
        logo_container.setObjectName("logoContainer")
        logo_layout = QVBoxLayout(logo_container)
        
        # Большой символ молнии
        lightning_label = QLabel("⚡")
        lightning_label.setAlignment(Qt.AlignCenter)
        lightning_label.setObjectName("lightningLogo")
        logo_layout.addWidget(lightning_label)
        
        # Название приложения
        title_label = QLabel("REACTION TEST")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("mainTitle")
        logo_layout.addWidget(title_label)
        
        # Слоган
        slogan_label = QLabel("Проверь свою скорость реакции")
        slogan_label.setAlignment(Qt.AlignCenter)
        slogan_label.setObjectName("slogan")
        logo_layout.addWidget(slogan_label)
        
        main_layout.addWidget(logo_container)
        
        # Карточка с преимуществами
        features_frame = QFrame()
        features_frame.setObjectName("featuresFrame")
        features_layout = QVBoxLayout(features_frame)
        features_layout.setSpacing(12)
        
        # Список преимуществ
        features = [
            "✓ Точное измерение реакции",
            "✓ Статистика и прогресс",
            "✓ Соревнуйся с друзьями",
            "✓ Разные режимы игры"
        ]
        
        for feature in features:
            feature_label = QLabel(feature)
            feature_label.setObjectName("featureLabel")
            features_layout.addWidget(feature_label)
        
        main_layout.addWidget(features_frame)
        
        # Добавляем растяжку между карточкой и кнопками
        main_layout.addStretch()
        
        # Контейнер для кнопок
        buttons_container = QFrame()
        buttons_container.setObjectName("buttonsContainer")
        buttons_layout = QVBoxLayout(buttons_container)
        buttons_layout.setSpacing(12)
        
        # Кнопка регистрации
        self.register_btn = QPushButton("Создать аккаунт")
        self.register_btn.setObjectName("registerBtn")
        self.register_btn.setCursor(Qt.PointingHandCursor)
        buttons_layout.addWidget(self.register_btn)
        
        # Кнопка входа
        self.login_btn = QPushButton("Уже есть аккаунт? Войти")
        self.login_btn.setObjectName("loginBtn")
        self.login_btn.setCursor(Qt.PointingHandCursor)
        buttons_layout.addWidget(self.login_btn)
        
        main_layout.addWidget(buttons_container)
        
        # Нижний текст
        guest_layout = QHBoxLayout()
        guest_layout.setAlignment(Qt.AlignCenter)
        
        guest_text = QLabel("Хотите попробовать без регистрации?")
        guest_text.setObjectName("guestText")
        
        self.guest_btn = QPushButton("Гостевой вход")
        self.guest_btn.setObjectName("guestBtn")
        self.guest_btn.setCursor(Qt.PointingHandCursor)
        self.guest_btn.setFlat(True)
        
        guest_layout.addWidget(guest_text)
        guest_layout.addWidget(self.guest_btn)
        
        main_layout.addLayout(guest_layout)
        
        # Версия приложения
        version_label = QLabel("Версия 1.0.0")
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setObjectName("versionLabel")
        main_layout.addWidget(version_label)
        
        self.setLayout(main_layout)
    
    def apply_styles(self):
        # Основные цвета
        primary_color = "#005cb3"
        white_color = "#ffffff"
        light_blue = "#cee7ff"
        dark_gray = "#333333"
        
        # Градиентный фон
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, white_color)
        gradient.setColorAt(0.7, light_blue)
        gradient.setColorAt(1, "#d4e4f5")
        
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)
        
        self.setStyleSheet(f"""
            QWidget {{
                font-family: 'Segoe UI', Arial, sans-serif;
            }}
            
            #topBar {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {primary_color}, stop:0.5 #0077e6, stop:1 {primary_color});
                border-radius: 4px;
            }}
            
            #logoContainer {{
                margin-top: 20px;
            }}
            
            #lightningLogo {{
                font-size: 80px;
                color: {primary_color};
                margin-bottom: 10px;
            }}
            
            #mainTitle {{
                font-size: 32px;
                font-weight: 800;
                letter-spacing: 3px;
                color: {dark_gray};
            }}
            
            #slogan {{
                font-size: 16px;
                color: #666666;
                margin-top: 5px;
            }}
            
            #featuresFrame {{
                background-color: rgba(255, 255, 255, 0.7);
                border-radius: 20px;
                padding: 20px;
                margin-top: 20px;
                border: 1px solid rgba(0, 92, 179, 0.2);
            }}
            
            #featureLabel {{
                font-size: 15px;
                color: {dark_gray};
                padding: 8px 15px;
                background-color: {white_color};
                border-radius: 25px;
                margin: 2px 0;
            }}
            
            #featureLabel:hover {{
                background-color: {light_blue};
                padding-left: 20px;
            }}
            
            #buttonsContainer {{
                margin-top: 10px;
            }}
            
            #registerBtn {{
                background-color: {primary_color};
                color: {white_color};
                border: none;
                border-radius: 30px;
                padding: 18px;
                font-size: 18px;
                font-weight: bold;
                min-width: 250px;
            }}
            
            #registerBtn:hover {{
                background-color: #004799;
                transform: scale(1.02);
            }}
            
            #registerBtn:pressed {{
                background-color: #003b80;
            }}
            
            #loginBtn {{
                background-color: transparent;
                color: {primary_color};
                border: 2px solid {primary_color};
                border-radius: 30px;
                padding: 16px;
                font-size: 16px;
                font-weight: 600;
            }}
            
            #loginBtn:hover {{
                background-color: rgba(0, 92, 179, 0.1);
            }}
            
            #loginBtn:pressed {{
                background-color: rgba(0, 92, 179, 0.2);
            }}
            
            #guestText {{
                font-size: 13px;
                color: #666666;
            }}
            
            #guestBtn {{
                color: {primary_color};
                font-size: 13px;
                font-weight: 600;
                border: none;
                background: transparent;
                text-decoration: underline;
                padding: 5px;
            }}
            
            #guestBtn:hover {{
                color: #004799;
            }}
            
            #versionLabel {{
                font-size: 11px;
                color: #999999;
                margin-top: 10px;
            }}
        """)
    
    def add_hover_animation(self, widget):
        # Создание анимации при наведении
        self.anim = QPropertyAnimation(widget, b"geometry")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        return self.anim


class ReactionTestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.start_window = StartWindow()
        self.start_window.show()
        
        # Здесь можно подключить переходы на другие окна
        # self.start_window.register_btn.clicked.connect(self.open_register)
        # self.start_window.login_btn.clicked.connect(self.open_login)
        # self.start_window.guest_btn.clicked.connect(self.open_guest_mode)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Настройка шрифта по умолчанию
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    window = StartWindow()
    window.show()
    
    sys.exit(app.exec())