from PySide6.QtCore import Signal, QEvent, QObject,Qt

class WidgetClickMonitor(QObject):
    """Мониторит клики по любому виджету"""
    
    clicked = Signal(object, object)  # виджет, событие
    
    def __init__(self, widget):
        super().__init__(widget)
        self.widget = widget
        widget.installEventFilter(self)
        
    def eventFilter(self, obj, event):
        if obj == self.widget and event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                self.clicked.emit(obj, event)
                return True
        return super().eventFilter(obj, event)
