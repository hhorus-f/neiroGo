import sys
import random
import math
from PySide6.QtWidgets import (QApplication, QMainWindow, QGraphicsView, 
                               QGraphicsScene, QGraphicsEllipseItem, QWidget,
                               QVBoxLayout, QHBoxLayout, QSlider, QLabel, QPushButton)
from PySide6.QtCore import Qt, QTimer, QPointF, Signal, QObject
from PySide6.QtGui import QBrush, QColor, QPainter, QPen


class FlyingBall(QGraphicsEllipseItem):
    """Класс летающего шарика с сигналами"""
    
    # Сигналы должны быть определены на уровне класса
    ball_clicked = Signal(object, float, float)  # шарик, x, y
    ball_released = Signal(object, float, float)  # шарик, x, y
    ball_hit_wall = Signal(object, str)  # шарик, стена (left, right, top, bottom)
    
    def __init__(self, x, y, radius, speed=5):
        super().__init__(x - radius, y - radius, radius * 2, radius * 2)
        
        self.radius = radius
        self.speed = speed
        
        # Начальное направление движения (случайное)
        angle = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
        # Настройка внешнего вида
        self.normal_color = QColor(255, 100, 100)
        self.clicked_color = QColor(100, 255, 100)
        self.setBrush(QBrush(self.normal_color))
        self.setPen(QPen(Qt.GlobalColor.black, 2))
        
        # Флаги состояния
        self.is_clicked = False
        self.is_moving = True
        self.is_visible = True
        
        # Включаем обработку событий мыши
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)
        
    def update_position(self, scene_rect):
        """Обновление позиции шарика"""
        if not self.is_moving:
            return
            
        new_pos = self.pos() + QPointF(self.vx, self.vy)
        wall_hit = False
        
        # Проверка столкновений со стенками
        if new_pos.x() - self.radius <= 0:
            self.vx = -self.vx
            new_pos.setX(self.radius)
            self.ball_hit_wall.emit(self, "left")
            wall_hit = True
            
        elif new_pos.x() + self.radius >= scene_rect.width():
            self.vx = -self.vx
            new_pos.setX(scene_rect.width() - self.radius)
            self.ball_hit_wall.emit(self, "right")
            wall_hit = True
            
        if new_pos.y() - self.radius <= 0:
            self.vy = -self.vy
            new_pos.setY(self.radius)
            self.ball_hit_wall.emit(self, "top")
            wall_hit = True
            
        elif new_pos.y() + self.radius >= scene_rect.height():
            self.vy = -self.vy
            new_pos.setY(scene_rect.height() - self.radius)
            self.ball_hit_wall.emit(self, "bottom")
            wall_hit = True
        
        self.setPos(new_pos)
    
    def set_speed(self, new_speed):
        """Изменение скорости шарика"""
        # Сохраняем направление движения
        current_vx = self.vx
        current_vy = self.vy
        current_speed = math.sqrt(current_vx**2 + current_vy**2)
        
        if current_speed > 0:
            # Масштабируем скорость с сохранением направления
            scale = new_speed / current_speed
            self.vx = current_vx * scale
            self.vy = current_vy * scale
        else:
            # Если скорость была нулевой, задаем новое направление
            angle = random.uniform(0, 2 * math.pi)
            self.vx = math.cos(angle) * new_speed
            self.vy = math.sin(angle) * new_speed
        
        self.speed = new_speed
    
    def set_direction(self, angle_degrees):
        """Установка направления движения (в градусах)"""
        angle_rad = math.radians(angle_degrees)
        current_speed = self.speed
        self.vx = math.cos(angle_rad) * current_speed
        self.vy = math.sin(angle_rad) * current_speed
    
    def reverse_direction(self):
        """Разворот шарика"""
        self.vx = -self.vx
        self.vy = -self.vy
    
    def stop(self):
        """Остановка шарика"""
        self.is_moving = False
        self.vx = 0
        self.vy = 0
    
    def start(self):
        """Запуск шарика"""
        if not self.is_moving:
            self.is_moving = True
            self.set_speed(self.speed)
    
    def set_color(self, color):
        """Установка цвета шарика"""
        self.normal_color = color
        if not self.is_clicked:
            self.setBrush(QBrush(color))
    
    def hide_ball(self):
        """Спрятать шарик"""
        self.is_visible = False
        self.setVisible(False)
    
    def show_ball(self):
        """Показать шарик"""
        self.is_visible = True
        self.setVisible(True)
    
    def mousePressEvent(self, event):
        """Обработка нажатия на шарик"""
        self.is_clicked = True
        self.setBrush(QBrush(self.clicked_color))
        pos = self.pos()
        self.ball_clicked.emit(self, pos.x(), pos.y())
        super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event):
        """Обработка отпускания шарика"""
        self.is_clicked = False
        self.setBrush(QBrush(self.normal_color))
        pos = self.pos()
        self.ball_released.emit(self, pos.x(), pos.y())
        super().mouseReleaseEvent(event)


class BallSceneManager(QObject):
    """Менеджер для управления шариком в сцене"""
    
    # Сигналы на уровне класса
    ball_clicked = Signal(object, float, float)
    ball_released = Signal(object, float, float)
    ball_hit_wall = Signal(object, str)
    background_clicked = Signal(float, float)
    
    def __init__(self, graphics_view):
        super().__init__()
        
        self.view = graphics_view
        self.scene = graphics_view.scene()
        
        if self.scene is None:
            self.scene = QGraphicsScene()
            self.view.setScene(self.scene)
        
        self.ball = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        
        # Настройка view
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # Сохраняем оригинальный обработчик
        self.original_mouse_press = self.view.mousePressEvent
        
        # Переопределяем обработчик событий view
        self.view.mousePressEvent = self.view_mouse_press
        
    def create_ball(self, x=None, y=None, radius=30, speed=5):
        """Создание шарика"""
        if x is None:
            x = self.view.width() // 2
        if y is None:
            y = self.view.height() // 2
            
        self.ball = FlyingBall(x, y, radius, speed)
        self.scene.addItem(self.ball)
        
        # Подключаем сигналы шарика к сигналам менеджера
        # Используем lambda для правильной передачи сигналов
        self.ball.ball_clicked.connect(lambda ball, x, y: self.ball_clicked.emit(ball, x, y))
        self.ball.ball_released.connect(lambda ball, x, y: self.ball_released.emit(ball, x, y))
        self.ball.ball_hit_wall.connect(lambda ball, wall: self.ball_hit_wall.emit(ball, wall))
        
        # Устанавливаем размер сцены
        self.update_scene_rect()
        
        return self.ball
    
    def update_scene_rect(self):
        """Обновление размера сцены"""
        if self.view.width() > 0 and self.view.height() > 0:
            self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())
    
    def view_mouse_press(self, event):
        """Обработка нажатий на view"""
        scene_pos = self.view.mapToScene(event.pos())
        item = self.view.itemAt(event.pos())
        
        if item is None and self.ball is not None:
            # Нажатие на фон
            self.background_clicked.emit(scene_pos.x(), scene_pos.y())
        
        # Вызываем оригинальный обработчик
        if self.original_mouse_press:
            self.original_mouse_press(event)
        else:
            QGraphicsView.mousePressEvent(self.view, event)
    
    def start_animation(self, interval_ms=20):
        """Запуск анимации"""
        self.timer.start(interval_ms)
    
    def stop_animation(self):
        """Остановка анимации"""
        self.timer.stop()
    
    def update_animation(self):
        """Обновление анимации"""
        if self.ball and self.scene.sceneRect().isValid():
            self.ball.update_position(self.scene.sceneRect())
            self.scene.update()
    
    def set_ball_speed(self, speed):
        """Установка скорости шарика"""
        if self.ball:
            self.ball.set_speed(speed)
    
    def remove_ball(self):
        """Удаление шарика"""
        if self.ball:
            self.scene.removeItem(self.ball)
            self.ball = None


# Пример использования
class ExampleWindow(QMainWindow):
    """Пример использования класса FlyingBall и BallSceneManager"""
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Пример использования FlyingBall")
        self.setGeometry(100, 100, 800, 600)
        
        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Создаем QGraphicsView
        self.view = QGraphicsView()
        layout.addWidget(self.view)
        
        # Создаем менеджер для шарика
        self.ball_manager = BallSceneManager(self.view)
        
        # Создаем шарик
        self.ball = self.ball_manager.create_ball(radius=30, speed=5)
        
        # Подключаем сигналы
        self.ball_manager.ball_clicked.connect(self.on_ball_clicked)
        self.ball_manager.ball_released.connect(self.on_ball_released)
        self.ball_manager.ball_hit_wall.connect(self.on_ball_hit_wall)
        self.ball_manager.background_clicked.connect(self.on_background_clicked)
        
        # Запускаем анимацию
        self.ball_manager.start_animation()
        
        # Создаем панель управления
        self.create_control_panel(layout)
    
    def create_control_panel(self, layout):
        """Создание панели управления"""
        control_panel = QWidget()
        control_layout = QHBoxLayout(control_panel)
        
        # Слайдер скорости
        self.speed_label = QLabel("Скорость: 5")
        control_layout.addWidget(self.speed_label)
        
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(0)
        self.speed_slider.setMaximum(20)
        self.speed_slider.setValue(5)
        self.speed_slider.valueChanged.connect(self.ball_manager.set_ball_speed)
        self.speed_slider.valueChanged.connect(lambda v: self.speed_label.setText(f"Скорость: {v}"))
        control_layout.addWidget(self.speed_slider)
        
        # Кнопка разворота
        reverse_btn = QPushButton("Развернуть")
        reverse_btn.clicked.connect(lambda: self.ball.reverse_direction() if self.ball else None)
        control_layout.addWidget(reverse_btn)
        
        layout.addWidget(control_panel)
    
    def on_ball_clicked(self, ball, x, y):
        """Обработка нажатия на шарик"""
        print(f"Шарик нажат! Позиция: ({x:.1f}, {y:.1f})")
    
    def on_ball_released(self, ball, x, y):
        """Обработка отпускания шарика"""
        print(f"Шарик отпущен! Позиция: ({x:.1f}, {y:.1f})")
    
    def on_ball_hit_wall(self, ball, wall):
        """Обработка удара о стену"""
        print(f"Шарик ударился о стену: {wall}")
    
    def on_background_clicked(self, x, y):
        """Обработка нажатия на фон"""
        print(f"Нажатие на фон в позиции ({x:.1f}, {y:.1f})")
        # Разворачиваем шарик при нажатии на фон
        if self.ball:
            self.ball.reverse_direction()
    
    def resizeEvent(self, event):
        """Обработка изменения размера окна"""
        super().resizeEvent(event)
        self.ball_manager.update_scene_rect()


def main():
    app = QApplication(sys.argv)
    window = ExampleWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()