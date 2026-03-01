import sys
import random
import math
from PySide6.QtWidgets import (QApplication, QMainWindow, QGraphicsView, 
                               QGraphicsScene, QGraphicsEllipseItem, QWidget,
                               QVBoxLayout, QHBoxLayout, QSlider, QLabel)
from PySide6.QtCore import Qt, QTimer, QRectF, QPointF
from PySide6.QtGui import QBrush, QColor, QPainter, QPen

class Ball(QGraphicsEllipseItem):
    """Класс летающего шарика"""
    
    def __init__(self, x, y, radius, speed):
        super().__init__(x - radius, y - radius, radius * 2, radius * 2)
        
        self.radius = radius
        self.speed = speed
        
        # Начальное направление движения (случайное)
        angle = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
        # Настройка внешнего вида
        self.setBrush(QBrush(QColor(255, 100, 100)))
        self.setPen(QPen(Qt.GlobalColor.black, 2))
        
        # Флаг для отслеживания нажатия на шарик
        self.is_clicked = False
        
        # Включаем обработку событий мыши
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)
        
    def update_position(self, scene_rect):
        """Обновление позиции шарика"""
        new_pos = self.pos() + QPointF(self.vx, self.vy)
        
        # Проверка столкновений со стенками
        if new_pos.x() - self.radius <= 0 or new_pos.x() + self.radius >= scene_rect.width():
            self.vx = -self.vx
            new_pos.setX(max(self.radius, min(new_pos.x(), scene_rect.width() - self.radius)))
            
        if new_pos.y() - self.radius <= 0 or new_pos.y() + self.radius >= scene_rect.height():
            self.vy = -self.vy
            new_pos.setY(max(self.radius, min(new_pos.y(), scene_rect.height() - self.radius)))
        
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
    
    def mousePressEvent(self, event):
        """Обработка нажатия на шарик"""
        self.is_clicked = True
        self.setBrush(QBrush(QColor(100, 255, 100)))  # Меняем цвет при нажатии
        print(f"Шарик нажат! Позиция: ({self.pos().x():.1f}, {self.pos().y():.1f})")
        super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event):
        """Обработка отпускания шарика"""
        self.is_clicked = False
        self.setBrush(QBrush(QColor(255, 100, 100)))  # Возвращаем исходный цвет
        print("Шарик отпущен!")
        super().mouseReleaseEvent(event)


class GraphicsView(QGraphicsView):
    """Кастомное представление для обработки нажатий"""
    
    def __init__(self, scene, ball):
        super().__init__(scene)
        self.ball = ball
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
    def mousePressEvent(self, event):
        """Обработка нажатий мыши"""
        # Преобразуем координаты нажатия в координаты сцены
        scene_pos = self.mapToScene(event.pos())
        
        # Проверяем, было ли нажатие на шарик
        item = self.itemAt(event.pos())
        
        if item is None:
            # Нажатие мимо шарика
            print(f"Нажатие мимо шарика в позиции ({scene_pos.x():.1f}, {scene_pos.y():.1f})")
            # Меняем направление шарика
            self.ball.vx = -self.ball.vx
            self.ball.vy = -self.ball.vy
        
        super().mousePressEvent(event)


class MainWindow(QMainWindow):
    """Главное окно приложения"""
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Летающий шарик")
        self.setGeometry(100, 100, 800, 600)
        
        # Создаем центральный виджет с вертикальным расположением
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Создаем сцену
        self.scene = QGraphicsScene()
        
        # Параметры шарика
        self.ball_radius = 25
        initial_speed = 6
        
        # Создаем шарик в центре сцены
        self.ball = Ball(400, 300, self.ball_radius, initial_speed)
        self.scene.addItem(self.ball)
        
        # Создаем вид с шариком
        self.view = GraphicsView(self.scene, self.ball)
        layout.addWidget(self.view)
        
        # Создаем панель управления скоростью
        control_panel = QWidget()
        control_layout = QHBoxLayout(control_panel)
        
        # Метка для отображения текущей скорости
        self.speed_label = QLabel(f"Скорость: {initial_speed}")
        control_layout.addWidget(self.speed_label)
        
        # Слайдер для регулировки скорости
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(20)
        self.speed_slider.setValue(initial_speed)
        self.speed_slider.valueChanged.connect(self.change_speed)
        control_layout.addWidget(self.speed_slider)
        
        layout.addWidget(control_panel)
        
        # Таймер для анимации
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(20)  # 50 кадров в секунду
        
    def resizeEvent(self, event):
        """Обработка изменения размера окна"""
        super().resizeEvent(event)
        # Устанавливаем размер сцены равным размеру view
        if self.view.width() > 0 and self.view.height() > 0:
            self.scene.setSceneRect(0, 0, self.view.width(), self.view.height())
        
    def update_animation(self):
        """Обновление анимации"""
        if self.scene.sceneRect().isValid():
            self.ball.update_position(self.scene.sceneRect())
            self.scene.update()
    
    def change_speed(self, value):
        """Изменение скорости шарика"""
        self.ball.set_speed(value)
        self.speed_label.setText(f"Скорость: {value}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()