import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QTimer, QRect, Qt
from PySide6.QtGui import QColor, QPainter

CELL_SIZE = 40
MIN_CELL_SIZE = 20
SNAKE_LENGTH = 8
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

class SnakeSquare(QWidget):
    def __init__(self, color, size, parent=None):
        super().__init__(parent)
        self._color = color
        self._size = size
        self.resize(self._size, self._size)
        self.setAttribute(Qt.WA_StyledBackground, True)

    def set_size(self, size):
        self._size = size
        self.resize(size, size)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self._color)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 8, 8)

class SnakeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Змейка с разными размерами сегментов")
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Начальные координаты змейки (голова - первый элемент)
        self.snake_pos = [(100 + i*CELL_SIZE, 100) for i in range(SNAKE_LENGTH)]
        self.direction = (1, 0)  # вправо

        # Создаём квадратики змейки с разными размерами
        self.snake_widgets = []
        colors = [QColor("#43B02A"), QColor("green"), QColor("blue"),
                  QColor("yellow"), QColor("#0E3A2F"), QColor("#79C000"),
                  QColor("orange"), QColor("red")]
        for i in range(SNAKE_LENGTH):
            # Размер уменьшается от головы к хвосту
            size = CELL_SIZE - int((CELL_SIZE-MIN_CELL_SIZE) * i/(SNAKE_LENGTH-1))
            widget = SnakeSquare(colors[i % len(colors)], size, self.central_widget)
            widget.move(*self.snake_pos[i])
            widget.show()
            self.snake_widgets.append(widget)

        # Таймер для движения змейки
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_snake)
        self.timer.start(120)  # скорость

    def keyPressEvent(self, event):
        key = event.key()
        # Меняем направление по стрелкам
        if key == Qt.Key_Left and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif key == Qt.Key_Right and self.direction != (-1, 0):
            self.direction = (1, 0)
        elif key == Qt.Key_Up and self.direction != (0, 1):
            self.direction = (0, -1)
        elif key == Qt.Key_Down and self.direction != (0, -1):
            self.direction = (0, 1)

    def move_snake(self):
        # Вычисляем новую позицию головы
        head_x, head_y = self.snake_pos[0]
        dx, dy = self.direction
        new_head = (head_x + dx * CELL_SIZE, head_y + dy * CELL_SIZE)

        # Ограничения: если уходит за окно, появляется с другой стороны
        new_head = (
            new_head[0] % WINDOW_WIDTH,
            new_head[1] % WINDOW_HEIGHT
        )

        # Смещаем позиции (хвост идёт за головой)
        self.snake_pos = [new_head] + self.snake_pos[:-1]

        # Перемещаем виджеты, обновляем размеры
        for i, widget in enumerate(self.snake_widgets):
            size = CELL_SIZE - int((CELL_SIZE-MIN_CELL_SIZE) * i/(SNAKE_LENGTH-1))
            widget.set_size(size)
            widget.move(self.snake_pos[i][0], self.snake_pos[i][1])
            widget.update()

# --- Запуск приложения ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SnakeWindow()
    window.show()
    window.central_widget.setFocus()  # чтобы ловить клавиши
    sys.exit(app.exec())