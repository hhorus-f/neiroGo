import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QLineEdit, QPushButton, QCheckBox, 
                               QFrame, QMessageBox)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPixmap, QPainter, QColor, QLinearGradient, QBrush, QPalette

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация - Reaction Test")
        self.setFixedSize(400, 600)
        self.setup_ui()
        self.apply_styles()
    
    def setup_ui(self):
        # Главный layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 40, 30, 30)
        main_layout.setSpacing(20)
        
        # Логотип/заголовок
        title_label = QLabel("⚡ Reaction Test")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("titleLabel")
        main_layout.addWidget(title_label)
        
        # Подзаголовок
        subtitle_label = QLabel("Создайте аккаунт для отслеживания прогресса")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setObjectName("subtitleLabel")
        main_layout.addWidget(subtitle_label)
        
        # Форма регистрации
        form_frame = QFrame()
        form_frame.setObjectName("formFrame")
        form_layout = QVBoxLayout(form_frame)
        form_layout.setSpacing(15)
        
        # Поле имени
        name_label = QLabel("Имя пользователя")
        name_label.setObjectName("fieldLabel")
        form_layout.addWidget(name_label)
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите имя")
        self.name_input.setObjectName("nameInput")
        form_layout.addWidget(self.name_input)
        
        # Поле email
        email_label = QLabel("Email")
        email_label.setObjectName("fieldLabel")
        form_layout.addWidget(email_label)
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("example@mail.com")
        self.email_input.setObjectName("emailInput")
        form_layout.addWidget(self.email_input)
        
        # Поле пароля
        password_label = QLabel("Пароль")
        password_label.setObjectName("fieldLabel")
        form_layout.addWidget(password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Минимум 8 символов")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setObjectName("passwordInput")
        form_layout.addWidget(self.password_input)
        
        # Поле подтверждения пароля
        confirm_label = QLabel("Подтвердите пароль")
        confirm_label.setObjectName("fieldLabel")
        form_layout.addWidget(confirm_label)
        
        self.confirm_input = QLineEdit()
        self.confirm_input.setPlaceholderText("Введите пароль ещё раз")
        self.confirm_input.setEchoMode(QLineEdit.Password)
        self.confirm_input.setObjectName("confirmInput")
        form_layout.addWidget(self.confirm_input)
        
        # Чекбокс согласия
        self.agree_check = QCheckBox("Я согласен с условиями использования")
        self.agree_check.setObjectName("agreeCheck")
        form_layout.addWidget(self.agree_check)
        
        main_layout.addWidget(form_frame)
        
        # Кнопка регистрации
        self.register_btn = QPushButton("Создать аккаунт")
        self.register_btn.setObjectName("registerBtn")
        self.register_btn.setCursor(Qt.PointingHandCursor)
        self.register_btn.clicked.connect(self.handle_register)
        main_layout.addWidget(self.register_btn)
        
        # Разделитель
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setObjectName("separator")
        main_layout.addWidget(separator)
        
        # Ссылка на вход
        login_layout = QHBoxLayout()
        login_layout.setAlignment(Qt.AlignCenter)
        
        login_text = QLabel("Уже есть аккаунт?")
        login_text.setObjectName("loginText")
        
        self.login_link = QPushButton("Войти")
        self.login_link.setObjectName("loginLink")
        self.login_link.setCursor(Qt.PointingHandCursor)
        self.login_link.setFlat(True)
        
        login_layout.addWidget(login_text)
        login_layout.addWidget(self.login_link)
        
        main_layout.addLayout(login_layout)
        
        # Добавляем растяжку в конец
        main_layout.addStretch()
        
        self.setLayout(main_layout)
    
    def apply_styles(self):
        # Основные цвета
        primary_color = "#005cb3"
        white_color = "#ffffff"
        light_gray = "#f5f5f5"
        dark_gray = "#333333"
        border_color = "#e0e0e0"
        
        # Градиентный фон
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, white_color)
        gradient.setColorAt(1, "#f0f7ff")
        
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)
        
        # Стили через setStyleSheet
        self.setStyleSheet(f"""
            QWidget {{
                font-family: 'Segoe UI', Arial, sans-serif;
            }}
            
            #titleLabel {{
                font-size: 28px;
                font-weight: bold;
                color: {primary_color};
                margin-bottom: 5px;
            }}
            
            #subtitleLabel {{
                font-size: 14px;
                color: #666666;
                margin-bottom: 20px;
            }}
            
            #formFrame {{
                background-color: {white_color};
                border-radius: 15px;
                border: 1px solid {border_color};
                padding: 20px;
            }}
            
            #fieldLabel {{
                font-size: 13px;
                font-weight: 600;
                color: {dark_gray};
                margin-bottom: 3px;
            }}
            
            QLineEdit {{
                padding: 12px 15px;
                border: 2px solid {border_color};
                border-radius: 8px;
                font-size: 14px;
                background-color: {light_gray};
                color: {dark_gray};
            }}
            
            QLineEdit:focus {{
                border: 2px solid {primary_color};
                background-color: {white_color};
            }}
            
            QLineEdit:hover {{
                border: 2px solid {primary_color};
            }}
            
            #agreeCheck {{
                font-size: 13px;
                color: #666666;
                margin-top: 5px;
            }}
            
            #agreeCheck::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 4px;
                border: 2px solid {border_color};
            }}
            
            #agreeCheck::indicator:checked {{
                background-color: {primary_color};
                border: 2px solid {primary_color};
            }}
            
            #registerBtn {{
                background-color: {primary_color};
                color: {white_color};
                border: none;
                border-radius: 8px;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
            }}
            
            #registerBtn:hover {{
                background-color: #004799;
            }}
            
            #registerBtn:pressed {{
                background-color: #003b80;
            }}
            
            #separator {{
                background-color: {border_color};
                max-height: 1px;
                margin: 10px 0;
            }}
            
            #loginText {{
                font-size: 13px;
                color: #666666;
            }}
            
            #loginLink {{
                color: {primary_color};
                font-size: 13px;
                font-weight: 600;
                border: none;
                background: transparent;
                padding: 5px;
                text-decoration: underline;
            }}
            
            #loginLink:hover {{
                color: #004799;
            }}
        """)
    
    def handle_register(self):
        # Простая валидация
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text()
        confirm = self.confirm_input.text()
        
        if not all([name, email, password, confirm]):
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля")
            return
        
        if password != confirm:
            QMessageBox.warning(self, "Ошибка", "Пароли не совпадают")
            return
        
        if len(password) < 8:
            QMessageBox.warning(self, "Ошибка", "Пароль должен содержать минимум 8 символов")
            return
        
        if not self.agree_check.isChecked():
            QMessageBox.warning(self, "Ошибка", "Необходимо принять условия использования")
            return
        
        # Успешная регистрация
        QMessageBox.information(self, "Успех", "Аккаунт успешно создан!")
        
        # Здесь можно добавить переход на главный экран
        # или очистку полей
        self.clear_fields()
    
    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.password_input.clear()
        self.confirm_input.clear()
        self.agree_check.setChecked(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Настройка шрифта по умолчанию
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    window = RegisterWindow()
    window.show()
    
    sys.exit(app.exec())