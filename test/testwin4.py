import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QPushButton, QFrame, QButtonGroup, QRadioButton,
                               QScrollArea, QGridLayout)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize
from PySide6.QtGui import QFont, QLinearGradient, QBrush, QPalette, QPixmap, QPainter, QColor

class TestSelectionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reaction Test - Выбор теста")
        self.setMinimumSize(1200, 700)
        self.setup_ui()
        self.apply_styles()
        
    def setup_ui(self):
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
        left_layout.setSpacing(15)
        
        # Логотип
        logo_label = QLabel("⚡ REACTION TEST")
        logo_label.setObjectName("logoLabel")
        logo_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(logo_label)
        
        # Разделитель
        separator = QFrame()
        separator.setObjectName("navSeparator")
        separator.setFixedHeight(2)
        left_layout.addWidget(separator)
        
        # Профиль пользователя
        profile_btn = QPushButton()
        profile_btn.setObjectName("profileBtn")
        profile_btn.setCursor(Qt.PointingHandCursor)
        profile_layout = QHBoxLayout(profile_btn)
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
        user_info.addStretch()
        
        profile_layout.addWidget(avatar_label)
        profile_layout.addLayout(user_info)
        
        left_layout.addWidget(profile_btn)
        
        # Кнопки навигации
        nav_buttons = [
            ("🏠 Главная", "home"),
            ("🎮 Тесты", "tests", True),  # Активная
            ("📊 Статистика", "stats"),
            ("❓ Помощь", "help")
        ]
        
        for text, name, *active in nav_buttons:
            btn = QPushButton(text)
            btn.setObjectName(f"navBtn_{name}")
            if active and active[0]:
                btn.setProperty("active", True)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedHeight(50)
            left_layout.addWidget(btn)
        
        # Растяжка
        left_layout.addStretch()
        
        # Кнопка выхода
        logout_btn = QPushButton("🚪 Выйти из аккаунта")
        logout_btn.setObjectName("logoutBtn")
        logout_btn.setCursor(Qt.PointingHandCursor)
        logout_btn.setFixedHeight(45)
        left_layout.addWidget(logout_btn)
        
        # Версия
        version_label = QLabel("Версия 2.0.0")
        version_label.setObjectName("versionLabel")
        version_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(version_label)
        
        # ========== ПРАВАЯ ПАНЕЛЬ (КОНТЕНТ) ==========
        right_panel = QFrame()
        right_panel.setObjectName("rightPanel")
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(40, 30, 40, 30)
        right_layout.setSpacing(25)
        
        # Верхняя панель с заголовком
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        header_title = QLabel("🎮 Выбор теста на реакцию")
        header_title.setObjectName("headerTitle")
        
        header_subtitle = QLabel("Выберите режим и сложность")
        header_subtitle.setObjectName("headerSubtitle")
        
        header_layout.addWidget(header_title)
        header_layout.addStretch()
        header_layout.addWidget(header_subtitle)
        
        right_layout.addWidget(header_frame)
        
        # ========== ОСНОВНОЙ КОНТЕНТ ==========
        content_frame = QFrame()
        content_frame.setObjectName("contentFrame")
        content_layout = QVBoxLayout(content_frame)
        content_layout.setSpacing(30)
        
        # === БЛОК 1: ТИП ТЕСТА ===
        test_type_frame = QFrame()
        test_type_frame.setObjectName("testTypeFrame")
        test_type_layout = QVBoxLayout(test_type_frame)
        test_type_layout.setSpacing(20)
        
        type_title = QLabel("1. Выберите тип теста")
        type_title.setObjectName("sectionTitle")
        test_type_layout.addWidget(type_title)
        
        # Карточки типов тестов
        types_grid = QHBoxLayout()
        types_grid.setSpacing(20)
        
        test_types = [
            {
                "icon": "⚡",
                "name": "Классический",
                "desc": "Стандартный тест на время реакции",
                "color": "#005cb3"
            },
            {
                "icon": "🎯",
                "name": "На точность",
                "desc": "Попади в цель как можно точнее",
                "color": "#4CAF50"
            },
            {
                "icon": "🔄",
                "name": "Последовательный",
                "desc": "Серия из 5 быстрых нажатий",
                "color": "#FF9800"
            },
            {
                "icon": "🧠",
                "name": "Сложный выбор",
                "desc": "Реагируй только на определенные сигналы",
                "color": "#9C27B0"
            }
        ]
        
        self.type_buttons = []
        for test in test_types:
            type_card = QPushButton()
            type_card.setObjectName("testTypeCard")
            type_card.setCursor(Qt.PointingHandCursor)
            type_card.setFixedHeight(160)
            
            card_layout = QVBoxLayout(type_card)
            card_layout.setSpacing(10)
            
            icon_label = QLabel(test["icon"])
            icon_label.setObjectName("testTypeIcon")
            icon_label.setAlignment(Qt.AlignCenter)
            
            name_label = QLabel(test["name"])
            name_label.setObjectName("testTypeName")
            name_label.setAlignment(Qt.AlignCenter)
            
            desc_label = QLabel(test["desc"])
            desc_label.setObjectName("testTypeDesc")
            desc_label.setAlignment(Qt.AlignCenter)
            desc_label.setWordWrap(True)
            
            card_layout.addWidget(icon_label)
            card_layout.addWidget(name_label)
            card_layout.addWidget(desc_label)
            card_layout.addStretch()
            
            # Сохраняем цвет для использования в стилях
            type_card.setProperty("cardColor", test["color"])
            self.type_buttons.append(type_card)
            types_grid.addWidget(type_card)
        
        test_type_layout.addLayout(types_grid)
        content_layout.addWidget(test_type_frame)
        
        # === БЛОК 2: СЛОЖНОСТЬ ===
        difficulty_frame = QFrame()
        difficulty_frame.setObjectName("difficultyFrame")
        difficulty_layout = QVBoxLayout(difficulty_frame)
        difficulty_layout.setSpacing(20)
        
        diff_title = QLabel("2. Выберите уровень сложности")
        diff_title.setObjectName("sectionTitle")
        difficulty_layout.addWidget(diff_title)
        
        # Карточки сложности
        diff_cards_layout = QHBoxLayout()
        diff_cards_layout.setSpacing(20)
        
        difficulties = [
            {
                "level": "Новичок",
                "desc": "Для первого знакомства",
                "time": "До 300 мс",
                "attempts": "3 попытки",
                "color": "#4CAF50",
                "icon": "🌱"
            },
            {
                "level": "Любитель",
                "desc": "Для опытных пользователей",
                "time": "До 250 мс",
                "attempts": "5 попыток",
                "color": "#FF9800",
                "icon": "⚡"
            },
            {
                "level": "Профессионал",
                "desc": "Для настоящих киберспортсменов",
                "time": "До 200 мс",
                "attempts": "7 попыток",
                "color": "#F44336",
                "icon": "🔥"
            },
            {
                "level": "Экстра",
                "desc": "Случайные параметры",
                "time": "Адаптивный",
                "attempts": "Без ограничений",
                "color": "#9C27B0",
                "icon": "🌟"
            }
        ]
        
        self.diff_buttons = []
        for diff in difficulties:
            diff_card = QPushButton()
            diff_card.setObjectName("difficultyCard")
            diff_card.setCursor(Qt.PointingHandCursor)
            diff_card.setFixedHeight(200)
            
            card_layout = QVBoxLayout(diff_card)
            card_layout.setSpacing(8)
            
            # Верхняя часть с иконкой и уровнем
            header_layout = QHBoxLayout()
            icon_label = QLabel(diff["icon"])
            icon_label.setObjectName("difficultyIcon")
            
            level_label = QLabel(diff["level"])
            level_label.setObjectName("difficultyLevel")
            
            header_layout.addWidget(icon_label)
            header_layout.addWidget(level_label)
            header_layout.addStretch()
            
            card_layout.addLayout(header_layout)
            
            # Описание
            desc_label = QLabel(diff["desc"])
            desc_label.setObjectName("difficultyDesc")
            desc_label.setWordWrap(True)
            card_layout.addWidget(desc_label)
            
            # Характеристики
            time_label = QLabel(f"⏱️ {diff['time']}")
            time_label.setObjectName("difficultyFeature")
            
            attempts_label = QLabel(f"🎯 {diff['attempts']}")
            attempts_label.setObjectName("difficultyFeature")
            
            card_layout.addWidget(time_label)
            card_layout.addWidget(attempts_label)
            card_layout.addStretch()
            
            # Сохраняем цвет
            diff_card.setProperty("diffColor", diff["color"])
            self.diff_buttons.append(diff_card)
            diff_cards_layout.addWidget(diff_card)
        
        difficulty_layout.addLayout(diff_cards_layout)
        content_layout.addWidget(difficulty_frame)
        
        # === БЛОК 3: ДОПОЛНИТЕЛЬНЫЕ НАСТРОЙКИ ===
        options_frame = QFrame()
        options_frame.setObjectName("optionsFrame")
        options_layout = QVBoxLayout(options_frame)
        options_layout.setSpacing(15)
        
        options_title = QLabel("3. Дополнительные настройки (опционально)")
        options_title.setObjectName("sectionTitle")
        options_layout.addWidget(options_title)
        
        # Сетка дополнительных опций
        options_grid = QGridLayout()
        options_grid.setSpacing(15)
        
        options = [
            ("Звуковые сигналы", "Вкл", "🔊"),
            ("Визуальные подсказки", "Вкл", "👁️"),
            ("Сохранять результаты", "Да", "💾"),
            ("Соревновательный режим", "Нет", "🏆"),
            ("Тренировочный режим", "Нет", "📝"),
            ("Автоматическое повторение", "Нет", "🔄")
        ]
        
        for i, (option, state, icon) in enumerate(options):
            row, col = i // 2, i % 2
            option_widget = QFrame()
            option_widget.setObjectName("optionWidget")
            option_layout = QHBoxLayout(option_widget)
            option_layout.setContentsMargins(15, 10, 15, 10)
            
            icon_label = QLabel(icon)
            icon_label.setObjectName("optionIcon")
            
            text_label = QLabel(option)
            text_label.setObjectName("optionText")
            
            state_btn = QPushButton(state)
            state_btn.setObjectName("optionState")
            state_btn.setCursor(Qt.PointingHandCursor)
            state_btn.setFixedSize(60, 30)
            
            option_layout.addWidget(icon_label)
            option_layout.addWidget(text_label)
            option_layout.addStretch()
            option_layout.addWidget(state_btn)
            
            options_grid.addWidget(option_widget, row, col)
        
        options_layout.addLayout(options_grid)
        content_layout.addWidget(options_frame)
        
        # === КНОПКИ ДЕЙСТВИЙ ===
        actions_frame = QFrame()
        actions_frame.setObjectName("actionsFrame")
        actions_layout = QHBoxLayout(actions_frame)
        actions_layout.setSpacing(20)
        
        # Кнопка "Начать тест"
        self.start_btn = QPushButton("🚀 НАЧАТЬ ТЕСТ")
        self.start_btn.setObjectName("startTestBtn")
        self.start_btn.setCursor(Qt.PointingHandCursor)
        self.start_btn.setFixedHeight(70)
        
        # Кнопка "Назад"
        self.back_btn = QPushButton("← Назад")
        self.back_btn.setObjectName("backBtn")
        self.back_btn.setCursor(Qt.PointingHandCursor)
        self.back_btn.setFixedHeight(70)
        self.back_btn.setFixedWidth(150)
        
        actions_layout.addWidget(self.back_btn)
        actions_layout.addWidget(self.start_btn, 1)
        
        content_layout.addWidget(actions_frame)
        
        right_layout.addWidget(content_frame)
        
        # Добавляем панели в главный layout
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel, 1)
        
        # Подключаем сигналы
        for btn in self.type_buttons:
            btn.clicked.connect(lambda checked, b=btn: self.select_test_type(b))
        
        for btn in self.diff_buttons:
            btn.clicked.connect(lambda checked, b=btn: self.select_difficulty(b))
    
    def select_test_type(self, selected_btn):
        # Снимаем выделение со всех кнопок
        for btn in self.type_buttons:
            btn.setProperty("selected", False)
            btn.style().polish(btn)
        
        # Выделяем выбранную
        selected_btn.setProperty("selected", True)
        selected_btn.style().polish(btn)
    
    def select_difficulty(self, selected_btn):
        # Снимаем выделение со всех кнопок
        for btn in self.diff_buttons:
            btn.setProperty("selected", False)
            btn.style().polish(btn)
        
        # Выделяем выбранную
        selected_btn.setProperty("selected", True)
        selected_btn.style().polish(btn)
    
    def apply_styles(self):
        primary_color = "#005cb3"
        white_color = "#ffffff"
        light_bg = "#f8fafc"
        dark_bg = "#1e293b"
        border_color = "#e2e8f0"
        
        self.setStyleSheet(f"""
            QMainWindow, QWidget {{
                background-color: {light_bg};
                font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            }}
            
            /* Левая панель */
            #leftPanel {{
                background-color: {white_color};
                border-right: 1px solid {border_color};
            }}
            
            #logoLabel {{
                font-size: 20px;
                font-weight: 700;
                color: {primary_color};
                padding: 20px 0;
                letter-spacing: 1px;
            }}
            
            #navSeparator {{
                background-color: {border_color};
                margin: 10px 0 20px 0;
            }}
            
            #profileBtn {{
                background-color: #f1f5f9;
                border: none;
                border-radius: 16px;
                text-align: left;
                padding: 0;
                margin-bottom: 20px;
            }}
            
            #profileBtn:hover {{
                background-color: #e2e8f0;
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
                color: #64748b;
            }}
            
            #navBtn_home, #navBtn_tests, #navBtn_stats, #navBtn_help {{
                background-color: transparent;
                color: {dark_bg};
                border: none;
                border-radius: 12px;
                font-size: 15px;
                font-weight: 500;
                text-align: left;
                padding-left: 20px;
                margin: 2px 0;
            }}
            
            #navBtn_home:hover, #navBtn_tests:hover, #navBtn_stats:hover, #navBtn_help:hover {{
                background-color: #f1f5f9;
            }}
            
            #navBtn_tests[active="true"] {{
                background-color: {primary_color};
                color: white;
            }}
            
            #logoutBtn {{
                background-color: transparent;
                color: #ef4444;
                border: 1px solid #ef4444;
                border-radius: 12px;
                font-size: 14px;
                font-weight: 500;
                margin-top: 10px;
            }}
            
            #logoutBtn:hover {{
                background-color: #ef4444;
                color: white;
            }}
            
            #versionLabel {{
                font-size: 12px;
                color: #94a3b8;
                margin-top: 15px;
            }}
            
            /* Правая панель */
            #rightPanel {{
                background-color: {light_bg};
            }}
            
            #headerFrame {{
                margin-bottom: 10px;
            }}
            
            #headerTitle {{
                font-size: 28px;
                font-weight: 700;
                color: {dark_bg};
            }}
            
            #headerSubtitle {{
                font-size: 16px;
                color: #64748b;
            }}
            
            /* Общие стили для секций */
            #testTypeFrame, #difficultyFrame, #optionsFrame {{
                background-color: white;
                border-radius: 24px;
                padding: 25px;
                border: 1px solid {border_color};
            }}
            
            #sectionTitle {{
                font-size: 20px;
                font-weight: 600;
                color: {dark_bg};
                margin-bottom: 5px;
            }}
            
            /* Карточки типов тестов */
            #testTypeCard {{
                background-color: white;
                border: 2px solid {border_color};
                border-radius: 20px;
                padding: 15px;
                min-width: 180px;
            }}
            
            #testTypeCard:hover {{
                border: 2px solid {primary_color};
                transform: translateY(-2px);
            }}
            
            #testTypeCard[selected="true"] {{
                border: 3px solid {primary_color};
                background-color: #f0f7ff;
            }}
            
            #testTypeIcon {{
                font-size: 40px;
                margin-bottom: 10px;
            }}
            
            #testTypeName {{
                font-size: 18px;
                font-weight: 600;
                color: {dark_bg};
            }}
            
            #testTypeDesc {{
                font-size: 13px;
                color: #64748b;
                margin-top: 5px;
            }}
            
            /* Карточки сложности */
            #difficultyCard {{
                background-color: white;
                border: 2px solid {border_color};
                border-radius: 20px;
                padding: 20px;
                min-width: 200px;
            }}
            
            #difficultyCard:hover {{
                border: 2px solid {primary_color};
                transform: translateY(-2px);
            }}
            
            #difficultyCard[selected="true"] {{
                border: 3px solid {primary_color};
                background-color: #f0f7ff;
            }}
            
            #difficultyIcon {{
                font-size: 24px;
                margin-right: 10px;
            }}
            
            #difficultyLevel {{
                font-size: 18px;
                font-weight: 700;
            }}
            
            #difficultyDesc {{
                font-size: 13px;
                color: #64748b;
                margin: 10px 0;
            }}
            
            #difficultyFeature {{
                font-size: 13px;
                color: {dark_bg};
                margin: 3px 0;
            }}
            
            /* Опции */
            #optionWidget {{
                background-color: #f8fafc;
                border-radius: 12px;
                border: 1px solid {border_color};
            }}
            
            #optionIcon {{
                font-size: 18px;
                margin-right: 10px;
            }}
            
            #optionText {{
                font-size: 14px;
                color: {dark_bg};
            }}
            
            #optionState {{
                background-color: white;
                border: 1px solid {border_color};
                border-radius: 8px;
                font-size: 12px;
                font-weight: 500;
                color: {dark_bg};
            }}
            
            #optionState:hover {{
                background-color: {primary_color};
                color: white;
                border: 1px solid {primary_color};
            }}
            
            /* Кнопки действий */
            #actionsFrame {{
                margin-top: 20px;
            }}
            
            #startTestBtn {{
                background-color: {primary_color};
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 24px;
                font-weight: 700;
                letter-spacing: 1px;
            }}
            
            #startTestBtn:hover {{
                background-color: #004799;
            }}
            
            #backBtn {{
                background-color: white;
                color: {dark_bg};
                border: 2px solid {border_color};
                border-radius: 20px;
                font-size: 18px;
                font-weight: 600;
            }}
            
            #backBtn:hover {{
                background-color: #f1f5f9;
                border: 2px solid {primary_color};
            }}
        """)

class TestInProgressWindow(QMainWindow):
    """Окно самого теста (для демонстрации перехода)"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reaction Test - Тест")
        self.setMinimumSize(1200, 700)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        
        test_label = QLabel("⚡ ТЕСТ НА РЕАКЦИЮ ⚡")
        test_label.setStyleSheet("""
            font-size: 48px;
            font-weight: bold;
            color: #005cb3;
            margin-bottom: 50px;
        """)
        test_label.setAlignment(Qt.AlignCenter)
        
        wait_label = QLabel("Ждите сигнала...")
        wait_label.setStyleSheet("""
            font-size: 24px;
            color: #64748b;
            margin-bottom: 30px;
        """)
        wait_label.setAlignment(Qt.AlignCenter)
        
        progress_label = QLabel("⚪ ⚪ ⚪")
        progress_label.setStyleSheet("""
            font-size: 32px;
            color: #e2e8f0;
            letter-spacing: 10px;
        """)
        progress_label.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(test_label)
        layout.addWidget(wait_label)
        layout.addWidget(progress_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    window = TestSelectionWindow()
    window.show()
    
    # Для демонстрации окна теста:
    # test_window = TestInProgressWindow()
    # test_window.show()
    
    sys.exit(app.exec())