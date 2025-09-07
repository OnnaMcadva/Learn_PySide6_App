import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                              QHBoxLayout, QPushButton, QLineEdit, QTextEdit,
                              QLabel, QSlider)
from PySide6.QtCore import Qt

class WidgetTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тест виджетов и макетов")
        self.setGeometry(100, 100, 600, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Создаем горизонтальный макет (QHBoxLayout) для верхней панели окна, 
        # где будут располагаться поле ввода текста (QLineEdit) и кнопка (QPushButton).
        # Этот макет размещает элементы слева направо, чтобы они были на одной линии.
        top_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введите текст здесь...")
        top_layout.addWidget(self.input_field)
        
        self.add_button = QPushButton("Добавить текст")
        self.add_button.clicked.connect(self.add_text)
        top_layout.addWidget(self.add_button)
        
        main_layout.addLayout(top_layout)
        
        # Создаем текстовое поле (QTextEdit), которое отображает многострочный текст.
        # Оно будет показывать текст, добавленный из поля ввода, и займет основное пространство окна.
        self.text_area = QTextEdit()
        main_layout.addWidget(self.text_area)
        
        # Создаем горизонтальный макет (QHBoxLayout) для нижней панели окна, 
        # где будут находиться метка (QLabel) и слайдер (QSlider) для управления яркостью.
        # Макет размещает элементы слева направо, включая метку с текущим значением слайдера.
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(QLabel("Яркость:"))
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.on_slider_change)
        bottom_layout.addWidget(self.slider)
        
        self.slider_value = QLabel("50%")
        bottom_layout.addWidget(self.slider_value)
        
        main_layout.addLayout(bottom_layout)
    
    def add_text(self):
        text = self.input_field.text()
        if text:
            self.text_area.append(f"→ {text}")
            self.input_field.clear()
    
    def on_slider_change(self, value):
        self.slider_value.setText(f"{value}%")
        # Можно добавить изменение яркости окна
        opacity = value / 100.0
        self.setWindowOpacity(opacity)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WidgetTestWindow()
    window.show()
    sys.exit(app.exec())
