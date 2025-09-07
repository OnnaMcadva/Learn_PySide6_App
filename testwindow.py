import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

# QApplication: Управляет приложением, его событиями и жизненным циклом.
# QMainWindow: Класс для создания главного окна приложения.
# QWidget: Базовый класс для всех виджетов (графических элементов).
# QVBoxLayout: Класс для вертикального размещения виджетов.
# QLabel: Класс для отображения текста или изображений.
# QPushButton: Класс для создания кнопки.

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тестовая программа с вертикальными и горизонтальными виджетами")
        self.setGeometry(100, 100, 400, 200)

        # Создаем центральный виджет, который будет содержать все элементы окна (надпись и кнопки).
        # QWidget — это пустой контейнер, в который мы добавим макеты и виджеты.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Создаем вертикальный макет (QVBoxLayout) для общей структуры окна.
        # Он разместит надпись сверху, а горизонтальный макет с кнопками — снизу.
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Создаем надпись (QLabel) с начальным текстом "Нажмите любую кнопку!".
        # Сохраняем её как self.label, чтобы обновлять текст при клике на кнопки.
        self.label = QLabel("Нажмите любую кнопку!")
        layout.addWidget(self.label)

        # Создаем горизонтальный макет (QHBoxLayout) для размещения двух кнопок рядом.
        # QHBoxLayout располагает виджеты слева направо.
        button_layout = QHBoxLayout()

        # Создаем первую кнопку с текстом "Нажми меня!" и подключаем её сигнал clicked
        # к методу on_button1_click, который будет обрабатывать клики по первой кнопке.
        self.button1 = QPushButton("Нажми меня!")
        self.button1.clicked.connect(self.on_button1_click)
        button_layout.addWidget(self.button1)

        # Создаем вторую кнопку с текстом "Нажми ещё!" и подключаем её сигнал clicked
        # к методу on_button2_click, который будет обрабатывать клики по второй кнопке.
        self.button2 = QPushButton("Нажми ещё!")
        self.button2.clicked.connect(self.on_button2_click)
        button_layout.addWidget(self.button2)

        # Добавляем горизонтальный макет с кнопками в вертикальный макет.
        # Это помещает обе кнопки (расположенные горизонтально) под надписью.
        layout.addLayout(button_layout)

        self.click_count1 = 0  # Счетчик для первой кнопки
        self.click_count2 = 0  # Счетчик для второй кнопки

    # Определяем метод для обработки кликов по первой кнопке.
    # Увеличивает счетчик click_count1 и обновляет текст надписи.
    def on_button1_click(self):
        self.click_count1 += 1
        word = "раз" if self.click_count1 == 1 else "раза"
        self.label.setText(f"Кнопка 1 нажата {self.click_count1} {word}!")

    # Определяем метод для обработки кликов по второй кнопке.
    # Увеличивает счетчик click_count2 и обновляет текст надписи.
    def on_button2_click(self):
        self.click_count2 += 1
        word = "раз" if self.click_count2 == 1 else "раза"
        self.label.setText(f"Кнопка 2 нажата {self.click_count2} {word}!")

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = TestWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Ошибка: {e}")
