# graph_widget.py - исправленная версия

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy
from PySide6.QtCore import Qt, QRect, QRectF
from PySide6.QtGui import QPainter, QPen, QColor, QBrush, QFont, QPainterPath
import numpy as np


class SplitGraphWidget(QWidget):
    """
    Виджет для отображения двух графиков в разделенных областях.
    Адаптирован для встраивания в существующий UI.
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Устанавливаем политику размера - виджет будет растягиваться
        # ИСПРАВЛЕНО: используем QSizePolicy.Policy.Expanding
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        # Данные для графиков
        self.data1 = []  # левый график (синий)
        self.data2 = []  # правый график (красный)
        
        # Настройки отображения
        self.padding = 40  # отступы от краев каждой области
        self.show_grid = True
        self.show_legend = True
        self.show_points = True
        self.split_ratio = 0.5  # соотношение левой/правой части (0.5 = 50/50)
        
        # Цвета графиков
        self.color1 = QColor(0, 100, 255)  # синий
        self.color2 = QColor(255, 50, 50)  # красный
        
        # Названия графиков
        self.title1 = "График 1"
        self.title2 = "График 2"
        
        # Включаем отслеживание мыши
        self.setMouseTracking(True)
        self.mouse_pos = None
        self.active_area = None  # какая область под мышью: 'left', 'right' или None
        
        # Генерируем тестовые данные
        self.generate_test_data()
    
    def generate_test_data(self):
        """Генерирует тестовые данные для графиков"""
        # Левый график: синусоида
        x1 = np.linspace(0, 10, 50)
        y1 = np.sin(x1) * 10 + 20
        
        # Правый график: косинусоида с другим диапазоном
        x2 = np.linspace(0, 20, 40)
        y2 = np.cos(x2 * 0.5) * 15 + 10
        
        self.data1 = list(zip(x1, y1))
        self.data2 = list(zip(x2, y2))
    
    def set_data(self, data1, data2):
        """Устанавливает данные для графиков"""
        self.data1 = data1
        self.data2 = data2
        self.update()
    
    def set_titles(self, title1, title2):
        """Устанавливает названия графиков"""
        self.title1 = title1
        self.title2 = title2
        self.update()
    
    def get_left_rect(self):
        """Возвращает прямоугольник левой области"""
        split_x = int(self.width() * self.split_ratio)
        return QRect(0, 0, split_x, self.height())
    
    def get_right_rect(self):
        """Возвращает прямоугольник правой области"""
        split_x = int(self.width() * self.split_ratio)
        return QRect(split_x, 0, self.width() - split_x, self.height())
    
    def get_data_range(self, data):
        """Возвращает диапазоны значений x и y для графика"""
        if not data:
            return 0, 1, 0, 1
        
        x_values = [p[0] for p in data]
        y_values = [p[1] for p in data]
        
        x_min, x_max = min(x_values), max(x_values)
        y_min, y_max = min(y_values), max(y_values)
        
        # Добавляем отступ
        x_range = x_max - x_min if x_max != x_min else 1
        y_range = y_max - y_min if y_max != y_min else 1
        
        x_min -= x_range * 0.05
        x_max += x_range * 0.05
        y_min -= y_range * 0.05
        y_max += y_range * 0.05
        
        return x_min, x_max, y_min, y_max
    
    def map_to_area(self, x, y, x_min, x_max, y_min, y_max, area_rect):
        """Преобразует координаты данных в координаты виджета для конкретной области"""
        widget_x = area_rect.left() + self.padding + \
                  (x - x_min) / (x_max - x_min) * (area_rect.width() - 2 * self.padding)
        widget_y = area_rect.bottom() - self.padding - \
                  (y - y_min) / (y_max - y_min) * (area_rect.height() - 2 * self.padding)
        
        return widget_x, widget_y
    
    def draw_area_grid(self, painter, x_min, x_max, y_min, y_max, area_rect, color, title=""):
        """Рисует сетку и оси для конкретной области"""
        if not self.show_grid:
            return
        
        # Рисуем рамку области
        pen = QPen(Qt.gray, 1, Qt.DotLine)
        painter.setPen(pen)
        painter.drawRect(area_rect)
        
        # Рисуем заголовок
        painter.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        painter.setPen(QPen(color))
        painter.drawText(area_rect.left() + 10, area_rect.top() + 20, title)
        
        # Рисуем оси
        pen = QPen(color, 2)
        painter.setPen(pen)
        
        # Ось X
        x_axis_y = area_rect.bottom() - self.padding
        painter.drawLine(area_rect.left() + self.padding, x_axis_y,
                        area_rect.right() - self.padding, x_axis_y)
        
        # Ось Y
        painter.drawLine(area_rect.left() + self.padding, area_rect.top() + self.padding,
                        area_rect.left() + self.padding, area_rect.bottom() - self.padding)
        
        # Сетка (полупрозрачная)
        pen = QPen(QColor(200, 200, 200), 1, Qt.DashLine)
        painter.setPen(pen)
        
        # Вертикальные линии сетки
        for i in range(5):
            x = x_min + (x_max - x_min) * i / 4
            wx, _ = self.map_to_area(x, y_min, x_min, x_max, y_min, y_max, area_rect)
            if area_rect.left() + self.padding <= wx <= area_rect.right() - self.padding:
                painter.drawLine(wx, area_rect.top() + self.padding,
                               wx, area_rect.bottom() - self.padding)
        
        # Горизонтальные линии сетки
        for i in range(5):
            y = y_min + (y_max - y_min) * i / 4
            _, wy = self.map_to_area(x_min, y, x_min, x_max, y_min, y_max, area_rect)
            if area_rect.top() + self.padding <= wy <= area_rect.bottom() - self.padding:
                painter.drawLine(area_rect.left() + self.padding, wy,
                               area_rect.right() - self.padding, wy)
        
        # Подписи значений
        painter.setFont(QFont("Arial", 8))
        painter.setPen(QPen(Qt.black, 1))
        
        # Подписи на оси X
        for i in range(5):
            x = x_min + (x_max - x_min) * i / 4
            wx, _ = self.map_to_area(x, y_min, x_min, x_max, y_min, y_max, area_rect)
            if area_rect.left() + self.padding <= wx <= area_rect.right() - self.padding:
                painter.drawText(wx - 20, x_axis_y + 15, f"{x:.1f}")
        
        # Подписи на оси Y
        for i in range(5):
            y = y_min + (y_max - y_min) * i / 4
            _, wy = self.map_to_area(x_min, y, x_min, x_max, y_min, y_max, area_rect)
            if area_rect.top() + self.padding <= wy <= area_rect.bottom() - self.padding:
                painter.drawText(area_rect.left() + self.padding - 35, wy + 5, f"{y:.1f}")
    
    def draw_area_graph(self, painter, data, color, x_min, x_max, y_min, y_max, area_rect, draw_points=True):
        """Рисует график в конкретной области"""
        if not data:
            return
        
        pen = QPen(color, 2)
        painter.setPen(pen)
        
        # Создаем путь для линии графика
        path = QPainterPath()
        first_point = True
        
        for x, y in data:
            wx, wy = self.map_to_area(x, y, x_min, x_max, y_min, y_max, area_rect)
            
            # Проверяем, что точка в пределах области
            if area_rect.left() + self.padding <= wx <= area_rect.right() - self.padding and \
               area_rect.top() + self.padding <= wy <= area_rect.bottom() - self.padding:
                
                if first_point:
                    path.moveTo(wx, wy)
                    first_point = False
                else:
                    path.lineTo(wx, wy)
            else:
                first_point = True
        
        if not path.isEmpty():
            painter.drawPath(path)
        
        # Рисуем точки
        if draw_points and self.show_points:
            painter.setBrush(QBrush(color))
            pen = QPen(Qt.black, 1)
            painter.setPen(pen)
            
            for x, y in data:
                wx, wy = self.map_to_area(x, y, x_min, x_max, y_min, y_max, area_rect)
                
                if area_rect.left() + self.padding <= wx <= area_rect.right() - self.padding and \
                   area_rect.top() + self.padding <= wy <= area_rect.bottom() - self.padding:
                    painter.drawEllipse(QRectF(wx - 3, wy - 3, 6, 6))
    
    def draw_mouse_info(self, painter):
        """Отображает информацию о позиции мыши"""
        if self.mouse_pos and self.active_area:
            painter.setPen(QPen(Qt.gray, 1, Qt.DashLine))
            
            if self.active_area == 'left':
                area_rect = self.get_left_rect()
                data = self.data1
                color = self.color1
                title = self.title1
            else:
                area_rect = self.get_right_rect()
                data = self.data2
                color = self.color2
                title = self.title2
            
            if data:
                x_min, x_max, y_min, y_max = self.get_data_range(data)
                
                # Рисуем перекрестие
                painter.drawLine(self.mouse_pos.x(), area_rect.top() + self.padding,
                               self.mouse_pos.x(), area_rect.bottom() - self.padding)
                painter.drawLine(area_rect.left() + self.padding, self.mouse_pos.y(),
                               area_rect.right() - self.padding, self.mouse_pos.y())
                
                # Преобразуем координаты
                data_x = x_min + (self.mouse_pos.x() - area_rect.left() - self.padding) / \
                        (area_rect.width() - 2 * self.padding) * (x_max - x_min)
                data_y = y_max - (self.mouse_pos.y() - area_rect.top() - self.padding) / \
                        (area_rect.height() - 2 * self.padding) * (y_max - y_min)
                
                # Отображаем координаты
                info_rect = QRect(self.mouse_pos.x() + 10, self.mouse_pos.y() - 30, 150, 40)
                
                # Фон для текста
                painter.setBrush(QBrush(QColor(255, 255, 255, 200)))
                painter.setPen(QPen(Qt.black, 1))
                painter.drawRect(info_rect)
                
                painter.setPen(QPen(color))
                painter.setFont(QFont("Arial", 8, QFont.Weight.Bold))
                painter.drawText(info_rect.left() + 5, info_rect.top() + 15, title)
                
                painter.setPen(Qt.black)
                painter.drawText(info_rect.left() + 5, info_rect.top() + 30, 
                               f"X: {data_x:.2f}, Y: {data_y:.2f}")
    
    def paintEvent(self, event):
        """Обработчик события отрисовки"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        try:
            # Заливаем фон белым
            painter.fillRect(self.rect(), Qt.white)
            
            # Получаем прямоугольники областей
            left_rect = self.get_left_rect()
            right_rect = self.get_right_rect()
            
            # Рисуем разделительную линию
            split_x = int(self.width() * self.split_ratio)
            painter.setPen(QPen(Qt.black, 2))
            painter.drawLine(split_x, 0, split_x, self.height())
            
            # Рисуем левый график
            if self.data1:
                x_min, x_max, y_min, y_max = self.get_data_range(self.data1)
                self.draw_area_grid(painter, x_min, x_max, y_min, y_max, left_rect, self.color1, self.title1)
                self.draw_area_graph(painter, self.data1, self.color1, x_min, x_max, y_min, y_max, left_rect)
            
            # Рисуем правый график
            if self.data2:
                x_min, x_max, y_min, y_max = self.get_data_range(self.data2)
                self.draw_area_grid(painter, x_min, x_max, y_min, y_max, right_rect, self.color2, self.title2)
                self.draw_area_graph(painter, self.data2, self.color2, x_min, x_max, y_min, y_max, right_rect)
            
            # Рисуем информацию о мыши
            self.draw_mouse_info(painter)
            
            # Подсвечиваем активную область
            if self.active_area:
                painter.setBrush(QBrush(QColor(255, 255, 0, 30)))
                painter.setPen(Qt.NoPen)
                if self.active_area == 'left':
                    painter.drawRect(left_rect)
                else:
                    painter.drawRect(right_rect)
            
        finally:
            painter.end()
    
    def mouseMoveEvent(self, event):
        """Обработчик движения мыши"""
        self.mouse_pos = event.pos()
        
        # Определяем, в какой области находится мышь
        split_x = int(self.width() * self.split_ratio)
        if event.pos().x() < split_x:
            self.active_area = 'left'
        else:
            self.active_area = 'right'
        
        self.update()
    
    def leaveEvent(self, event):
        """Обработчик ухода мыши с виджета"""
        self.mouse_pos = None
        self.active_area = None
        self.update()
    
    def resizeEvent(self, event):
        """Обработчик изменения размера"""
        self.update()