import sys
import random
import math
from PySide6.QtWidgets import (QApplication, QMainWindow, QGraphicsView, 
                               QGraphicsScene, QGraphicsEllipseItem, QWidget,
                               QVBoxLayout, QHBoxLayout, QSlider, QLabel, QPushButton)
from PySide6.QtCore import Qt, QTimer, QPointF, Signal, QObject
from PySide6.QtGui import QBrush, QColor, QPainter, QPen


class FlyingBall(QGraphicsEllipseItem):
    """Класс летающего шарика (без сигналов)"""
    
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
        
        # Включаем обработку событий мыши
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)
        
        # Ссылка на менеджер (будет установлена позже)
        self.manager = None
        
    def set_manager(self, manager):
        """Установка ссылки на менеджер"""
        self.manager = manager
        
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
            if self.manager:
                self.manager.on_ball_hit_wall(self, "left")
            wall_hit = True
            
        elif new_pos.x() + self.radius >= scene_rect.width():
            self.vx = -self.vx
            new_pos.setX(scene_rect.width() - self.radius)
            if self.manager:
                self.manager.on_ball_hit_wall(self, "right")
            wall_hit = True
            
        if new_pos.y() - self.radius <= 0:
            self.vy = -self.vy
            new_pos.setY(self.radius)
            if self.manager:
                self.manager.on_ball_hit_wall(self, "top")
            wall_hit = True
            
        elif new_pos.y() + self.radius >= scene_rect.height():
            self.vy = -self.vy
            new_pos.setY(scene_rect.height() - self.radius)
            if self.manager:
                self.manager.on_ball_hit_wall(self, "bottom")
            wall_hit = True
        
        self.setPos(new_pos)
    
    def set_speed(self, new_speed):
        """Изменение скорости шарика"""
        current_vx = self.vx
        current_vy = self.vy
        current_speed = math.sqrt(current_vx**2 + current_vy**2)
        
        if current_speed > 0:
            scale = new_speed / current_speed
            self.vx = current_vx * scale
            self.vy = current_vy * scale
        else:
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
    
    def mousePressEvent(self, event):
        """Обработка нажатия на шарик"""
        self.is_clicked = True
        self.setBrush(QBrush(self.clicked_color))
        pos = self.pos()
        if self.manager:
            self.manager.on_ball_clicked(self, pos.x(), pos.y())
        super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event):
        """Обработка отпускания шарика"""
        self.is_clicked = False
        self.setBrush(QBrush(self.normal_color))
        pos = self.pos()
        if self.manager:
            self.manager.on_ball_released(self, pos.x(), pos.y())
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
        
        print("✓ BallSceneManager инициализирован")
        
    def create_ball(self, x=None, y=None, radius=30, speed=5):
        """Создание шарика"""
        try:
            print("\n=== Создание шарика ===")
            
            if x is None:
                x = self.view.width() // 2
            if y is None:
                y = self.view.height() // 2
            
            print(f"Позиция: ({x}, {y}), радиус: {radius}, скорость: {speed}")
            
            # Создаем шарик
            self.ball = FlyingBall(x, y, radius, speed)
            self.ball.set_manager(self)  # Устанавливаем ссылку на менеджер
            self.scene.addItem(self.ball)
            
            print("✓ Шарик создан и добавлен в сцену")
            
            # Устанавливаем размер сцены
            self.update_scene_rect()
            
            print("✓ Шарик создан успешно")
            print("========================\n")
            
            return self.ball
            
        except Exception as e:
            print(f"✗ Ошибка при создании шарика: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def on_ball_clicked(self, ball, x, y):
        """Обработка нажатия на шарик (вызывается из шарика)"""
        print(f"  → Получено нажатие на шарик в менеджере: ({x:.1f}, {y:.1f})")
        self.ball_clicked.emit(ball, x, y)
    
    def on_ball_released(self, ball, x, y):
        """Обработка отпускания шарика (вызывается из шарика)"""
        print(f"  → Получено отпускание шарика в менеджере: ({x:.1f}, {y:.1f})")
        self.ball_released.emit(ball, x, y)
    
    def on_ball_hit_wall(self, ball, wall):
        """Обработка удара о стену (вызывается из шарика)"""
        print(f"  → Получен удар о стену в менеджере: {wall}")
        self.ball_hit_wall.emit(ball, wall)
    
    def update_scene_rect(self):
        """Обновление размера сцены"""
        if self.view.width() > 0 and self.view.height() > 0:
            self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())
    
    def view_mouse_press(self, event):
        """Обработка нажатий на view"""
        try:
            scene_pos = self.view.mapToScene(event.pos())
            item = self.view.itemAt(event.pos())
            
            if item is None and self.ball is not None:
                print(f"✓ Нажатие на фон в позиции ({scene_pos.x():.1f}, {scene_pos.y():.1f})")
                self.background_clicked.emit(scene_pos.x(), scene_pos.y())
            
            # Вызываем оригинальный обработчик
            if self.original_mouse_press:
                self.original_mouse_press(event)
            else:
                QGraphicsView.mousePressEvent(self.view, event)
                
        except Exception as e:
            print(f"✗ Ошибка в view_mouse_press: {e}")
    
    def start_animation(self, interval_ms=20):
        """Запуск анимации"""
        self.timer.start(interval_ms)
        print("✓ Анимация запущена")
    
    def stop_animation(self):
        """Остановка анимации"""
        self.timer.stop()
        print("✓ Анимация остановлена")
    
    def update_animation(self):
        """Обновление анимации"""
        try:
            if self.ball and self.scene.sceneRect().isValid():
                self.ball.update_position(self.scene.sceneRect())
                self.scene.update()
        except Exception as e:
            print(f"✗ Ошибка в update_animation: {e}")
    
    def set_ball_speed(self, speed):
        """Установка скорости шарика"""
        if self.ball:
            self.ball.set_speed(speed)
            print(f"✓ Скорость изменена на {speed}")
    
    def remove_ball(self):
        """Удаление шарика"""
        if self.ball:
            self.scene.removeItem(self.ball)
            self.ball = None
            print("✓ Шарик удален")


# Пример использования
class ExampleWindow(QMainWindow):
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
        control_panel = QWidget()
        control_layout = QHBoxLayout(control_panel)
        
        self.speed_label = QLabel("Скорость: 5")
        control_layout.addWidget(self.speed_label)
        
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(0)
        self.speed_slider.setMaximum(20)
        self.speed_slider.setValue(5)
        self.speed_slider.valueChanged.connect(self.ball_manager.set_ball_speed)
        self.speed_slider.valueChanged.connect(lambda v: self.speed_label.setText(f"Скорость: {v}"))
        control_layout.addWidget(self.speed_slider)
        
        reverse_btn = QPushButton("Развернуть")
        reverse_btn.clicked.connect(lambda: self.ball.reverse_direction() if self.ball else None)
        control_layout.addWidget(reverse_btn)
        
        layout.addWidget(control_panel)
    
    def on_ball_clicked(self, ball, x, y):
        print(f"✓ СИГНАЛ: Шарик нажат! Позиция: ({x:.1f}, {y:.1f})")
    
    def on_ball_released(self, ball, x, y):
        print(f"✓ СИГНАЛ: Шарик отпущен! Позиция: ({x:.1f}, {y:.1f})")
    
    def on_ball_hit_wall(self, ball, wall):
        print(f"✓ СИГНАЛ: Шарик ударился о стену: {wall}")
    
    def on_background_clicked(self, x, y):
        print(f"✓ СИГНАЛ: Нажатие на фон в позиции ({x:.1f}, {y:.1f})")
        if self.ball:
            self.ball.reverse_direction()
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.ball_manager.update_scene_rect()


def main():
    app = QApplication(sys.argv)
    window = ExampleWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()