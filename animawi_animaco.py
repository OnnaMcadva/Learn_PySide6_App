import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLabel
)
from PySide6.QtCore import (
    QTimer, QPropertyAnimation, QEasingCurve, QPoint, QRect, Property, Qt
)
from PySide6.QtGui import QColor, QPainter

# --- Квадратный виджет с поддержкой плавной анимации цвета ---
class AnimatedWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._color = QColor("red")
        self.setGeometry(50, 50, 100, 100)  # начальная позиция и размер
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("border-radius: 10px;")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self._color)
        painter.setPen(self._color)
        painter.drawRoundedRect(self.rect(), 10, 10)

    def getColor(self):
        return self._color

    def setColor(self, color):
        if self._color != color:
            self._color = color
            self.update()

    color = Property(QColor, getColor, setColor)

# --- Главное окно приложения ---
class AnimationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тест анимаций и таймера")
        self.setGeometry(100, 100, 600, 400)

        # Центральный виджет-контейнер
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout для элементов управления (НЕ для квадрата)
        layout = QVBoxLayout(central_widget)

        # --- Сам квадрат, размещается вручную, не в layout! ---
        self.animated_widget = AnimatedWidget(central_widget)

        # --- Таймер и лейбл для вывода времени ---
        self.timer_label = QLabel("Таймер: 0 сек")
        layout.addWidget(self.timer_label)

        # --- Кнопки для управления таймером ---
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Старт")
        self.start_btn.clicked.connect(self.start_timer)
        btn_layout.addWidget(self.start_btn)
        self.stop_btn = QPushButton("Стоп")
        self.stop_btn.clicked.connect(self.stop_timer)
        self.stop_btn.setEnabled(False)
        btn_layout.addWidget(self.stop_btn)
        layout.addLayout(btn_layout)

        # --- Кнопки анимаций ---
        anim_layout = QHBoxLayout()
        move_btn = QPushButton("Движение")
        move_btn.clicked.connect(self.animate_movement)
        anim_layout.addWidget(move_btn)
        color_btn = QPushButton("Цвет")
        color_btn.clicked.connect(self.animate_color)
        anim_layout.addWidget(color_btn)
        scale_btn = QPushButton("Масштаб")
        scale_btn.clicked.connect(self.animate_scale)
        anim_layout.addWidget(scale_btn)
        layout.addLayout(anim_layout)

        # --- Таймер ---
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.seconds = 0

        # --- Переменные для хранения анимаций ---
        self.anim = None
        self.color_anim = None
        self.size_anim = None

        # --- Цвета для анимации ---
        self.colors = [
            QColor("#43B02A"), QColor("green"), QColor("blue"),
            QColor("yellow"), QColor("#0E3A2F"), QColor("#79C000"),
        ]
        self.current_color_index = 0

        # --- Флаг для контроля масштаба (True — большой, False — маленький) ---
        self.is_scaled_up = False

    # --- Запуск таймера ---
    def start_timer(self):
        self.timer.start(1000)
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)

    # --- Остановка таймера и сброс ---
    def stop_timer(self):
        self.timer.stop()
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.seconds = 0
        self.timer_label.setText("Таймер: 0 сек")

    # --- Обновление значения таймера ---
    def update_timer(self):
        self.seconds += 1
        self.timer_label.setText(f"Таймер: {self.seconds} сек")

    # --- Анимация перемещения квадрата вправо и обратно ---
    def animate_movement(self):
        start_rect = self.animated_widget.geometry()
        if start_rect.x() < 300:
            end_rect = QRect(400, start_rect.y(), start_rect.width(), start_rect.height())
        else:
            end_rect = QRect(50, start_rect.y(), start_rect.width(), start_rect.height())
        self.anim = QPropertyAnimation(self.animated_widget, b"geometry")
        self.anim.setDuration(1000)
        self.anim.setStartValue(start_rect)
        self.anim.setEndValue(end_rect)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        self.anim.start()

    # --- Плавная анимация смены цвета квадрата ---
    def animate_color(self):
        old_color = self.animated_widget.color
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)
        new_color = self.colors[self.current_color_index]
        self.color_anim = QPropertyAnimation(self.animated_widget, b"color")
        self.color_anim.setDuration(800)
        self.color_anim.setStartValue(old_color)
        self.color_anim.setEndValue(new_color)
        self.color_anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.color_anim.start()

    # --- Плавная анимация изменения масштаба (размера) квадрата ---
    def animate_scale(self):
        start_rect = self.animated_widget.geometry()
        if not self.is_scaled_up:
            # Увеличиваем размер, но позиция корректируется так, чтобы квадрат "оставался" примерно на месте
            new_w, new_h = 150, 150
            new_x = start_rect.x() - (new_w - start_rect.width()) // 2
            new_y = start_rect.y() - (new_h - start_rect.height()) // 2
        else:
            new_w, new_h = 100, 100
            new_x = start_rect.x() + (start_rect.width() - new_w) // 2
            new_y = start_rect.y() + (start_rect.height() - new_h) // 2
        end_rect = QRect(new_x, new_y, new_w, new_h)
        self.is_scaled_up = not self.is_scaled_up
        self.size_anim = QPropertyAnimation(self.animated_widget, b"geometry")
        self.size_anim.setDuration(800)
        self.size_anim.setStartValue(start_rect)
        self.size_anim.setEndValue(end_rect)
        self.size_anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.size_anim.start()

# --- Запуск приложения ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    sys.exit(app.exec())
