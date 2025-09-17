import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QHBoxLayout, QPushButton, QLabel)
from PySide6.QtCore import QTimer, QPropertyAnimation, QEasingCurve, QPoint
from PySide6.QtGui import QColor

class AnimationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тест анимаций и таймера")
        self.setGeometry(100, 100, 600, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # --- animated_widget вне layout! ---
        self.animated_widget = QWidget(central_widget)
        self.animated_widget.setStyleSheet("background-color: red; border-radius: 10px;")
        self.animated_widget.setFixedSize(100, 100)
        self.animated_widget.move(50, 50)  # Задаем стартовую позицию
        
        # Таймер
        self.timer_label = QLabel("Таймер: 0 сек")
        layout.addWidget(self.timer_label)
        
        # Кнопки управления
        btn_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("Старт")
        self.start_btn.clicked.connect(self.start_timer)
        btn_layout.addWidget(self.start_btn)
        
        self.stop_btn = QPushButton("Стоп")
        self.stop_btn.clicked.connect(self.stop_timer)
        self.stop_btn.setEnabled(False)
        btn_layout.addWidget(self.stop_btn)
        
        layout.addLayout(btn_layout)
        
        # Анимационные кнопки
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
        
        # Настройка таймера
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.seconds = 0
        
        # Для анимаций - нужно хранить ссылку, чтобы не удаляли сборщики мусора!
        self.anim = None
    
    def start_timer(self):
        self.timer.start(1000)  # 1 секунда
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
    
    def stop_timer(self):
        self.timer.stop()
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.seconds = 0
        self.timer_label.setText("Таймер: 0 сек")
    
    def update_timer(self):
        self.seconds += 1
        self.timer_label.setText(f"Таймер: {self.seconds} сек")
    
    def animate_movement(self):
        # Анимируем позицию по горизонтали (например, вправо и обратно)
        start_pos = self.animated_widget.pos()
        if start_pos.x() < 300:
            end_pos = QPoint(400, start_pos.y())
        else:
            end_pos = QPoint(50, start_pos.y())
        self.anim = QPropertyAnimation(self.animated_widget, b"pos")
        self.anim.setDuration(1000)
        self.anim.setStartValue(start_pos)
        self.anim.setEndValue(end_pos)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        self.anim.start()
    
    def animate_color(self):
        # Просто меняем цвет, не анимируем плавно
        colors = ["red", "green", "blue", "yellow", "purple"]
        current_color = self.animated_widget.styleSheet().split(":")[1].split(";")[0].strip()
        next_color = colors[(colors.index(current_color) + 1) % len(colors)]
        self.animated_widget.setStyleSheet(f"background-color: {next_color}; border-radius: 10px;")
    
    def animate_scale(self):
        current_size = self.animated_widget.size()
        new_size = current_size * 1.5 if current_size.width() < 150 else current_size / 1.5
        self.anim = QPropertyAnimation(self.animated_widget, b"size")
        self.anim.setDuration(1000)
        self.anim.setStartValue(current_size)
        self.anim.setEndValue(new_size)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    sys.exit(app.exec())
