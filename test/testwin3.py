import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QPushButton, QFrame, QProgressBar, QStackedWidget,
                               QListWidget, QListWidgetItem, QGridLayout)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize
from PySide6.QtGui import QFont, QLinearGradient, QBrush, QPalette, QIcon, QAction

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reaction Test - Проверка реакции")
        self.setMinimumSize(1000, 700)
        self.setup_main_ui()
        self.apply_styles()
        
    def setup_main_ui(self):
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Главный горизонтальный layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # ========== ЛЕВАЯ ПАНЕЛЬ (НАВИГАЦИЯ) ==========
        left_panel = QFrame()
        left_panel.setObjectName("leftPanel")
        left_panel.setFixedWidth(280)
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(20, 30, 20, 30)
        left_layout.setSpacing(20)
        
        # Логотип
        logo_label = QLabel("REACTION TEST")
        logo_label.setObjectName("logoLabel")
        logo_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(logo_label)
        
        # Разделитель
        separator = QFrame()
        separator.setObjectName("navSeparator")
        separator.setFixedHeight(2)
        left_layout.addWidget(separator)
        
        # Профиль пользователя (всегда видимый)
        profile_frame = QFrame()
        profile_frame.setObjectName("profileFrame")
        profile_layout = QHBoxLayout(profile_frame)
        profile_layout.setContentsMargins(15, 15, 15, 15)
        
        # Аватар
        avatar_label = QLabel("A")
        avatar_label.setObjectName("avatarLabel")
        avatar_label.setFixedSize(50, 50)
        avatar_label.setAlignment(Qt.AlignCenter)
        
        # Информация
        user_info = QVBoxLayout()
        user_name = QLabel("Алексей Петров")
        user_name.setObjectName("userName")
        user_level = QLabel("Уровень 7 · 1250 очков")
        user_level.setObjectName("userLevel")
        
        user_info.addWidget(user_name)
        user_info.addWidget(user_level)
        
        profile_layout.addWidget(avatar_label)
        profile_layout.addLayout(user_info)
        profile_layout.addStretch()
        
        left_layout.addWidget(profile_frame)
        
        # Кнопки навигации
        nav_buttons = [
            ("🏠 Главная", "home"),
            ("📊 Статистика", "stats"),
            ("⚙️ Настройки", "settings"),
            ("❓ Помощь", "help")
        ]
        
        self.nav_buttons = {}
        for text, name in nav_buttons:
            btn = QPushButton(text)
            btn.setObjectName(f"navBtn_{name}")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedHeight(50)
            left_layout.addWidget(btn)
            self.nav_buttons[name] = btn
        
        # Растяжка
        left_layout.addStretch()
        
        # Кнопка выхода
        self.logout_btn = QPushButton("🚪 Выйти")
        self.logout_btn.setObjectName("logoutBtn")
        self.logout_btn.setCursor(Qt.PointingHandCursor)
        self.logout_btn.setFixedHeight(45)
        left_layout.addWidget(self.logout_btn)
        
        # ========== ПРАВАЯ ПАНЕЛЬ (КОНТЕНТ) ==========
        right_panel = QFrame()
        right_panel.setObjectName("rightPanel")
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(30, 30, 30, 30)
        right_layout.setSpacing(25)
        
        # Верхняя панель с приветствием
        welcome_frame = QFrame()
        welcome_frame.setObjectName("welcomeFrame")
        welcome_layout = QHBoxLayout(welcome_frame)
        
        welcome_text = QLabel("Добро пожаловать, Алексей! 👋")
        welcome_text.setObjectName("welcomeText")
        
        date_label = QLabel("28 февраля 2026")
        date_label.setObjectName("dateLabel")
        
        welcome_layout.addWidget(welcome_text)
        welcome_layout.addStretch()
        welcome_layout.addWidget(date_label)
        
        right_layout.addWidget(welcome_frame)
        
        # ========== ОСНОВНОЙ КОНТЕНТ ==========
        content_frame = QFrame()
        content_frame.setObjectName("contentFrame")
        content_layout = QVBoxLayout(content_frame)
        content_layout.setSpacing(25)
        
        # Верхняя строка с карточками статистики
        stats_row = QHBoxLayout()
        stats_row.setSpacing(20)
        
        # Карточки статистики
        stat_cards = [
            ("Тестов сегодня", "8", "+2"),
            ("Лучшее время", "187 мс", "🏆"),
            ("Среднее время", "245 мс", "📈"),
            ("Место в рейтинге", "#124", "⬆️")
        ]
        
        for title, value, change in stat_cards:
            card = self.create_stat_card(title, value, change)
            stats_row.addWidget(card)
        
        content_layout.addLayout(stats_row)
        
        # Кнопка начала теста
        self.start_test_btn = QPushButton("🚀 НАЧАТЬ ТЕСТ РЕАКЦИИ")
        self.start_test_btn.setObjectName("startTestBigBtn")
        self.start_test_btn.setCursor(Qt.PointingHandCursor)
        self.start_test_btn.setFixedHeight(100)
        content_layout.addWidget(self.start_test_btn)
        
        # Нижняя строка с графиками и историей
        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(20)
        
        # Левая колонка - график прогресса
        progress_frame = QFrame()
        progress_frame.setObjectName("progressFrame")
        progress_frame.setFixedWidth(400)
        progress_layout = QVBoxLayout(progress_frame)
        
        progress_title = QLabel("Прогресс за неделю")
        progress_title.setObjectName("sectionTitle")
        progress_layout.addWidget(progress_title)
        
        # Создаем простую визуализацию прогресса
        days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
        values = [245, 198, 312, 187, 234, 201, 178]
        
        for i, (day, value) in enumerate(zip(days, values)):
            day_frame = QFrame()
            day_frame.setObjectName("dayFrame")
            day_layout = QHBoxLayout(day_frame)
            
            day_label = QLabel(day)
            day_label.setObjectName("dayLabel")
            day_label.setFixedWidth(40)
            
            bar_frame = QFrame()
            bar_frame.setObjectName("barFrame")
            bar_layout = QHBoxLayout(bar_frame)
            bar_layout.setContentsMargins(0, 0, 0, 0)
            
            bar = QFrame()
            bar.setObjectName("progressBar")
            bar.setFixedWidth(value // 2)  # Простая пропорция
            bar.setFixedHeight(20)
            
            value_label = QLabel(f"{value} мс")
            value_label.setObjectName("valueLabel")
            
            bar_layout.addWidget(bar)
            bar_layout.addStretch()
            
            day_layout.addWidget(day_label)
            day_layout.addWidget(bar_frame)
            day_layout.addWidget(value_label)
            
            progress_layout.addWidget(day_frame)
        
        progress_layout.addStretch()
        bottom_row.addWidget(progress_frame)
        
        # Правая колонка - последние результаты
        history_frame = QFrame()
        history_frame.setObjectName("historyFrame")
        history_layout = QVBoxLayout(history_frame)
        
        history_title = QLabel("Последние результаты")
        history_title.setObjectName("sectionTitle")
        history_layout.addWidget(history_title)
        
        # Список результатов
        results = [
            ("Простой режим", "245 мс", "2 мин назад", "#4CAF50"),
            ("Сложный режим", "312 мс", "15 мин назад", "#FF9800"),
            ("Тренировка", "198 мс", "1 час назад", "#4CAF50"),
            ("Простой режим", "267 мс", "3 часа назад", "#FF9800"),
            ("Сложный режим", "189 мс", "вчера", "#4CAF50")
        ]
        
        for mode, time, ago, color in results:
            result_item = QFrame()
            result_item.setObjectName("historyItem")
            item_layout = QHBoxLayout(result_item)
            
            mode_label = QLabel(mode)
            mode_label.setObjectName("historyMode")
            
            time_label = QLabel(time)
            time_label.setObjectName("historyTime")
            time_label.setStyleSheet(f"color: {color}; font-weight: bold;")
            
            ago_label = QLabel(ago)
            ago_label.setObjectName("historyAgo")
            
            item_layout.addWidget(mode_label)
            item_layout.addStretch()
            item_layout.addWidget(time_label)
            item_layout.addWidget(ago_label)
            
            history_layout.addWidget(result_item)
        
        history_layout.addStretch()
        bottom_row.addWidget(history_frame)
        
        content_layout.addLayout(bottom_row)
        right_layout.addWidget(content_frame)
        
        # Добавляем панели в главный layout
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel, 1)
    
    def create_stat_card(self, title, value, change):
        card = QFrame()
        card.setObjectName("statCard")
        card.setFixedHeight(120)
        layout = QVBoxLayout(card)
        
        title_label = QLabel(title)
        title_label.setObjectName("statTitle")
        
        value_label = QLabel(value)
        value_label.setObjectName("statValue")
        
        change_label = QLabel(change)
        change_label.setObjectName("statChange")
        
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addWidget(change_label)
        layout.addStretch()
        
        return card
    
    def apply_styles(self):
        primary_color = "#005cb3"
        white_color = "#ffffff"
        light_bg = "#f5f7fa"
        dark_bg = "#2c3e50"
        border_color = "#e1e8ed"
        
        self.setStyleSheet(f"""
            QMainWindow, QWidget {{
                background-color: {light_bg};
                font-family: 'Segoe UI', Arial, sans-serif;
            }}
            
            /* Левая панель */
            #leftPanel {{
                background-color: {white_color};
                border-right: 2px solid {border_color};
            }}
            
            #logoLabel {{
                font-size: 22px;
                font-weight: bold;
                color: {primary_color};
                padding: 20px 0;
            }}
            
            #navSeparator {{
                background-color: {border_color};
                margin: 10px 0;
            }}
            
            /* Профиль */
            #profileFrame {{
                background-color: #f8f9fa;
                border-radius: 15px;
                margin: 10px 0;
            }}
            
            #avatarLabel {{
                background-color: {primary_color};
                color: white;
                font-size: 20px;
                font-weight: bold;
                border-radius: 25px;
            }}
            
            #userName {{
                font-size: 16px;
                font-weight: 600;
                color: {dark_bg};
            }}
            
            #userLevel {{
                font-size: 13px;
                color: #7f8c8d;
            }}
            
            /* Кнопки навигации */
            QPushButton {{
                text-align: left;
                padding: 0 20px;
                border-radius: 10px;
                font-size: 15px;
                font-weight: 500;
            }}
            
            #navBtn_home, #navBtn_stats, #navBtn_settings, #navBtn_help {{
                background-color: transparent;
                color: {dark_bg};
                border: none;
            }}
            
            #navBtn_home:hover, #navBtn_stats:hover, #navBtn_settings:hover, #navBtn_help:hover {{
                background-color: #eef2f6;
            }}
            
            #navBtn_home:checked, #navBtn_stats:checked, #navBtn_settings:checked, #navBtn_help:checked {{
                background-color: {primary_color};
                color: white;
            }}
            
            #logoutBtn {{
                background-color: transparent;
                color: #e74c3c;
                border: 2px solid #e74c3c;
                text-align: center;
            }}
            
            #logoutBtn:hover {{
                background-color: #e74c3c;
                color: white;
            }}
            
            /* Правая панель */
            #rightPanel {{
                background-color: {light_bg};
            }}
            
            #welcomeFrame {{
                background-color: transparent;
            }}
            
            #welcomeText {{
                font-size: 24px;
                font-weight: 600;
                color: {dark_bg};
            }}
            
            #dateLabel {{
                font-size: 16px;
                color: #7f8c8d;
            }}
            
            /* Карточки статистики */
            #statCard {{
                background-color: white;
                border-radius: 15px;
                padding: 15px;
                border: 1px solid {border_color};
                min-width: 150px;
            }}
            
            #statTitle {{
                font-size: 14px;
                color: #7f8c8d;
            }}
            
            #statValue {{
                font-size: 28px;
                font-weight: bold;
                color: {dark_bg};
                margin-top: 5px;
            }}
            
            #statChange {{
                font-size: 14px;
                color: {primary_color};
            }}
            
            /* Кнопка старта */
            #startTestBigBtn {{
                background-color: {primary_color};
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 24px;
                font-weight: bold;
                letter-spacing: 2px;
                margin: 10px 0;
            }}
            
            #startTestBigBtn:hover {{
                background-color: #004799;
            }}
            
            #startTestBigBtn:pressed {{
                background-color: #003b80;
            }}
            
            /* Прогресс и история */
            #progressFrame, #historyFrame {{
                background-color: white;
                border-radius: 20px;
                padding: 20px;
                border: 1px solid {border_color};
            }}
            
            #sectionTitle {{
                font-size: 18px;
                font-weight: 600;
                color: {dark_bg};
                margin-bottom: 15px;
            }}
            
            #dayFrame {{
                margin: 8px 0;
            }}
            
            #dayLabel {{
                font-size: 14px;
                font-weight: 600;
                color: {dark_bg};
            }}
            
            #progressBar {{
                background-color: {primary_color};
                border-radius: 10px;
                min-width: 30px;
            }}
            
            #valueLabel {{
                font-size: 13px;
                color: #7f8c8d;
                min-width: 60px;
            }}
            
            #historyItem {{
                background-color: #f8f9fa;
                border-radius: 10px;
                padding: 8px 15px;
                margin: 3px 0;
            }}
            
            #historyItem:hover {{
                background-color: #eef2f6;
            }}
            
            #historyMode {{
                font-size: 14px;
                color: {dark_bg};
            }}
            
            #historyTime {{
                font-size: 14px;
                margin-right: 20px;
            }}
            
            #historyAgo {{
                font-size: 12px;
                color: #95a5a6;
                min-width: 70px;
            }}
            
            #barFrame {{
                background-color: #eef2f6;
                border-radius: 10px;
                height: 20px;
            }}
        """)


class ProfileWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reaction Test - Профиль")
        self.setMinimumSize(900, 600)
        self.setup_profile_ui()
        self.apply_styles()
    
    def setup_profile_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(30)
        
        # ========== ЛЕВАЯ КОЛОНКА - АВАТАР И ОСНОВНАЯ ИНФО ==========
        left_column = QFrame()
        left_column.setObjectName("profileLeftColumn")
        left_column.setFixedWidth(350)
        left_layout = QVBoxLayout(left_column)
        left_layout.setSpacing(20)
        
        # Кнопка назад
        self.back_btn = QPushButton("← На главную")
        self.back_btn.setObjectName("backBtn")
        self.back_btn.setCursor(Qt.PointingHandCursor)
        left_layout.addWidget(self.back_btn)
        
        # Аватар
        avatar_frame = QFrame()
        avatar_frame.setObjectName("profileAvatarFrame")
        avatar_layout = QVBoxLayout(avatar_frame)
        
        avatar_big = QLabel("A")
        avatar_big.setObjectName("profileAvatarBig")
        avatar_big.setAlignment(Qt.AlignCenter)
        avatar_big.setFixedSize(150, 150)
        
        avatar_layout.addWidget(avatar_big, 0, Qt.AlignCenter)
        left_layout.addWidget(avatar_frame)
        
        # Имя пользователя
        name_label = QLabel("Алексей Петров")
        name_label.setObjectName("profileName")
        name_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(name_label)
        
        # Email
        email_label = QLabel("alexey.petrov@email.com")
        email_label.setObjectName("profileEmail")
        email_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(email_label)
        
        # Кнопка редактирования
        edit_btn = QPushButton("✎ Редактировать профиль")
        edit_btn.setObjectName("editProfileBtn")
        edit_btn.setCursor(Qt.PointingHandCursor)
        left_layout.addWidget(edit_btn)
        
        left_layout.addStretch()
        
        # ========== ПРАВАЯ КОЛОНКА - ДЕТАЛЬНАЯ СТАТИСТИКА ==========
        right_column = QFrame()
        right_column.setObjectName("profileRightColumn")
        right_layout = QVBoxLayout(right_column)
        right_layout.setSpacing(25)
        
        # Заголовок
        stats_title = QLabel("Детальная статистика")
        stats_title.setObjectName("profileStatsTitle")
        right_layout.addWidget(stats_title)
        
        # Сетка статистики
        stats_grid = QFrame()
        stats_grid.setObjectName("statsGrid")
        grid_layout = QGridLayout(stats_grid)
        grid_layout.setSpacing(15)
        
        stats_items = [
            ("Всего тестов", "156", "📊"),
            ("Лучшее время", "187 мс", "⚡"),
            ("Среднее время", "245 мс", "📈"),
            ("Побед", "98", "🏆"),
            ("Поражений", "58", "📉"),
            ("Точность", "78%", "🎯"),
            ("В рейтинге", "#124", "👑"),
            ("Друзей", "12", "👥"),
            ("Достижений", "15/30", "🏅")
        ]
        
        for i, (label, value, icon) in enumerate(stats_items):
            row, col = i // 3, i % 3
            item_frame = QFrame()
            item_frame.setObjectName("statItemFrame")
            item_layout = QVBoxLayout(item_frame)
            
            icon_label = QLabel(icon)
            icon_label.setObjectName("statItemIcon")
            
            value_label = QLabel(value)
            value_label.setObjectName("statItemValue")
            
            desc_label = QLabel(label)
            desc_label.setObjectName("statItemLabel")
            
            item_layout.addWidget(icon_label)
            item_layout.addWidget(value_label)
            item_layout.addWidget(desc_label)
            
            grid_layout.addWidget(item_frame, row, col)
        
        right_layout.addWidget(stats_grid)
        
        # График прогресса
        progress_frame = QFrame()
        progress_frame.setObjectName("profileProgressFrame")
        progress_layout = QVBoxLayout(progress_frame)
        
        progress_title = QLabel("Прогресс за месяц")
        progress_title.setObjectName("progressTitle")
        progress_layout.addWidget(progress_title)
        
        # Простая визуализация прогресса
        weeks = ["Неделя 1", "Неделя 2", "Неделя 3", "Неделя 4"]
        week_values = [210, 195, 183, 172]
        
        for week, value in zip(weeks, week_values):
            week_frame = QFrame()
            week_layout = QHBoxLayout(week_frame)
            
            week_label = QLabel(week)
            week_label.setObjectName("weekLabel")
            week_label.setFixedWidth(80)
            
            bar_frame = QFrame()
            bar_frame.setObjectName("weekBarFrame")
            bar_layout = QHBoxLayout(bar_frame)
            
            bar = QFrame()
            bar.setObjectName("weekBar")
            bar.setFixedWidth(value * 2)
            bar.setFixedHeight(25)
            
            value_label = QLabel(f"{value} мс")
            value_label.setObjectName("weekValue")
            
            bar_layout.addWidget(bar)
            bar_layout.addStretch()
            
            week_layout.addWidget(week_label)
            week_layout.addWidget(bar_frame)
            week_layout.addWidget(value_label)
            
            progress_layout.addWidget(week_frame)
        
        right_layout.addWidget(progress_frame)
        
        # Добавляем колонки в главный layout
        main_layout.addWidget(left_column)
        main_layout.addWidget(right_column, 1)
    
    def apply_styles(self):
        primary_color = "#005cb3"
        white_color = "#ffffff"
        light_bg = "#f5f7fa"
        dark_bg = "#2c3e50"
        
        self.setStyleSheet(f"""
            QMainWindow, QWidget {{
                background-color: {light_bg};
                font-family: 'Segoe UI', Arial, sans-serif;
            }}
            
            #profileLeftColumn {{
                background-color: white;
                border-radius: 25px;
                padding: 30px;
            }}
            
            #backBtn {{
                background-color: transparent;
                color: {primary_color};
                border: 2px solid {primary_color};
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                font-weight: 600;
                text-align: center;
            }}
            
            #backBtn:hover {{
                background-color: {primary_color};
                color: white;
            }}
            
            #profileAvatarFrame {{
                margin: 20px 0;
            }}
            
            #profileAvatarBig {{
                background-color: {primary_color};
                color: white;
                font-size: 60px;
                font-weight: bold;
                border-radius: 75px;
                margin: 0 auto;
            }}
            
            #profileName {{
                font-size: 24px;
                font-weight: bold;
                color: {dark_bg};
                margin-top: 10px;
            }}
            
            #profileEmail {{
                font-size: 14px;
                color: #7f8c8d;
                margin-bottom: 20px;
            }}
            
            #editProfileBtn {{
                background-color: {primary_color};
                color: white;
                border: none;
                border-radius: 15px;
                padding: 15px;
                font-size: 16px;
                font-weight: 600;
            }}
            
            #editProfileBtn:hover {{
                background-color: #004799;
            }}
            
            #profileRightColumn {{
                background-color: transparent;
            }}
            
            #profileStatsTitle {{
                font-size: 28px;
                font-weight: bold;
                color: {dark_bg};
                margin-bottom: 20px;
            }}
            
            #statsGrid {{
                background-color: white;
                border-radius: 25px;
                padding: 20px;
            }}
            
            #statItemFrame {{
                background-color: #f8f9fa;
                border-radius: 15px;
                padding: 20px;
                min-width: 130px;
            }}
            
            #statItemIcon {{
                font-size: 24px;
                margin-bottom: 10px;
            }}
            
            #statItemValue {{
                font-size: 22px;
                font-weight: bold;
                color: {primary_color};
            }}
            
            #statItemLabel {{
                font-size: 13px;
                color: #7f8c8d;
                margin-top: 5px;
            }}
            
            #profileProgressFrame {{
                background-color: white;
                border-radius: 25px;
                padding: 25px;
                margin-top: 20px;
            }}
            
            #progressTitle {{
                font-size: 20px;
                font-weight: 600;
                color: {dark_bg};
                margin-bottom: 20px;
            }}
            
            #weekLabel {{
                font-size: 14px;
                font-weight: 600;
                color: {dark_bg};
            }}
            
            #weekBarFrame {{
                background-color: #eef2f6;
                border-radius: 12px;
                height: 25px;
            }}
            
            #weekBar {{
                background-color: {primary_color};
                border-radius: 12px;
                min-width: 30px;
            }}
            
            #weekValue {{
                font-size: 14px;
                color: {primary_color};
                font-weight: 600;
                min-width: 60px;
            }}
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Настройка шрифта
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    # Запуск главного окна
    window = MainApplication()
    window.show()
    
    # Для демонстрации профиля:
    # profile = ProfileWindow()
    # profile.show()
    
    sys.exit(app.exec())