import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QPushButton, QLabel, QMessageBox, QFileDialog,
                              QColorDialog)
from PySide6.QtGui import QColor

class DialogTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тест диалоговых окон")
        self.setGeometry(100, 100, 500, 300)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Создаем четыре кнопки (QPushButton), каждая из которых открывает разные диалоговые окна.
        # Кнопки размещаются в вертикальном макете (QVBoxLayout), чтобы отображаться одна под другой.
        # Каждая кнопка связана с методом, который вызывается при клике, используя сигнал clicked.
        self.info_btn = QPushButton("Информационное сообщение")
        self.info_btn.clicked.connect(self.show_info)
        layout.addWidget(self.info_btn)
        
        self.warning_btn = QPushButton("Предупреждение")
        self.warning_btn.clicked.connect(self.show_warning)
        layout.addWidget(self.warning_btn)
        
        self.file_btn = QPushButton("Выбрать файл")
        self.file_btn.clicked.connect(self.open_file)
        layout.addWidget(self.file_btn)
        
        self.color_btn = QPushButton("Выбрать цвет")
        self.color_btn.clicked.connect(self.choose_color)
        layout.addWidget(self.color_btn)
        
        # Создаем метку (QLabel) для отображения результатов взаимодействия с диалоговыми окнами.
        # Эта метка показывает, какое действие выполнил пользователь (например, выбор файла или цвета).
        # Она стилизована с помощью CSS-подобного синтаксиса для красивого отображения.
        self.result_label = QLabel("Результаты будут отображаться здесь")
        self.result_label.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0;
                border: 2px solid #ccc;
                padding: 10px;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.result_label)
        
        # Применяем стилизацию ко всем кнопкам в окне с помощью CSS-подобного синтаксиса.
        # Задаем цвет фона, текст, отступы и эффекты (например, при наведении или нажатии).
        # Это улучшает внешний вид приложения, делая кнопки более современными и интерактивными.
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
    
    def show_info(self):
        QMessageBox.information(self, "Информация", 
                               "Это информационное сообщение!\nPySide6 очень мощный!")
        self.result_label.setText("Было показано информационное сообщение")
    
    def show_warning(self):
        reply = QMessageBox.warning(self, "Предупреждение",
                                  "Вы уверены, что хотите продолжить?",
                                  QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.result_label.setText("Пользователь выбрал 'Да'")
        else:
            self.result_label.setText("Пользователь выбрал 'Нет'")
    
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл", "", "Все файлы (*);;Текстовые файлы (*.txt)"
        )
        if file_path:
            self.result_label.setText(f"Выбран файл: {file_path}")
        else:
            self.result_label.setText("Файл не выбран")
    
    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.result_label.setText(f"Выбран цвет: {color.name()}")
            self.result_label.setStyleSheet(f"""
                QLabel {{
                    background-color: {color.name()};
                    color: {'white' if color.lightness() < 128 else 'black'};
                    border: 2px solid #ccc;
                    padding: 10px;
                    border-radius: 5px;
                }}
            """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DialogTestWindow()
    window.show()
    sys.exit(app.exec())
