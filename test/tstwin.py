import sys
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QGraphicsView, 
    QGraphicsScene, QGraphicsItem, QGraphicsObject
)
from PySide6.QtCore import Qt, QRectF, QPointF, QPropertyAnimation, Property, QEasingCurve, Signal
from PySide6.QtGui import QPainter, QBrush, QColor, QPen, QFont, QPainterPath


class AnimatedGraphicsButton(QGraphicsObject):
    """Графический объект кнопки с анимацией"""
    
    clicked = Signal()
    
    def __init__(self):
        super().__init__()
        
        # Свойства для анимации
        self._opacity = 1.0
        self._color = QColor(69, 183, 209)  # Синий
        self._hovered = False
        self._pressed = False
        
        # Создаем анимации
        self.position_animation = QPropertyAnimation(self, b"pos")
        self.position_animation.setDuration(3000)
        self.position_animation.setLoopCount(-1)  # Бесконечно
        self.position_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        
        self.opacity_animation = QPropertyAnimation(self, b"opacity")
        self.opacity_animation.setDuration(2000)
        self.opacity_animation.setLoopCount(-1)
        self.opacity_animation.setKeyValueAt(0, 1.0)
        self.opacity_animation.setKeyValueAt(0.5, 0.3)
        self.opacity_animation.setKeyValueAt(1, 1.0)
        
        # Включаем прием событий мыши
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        
    def boundingRect(self):
        """Определяем границы объекта"""
        return QRectF(-60, -60, 120, 120)
    
    def shape(self):
        """Определяем форму для точного определения попадания"""
        path = QPainterPath()
        path.addEllipse(self.boundingRect())
        return path
    
    def paint(self, painter, option, widget=None):
        """Отрисовка объекта"""
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Определяем цвет в зависимости от состояния
        if self._pressed:
            color = QColor(255, 107, 107)  # Красный
            shadow_color = QColor(255, 0, 0)
        elif self._hovered:
            color = QColor(78, 205, 196)   # Бирюзовый
            shadow_color = QColor(78, 205, 196)
        else:
            color = self._color
            shadow_color = QColor(69, 183, 209)
        
        # Рисуем тень
        painter.setBrush(QBrush(shadow_color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setOpacity(self._opacity * 0.5)
        painter.drawEllipse(QRectF(-55, -55, 110, 110))
        
        # Рисуем основную фигуру (звезда)
        painter.setBrush(QBrush(color))
        painter.setOpacity(self._opacity)
        
        # Создаем путь для звезды
        path = QPainterPath()
        center = QPointF(0, 0)
        
        # Рисуем звезду
        points = []
        for i in range(5):
            # Внешние точки
            angle = -90 + i * 72
            outer_x = 50 * self._cos(angle)
            outer_y = 50 * self._sin(angle)
            
            # Внутренние точки
            inner_angle = angle + 36
            inner_x = 25 * self._cos(inner_angle)
            inner_y = 25 * self._sin(inner_angle)
            
            points.append(QPointF(outer_x, outer_y))
            points.append(QPointF(inner_x, inner_y))
        
        # Строим путь
        path.moveTo(points[0])
        for point in points[1:]:
            path.lineTo(point)
        path.closeSubpath()
        
        painter.drawPath(path)
        
        # Рисуем текст
        painter.setOpacity(self._opacity)
        painter.setPen(QPen(Qt.GlobalColor.white, 2))
        painter.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        painter.drawText(self.boundingRect(), Qt.AlignmentFlag.AlignCenter, "Click")
    
    def _cos(self, degrees):
        """Косинус в градусах"""
        import math
        return math.cos(math.radians(degrees))
    
    def _sin(self, degrees):
        """Синус в градусах"""
        import math
        return math.sin(math.radians(degrees))
    
    # Свойства для анимации
    def get_opacity(self):
        return self._opacity
    
    def set_opacity(self, value):
        self._opacity = value
        self.update()
    
    opacity = Property(float, get_opacity, set_opacity)
    
    # Обработчики событий мыши
    def hoverEnterEvent(self, event):
        self._hovered = True
        self.update()
        super().hoverEnterEvent(event)
    
    def hoverLeaveEvent(self, event):
        self._hovered = False
        self.update()
        super().hoverLeaveEvent(event)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._pressed = True
            self.update()
        super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._pressed = False
            self.update()
            
            # Проверяем, что отпустили внутри фигуры
            if self.contains(event.pos()):
                self.clicked.emit()
                print("Кнопка нажата!")  # Замените на нужное действие
        super().mouseReleaseEvent(event)
    
    def start_animations(self, scene_rect):
        """Запуск анимаций движения и прозрачности"""
        # Анимация движения
        self.position_animation.setStartValue(QPointF(50, 50))
        self.position_animation.setEndValue(
            QPointF(scene_rect.width() - 150, scene_rect.height() - 150)
        )
        self.position_animation.start()
        
        # Анимация прозрачности
        self.opacity_animation.start()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анимированная кнопка")
        self.setGeometry(100, 100, 800, 600)
        
        # Создаем сцену и вид
        self.scene = QGraphicsScene(0, 0, 780, 580)
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.view.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        self.view.setFrameStyle(0)
        self.setCentralWidget(self.view)
        
        # Создаем несколько кнопок
        for i in range(3):
            button = AnimatedGraphicsButton()
            button.setPos(random.randint(50, 300), random.randint(50, 300))
            button.clicked.connect(lambda i=i: print(f"Кнопка {i+1} нажата!"))
            self.scene.addItem(button)
            button.start_animations(self.scene.sceneRect())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())