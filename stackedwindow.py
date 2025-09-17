import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QHBoxLayout, QPushButton, QLabel, QLineEdit,
                              QListWidget, QStackedWidget, QSlider, QProgressBar)
from PySide6.QtCore import Qt, QTimer

class StackedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тест переключения страниц")  # Устанавливаем заголовок окна
        self.setGeometry(100, 100, 600, 400)  # Размер и положение окна

        # Создаем центральный виджет, который будет основой для всех элементов
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Главный горизонтальный слой (разделяет окно на две части: навигация и контент)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # -------- Левая панель с кнопками навигации --------
        nav_layout = QVBoxLayout()  # Вертикальный слой для навигационных кнопок

        self.page1_btn = QPushButton("Форма ввода")  # Кнопка перехода на 1 страницу
        self.page1_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        nav_layout.addWidget(self.page1_btn)

        self.page2_btn = QPushButton("Список элементов")  # Кнопка перехода на 2 страницу
        self.page2_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        nav_layout.addWidget(self.page2_btn)

        self.page3_btn = QPushButton("Прогресс бар")  # Кнопка перехода на 3 страницу
        self.page3_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        nav_layout.addWidget(self.page3_btn)

        nav_layout.addStretch()  # Растягиваем пространство под кнопками, чтобы они были наверху
        main_layout.addLayout(nav_layout)  # Добавляем навигацию в главный слой

        # -------- Правая панель с QStackedWidget --------
        self.stacked_widget = QStackedWidget()  # Виджет для переключения страниц
        main_layout.addWidget(self.stacked_widget)

        # ========== Страница 1 - Форма ввода ==========
        page1 = QWidget()
        page1_layout = QVBoxLayout()

        self.name_input = QLineEdit()  # Поле для ввода имени
        self.name_input.setPlaceholderText("Введите имя")
        page1_layout.addWidget(QLabel("Имя:"))
        page1_layout.addWidget(self.name_input)

        self.email_input = QLineEdit()  # Поле для ввода email
        self.email_input.setPlaceholderText("Введите email")
        page1_layout.addWidget(QLabel("Email:"))
        page1_layout.addWidget(self.email_input)

        self.submit_btn = QPushButton("Отправить")  # Кнопка отправки формы
        self.submit_btn.clicked.connect(self.submit_form)
        page1_layout.addWidget(self.submit_btn)

        self.form_result = QLabel("")  # Текст для вывода результата
        page1_layout.addWidget(self.form_result)

        page1.setLayout(page1_layout)
        self.stacked_widget.addWidget(page1)  # Добавляем первую страницу в стек

        # ========== Страница 2 - Список ==========
        page2 = QWidget()
        page2_layout = QVBoxLayout()

        self.list_widget = QListWidget()  # Список элементов
        self.list_widget.addItems(["Элемент 1", "Элемент 2", "Элемент 3"])  # Начальные элементы
        page2_layout.addWidget(self.list_widget)

        add_layout = QHBoxLayout()  # Слой для поля ввода и кнопки добавления нового элемента
        self.new_item_input = QLineEdit()
        self.new_item_input.setPlaceholderText("Новый элемент")
        add_layout.addWidget(self.new_item_input)

        self.add_item_btn = QPushButton("Добавить")  # Кнопка для добавления нового элемента
        self.add_item_btn.clicked.connect(self.add_list_item)
        add_layout.addWidget(self.add_item_btn)

        page2_layout.addLayout(add_layout)
        page2.setLayout(page2_layout)
        self.stacked_widget.addWidget(page2)  # Добавляем вторую страницу в стек

        # ========== Страница 3 - Прогресс бар ==========
        page3 = QWidget()
        page3_layout = QVBoxLayout()

        self.progress_bar = QProgressBar()  # Прогресс-бар, изначально на 0
        self.progress_bar.setValue(0)
        page3_layout.addWidget(self.progress_bar)

        self.slider = QSlider(Qt.Horizontal)  # Горизонтальный слайдер для управления прогрессом
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.progress_bar.setValue)  # Слайдер меняет значение прогресс-бара
        page3_layout.addWidget(self.slider)

        self.auto_progress_btn = QPushButton("Авто-прогресс")  # Кнопка для автоматического заполнения прогресса
        self.auto_progress_btn.clicked.connect(self.start_auto_progress)
        page3_layout.addWidget(self.auto_progress_btn)

        page3.setLayout(page3_layout)
        self.stacked_widget.addWidget(page3)  # Добавляем третью страницу в стек

    # ====== Метод для обработки отправки формы ======
    def submit_form(self):
        name = self.name_input.text()
        email = self.email_input.text()
        if name and email:
            self.form_result.setText(f"Данные отправлены: {name}, {email}")  # Если оба поля заполнены
        else:
            self.form_result.setText("Заполните все поля!")  # Если что-то не заполнено

    # ====== Метод для добавления нового элемента в список ======
    def add_list_item(self):
        text = self.new_item_input.text()
        if text:
            self.list_widget.addItem(text)  # Добавляем новый элемент
            self.new_item_input.clear()  # Очищаем поле ввода

    # ====== Метод для запуска авто-прогресса ======
    def start_auto_progress(self):
        self.timer = QTimer()  # Создаем таймер
        self.timer.timeout.connect(self.update_progress)  # При каждом срабатывании таймера вызывается update_progress
        self.progress_value = 0  # Начальное значение прогресса
        self.timer.start(100)  # Таймер срабатывает каждые 100 мс

    # ====== Метод для обновления прогресс-бара и слайдера ======
    def update_progress(self):
        self.progress_value += 1
        if self.progress_value > 100:
            self.timer.stop()  # Останавливаем таймер, если достигли 100
            return
        self.progress_bar.setValue(self.progress_value)  # Обновляем прогресс-бар
        self.slider.setValue(self.progress_value)  # Обновляем слайдер

# ====== Запуск приложения ======
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StackedWindow()
    window.show()
    sys.exit(app.exec())