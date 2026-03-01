import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QVBoxLayout, QWidget, QLabel, QSpinBox
from PySide6.QtCore import QObject, QTimer, Signal, QPointF, QRectF
from PySide6.QtGui import QColor, QBrush, QPen

class BallScene(QGraphicsScene):
    """
    Кастомная сцена для обработки нажатий мыши.
    Сообщает контроллеру, куда был сделан клик.
    """
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setBackgroundBrush(QColor("#f0f0f0"))

    def mousePressEvent(self, event):
        # Получаем позицию клика в координатах сцены
        scene_pos = event.scenePos()
        
        # Проверяем, есть ли объект в этой точке
        # itemAt требует трансформацию вида, но мы можем получить список элементов
        items = self.items(scene_pos)
        
        # Ищем наш шарик в списке элементов под курсором
        ball_clicked = False
        for item in items:
            if item == self.controller.ball_item:
                ball_clicked = True
                break
        
        if ball_clicked:
            self.controller.ball_clicked.emit(scene_pos)
        else:
            self.controller.background_clicked.emit(scene_pos)
            
        # Вызываем базовый обработчик, чтобы события шли дальше при необходимости
        super().mousePressEvent(event)

class FlyingBallController(QObject):
    """
    Класс-контроллер, который принимает QGraphicsView и управляет шариком.
    """
    # Сигналы
    ball_clicked = Signal(QPointF)       # Сигнал при клике на шарик (координаты сцены)
    background_clicked = Signal(QPointF) # Сигнал при клике на фон (координаты сцены)

    def __init__(self, view: QGraphicsView):
        super().__init__()
        self.view = view
        
        # Создаем сцену
        self.scene = BallScene(self)
        self.view.setScene(self.scene)
        
        # Устанавливаем размер сцены (например, 800x600)
        self.scene.setSceneRect(0, 0, 800, 600)
        
        # Создаем шарик
        self.ball_size = 40
        self.ball_item = QGraphicsEllipseItem(0, 0, self.ball_size, self.ball_size)
        self.ball_item.setBrush(QBrush(QColor("red")))
        self.ball_item.setPen(QPen(QColor("darkred"), 2))
        # self.ball_item.setFlags(self.ball_item.ItemIsMovable) # Можно включить, если нужно таскать мышкой
        self.scene.addItem(self.ball_item)
        
        # Начальная позиция
        self.pos_x = 100
        self.pos_y = 100
        self.ball_item.setPos(self.pos_x, self.pos_y)
        
        # Параметры движения
        self.dx = 3.0  # Скорость по X
        self.dy = 3.0  # Скорость по Y
        
        # Таймер анимации
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_position)
        self.timer.start(16) # ~60 FPS
        
        # Флаг активности
        self.is_active = True

    def set_Size(self,data:list):
        self.scene.setSceneRect(data[0], data[1], data[2], data[3])

    def set_speed(self, multiplier: float):
        """
        Настройка скорости полета.
        :param multiplier: Множитель скорости (1.0 - норм, 2.0 - в 2 раза быстрее)
        """
        base_speed = 3.0
        # Сохраняем направление, меняем только модуль вектора
        sign_x = 1 if self.dx >= 0 else -1
        sign_y = 1 if self.dy >= 0 else -1
        
        self.dx = base_speed * multiplier * sign_x
        self.dy = base_speed * multiplier * sign_y

    def set_timer_interval(self, ms: int):
        """
        Настройка плавности/частоты обновления (в миллисекундах).
        Меньше значение = плавнее, но больше нагрузка.
        """
        self.timer.setInterval(ms)

    def _update_position(self):
        if not self.is_active:
            return

        # Текущие координаты
        x = self.ball_item.x()
        y = self.ball_item.y()
        
        # Предсказываем следующую позицию
        next_x = x + self.dx
        next_y = y + self.dy
        
        # Границы сцены
        rect = self.scene.sceneRect()
        radius = self.ball_size / 2
        
        # Отскок от стен (простая физика)
        if next_x <= rect.left() or next_x + self.ball_size >= rect.right():
            self.dx = -self.dx
            next_x = x + self.dx # Корректируем, чтобы не застрял в стене
            
        if next_y <= rect.top() or next_y + self.ball_size >= rect.bottom():
            self.dy = -self.dy
            next_y = y + self.dy
            
        self.ball_item.setPos(next_x, next_y)

    def stop(self):
        self.timer.stop()
        self.is_active = False

    def start(self):
        self.timer.start()
        self.is_active = True

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Летающий шарик PySide6")
        self.resize(1000, 700)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Панель управления
        control_layout = QVBoxLayout()
        
        self.speed_label = QLabel("Скорость (множитель): 1.0")
        self.speed_spin = QSpinBox()
        self.speed_spin.setRange(1, 20)
        self.speed_spin.setValue(1)
        self.speed_spin.valueChanged.connect(self.on_speed_changed)
        
        control_layout.addWidget(self.speed_label)
        control_layout.addWidget(self.speed_spin)
        
        self.status_label = QLabel("Кликните на шарик или фон")
        self.status_label.setStyleSheet("color: blue; font-weight: bold;")
        control_layout.addWidget(self.status_label)

        # QGraphicsView
        self.view = QGraphicsView()
        self.view.setDragMode(QGraphicsView.NoDrag) # Отключаем перетаскивание сцены
        
        layout.addLayout(control_layout)
        layout.addWidget(self.view)

        # Инициализация контроллера шарика
        self.ball_controller = FlyingBallController(self.view)
        
        # Подключение сигналов контроллера к слотам главного окна
        self.ball_controller.ball_clicked.connect(self.on_ball_click)
        self.ball_controller.background_clicked.connect(self.on_background_click)

    def on_speed_changed(self, value):
        # Делим на 2, чтобы значения 1-20 давали более плавный диапазон скорости
        speed = value / 2.0 
        self.ball_controller.set_speed(speed)
        self.speed_label.setText(f"Скорость (множитель): {speed}")

    def on_ball_click(self, pos: QPointF):
        self.status_label.setText(f"Клик по ШАРИКУ в точке: ({pos.x():.1f}, {pos.y():.1f})")
        # Меняем цвет шарика при клике для наглядности
        self.ball_controller.ball_item.setBrush(QBrush(QColor("orange")))

    def on_background_click(self, pos: QPointF):
        self.status_label.setText(f"Клик по ФОНУ в точке: ({pos.x():.1f}, {pos.y():.1f})")
        # Возвращаем цвет
        self.ball_controller.ball_item.setBrush(QBrush(QColor("red")))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())