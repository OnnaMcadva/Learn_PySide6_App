# Используемые библиотеки и функции в проекте

## 1. Модуль: `sys`
- **sys.argv**  
  Получение аргументов командной строки для передачи в QApplication.
- **sys.exit(...)**  
  Корректное завершение приложения.

---

## 2. PySide6.QtWidgets

### Классы и функции:
- **QApplication**  
  Основной класс для управления жизненным циклом Qt-приложения. Инициализация и запуск главного цикла событий.
- **QMainWindow**  
  Базовый класс главного окна приложения (рамка, меню, статусбар и центральный виджет).
- **QWidget**  
  Базовый класс для всех виджетов (элементов интерфейса).
- **QVBoxLayout, QHBoxLayout**  
  Вертикальные и горизонтальные макеты для размещения других виджетов.
- **QPushButton**  
  Кнопка с возможностью обработки нажатий через сигнал clicked.
- **QLabel**  
  Метка для отображения текста и изображений.
- **QLineEdit**  
  Однострочное поле для ввода текста пользователем.
- **QListWidget**  
  Виджет для отображения и управления списком элементов.
- **QStackedWidget**  
  Контейнер для переключения между несколькими страницами/виджетами.
- **QSlider**  
  Ползунок для выбора значения из диапазона (например, для яркости или процентов).
- **QProgressBar**  
  Виджет для отображения прогресса выполнения задачи.
- **QTableWidget**  
  Виджет таблицы для отображения данных по строкам и столбцам.
- **QTableWidgetItem**  
  Класс для хранения данных в ячейках таблицы.
- **QHeaderView**  
  Класс для управления заголовками таблиц (например, растяжение колонок).
- **QMenu**  
  Контекстное меню для дополнительных действий над таблицей.
- **QInputDialog**  
  Диалог для ввода строки пользователем.
- **QMessageBox**  
  Диалоговое окно для показа информационных и предупреждающих сообщений.
- **QFileDialog**  
  Диалоговое окно для выбора файла на диске.
- **QColorDialog**  
  Диалоговое окно для выбора цвета.

---

## 3. PySide6.QtCore

### Классы и функции:
- **QTimer**  
  Таймер для регулярного выполнения действий (например, обновление времени или прогресса).
- **QPropertyAnimation**  
  Класс для анимации свойств виджетов (например, перемещение, размер, цвет).
- **QEasingCurve**  
  Класс для задания плавности анимации (например, скачок, плавное начало/конец).
- **QPoint**  
  Класс для хранения координат (x, y) — используется для размещения и анимации виджетов.
- **QRect**  
  Класс для хранения прямоугольной области (позиция и размер).
- **Property**  
  Декоратор для создания анимируемых свойств в кастомных виджетах.
- **Qt**  
  Пространство имён с флагами, константами, модификаторами (например, Qt.Horizontal, Qt.CustomContextMenu).

---

## 4. PySide6.QtGui

### Классы и функции:
- **QColor**  
  Класс для хранения цвета (RGB/HEX) — используется для задания цвета элементов.
- **QPainter**  
  Класс для кастомной отрисовки (например, закрашивание прямоугольника с цветом и скруглением).

---

# Схема использования функций и их назначение (с комментариями)

## QApplication
- `app = QApplication(sys.argv)`  
  — Создаёт объект приложения и запускает цикл обработки событий.

## QMainWindow
- `class ... (QMainWindow)`  
  — Создаёт главное окно приложения с центральным виджетом.
- `setWindowTitle(str)`  
  — Устанавливает заголовок окна.
- `setGeometry(x, y, w, h)`  
  — Задает положение и размер окна.

## QWidget
- `QWidget()`  
  — Создаёт базовый контейнер для других виджетов.
- `setCentralWidget(widget)`  
  — Устанавливает центральный виджет для QMainWindow.
- `setLayout(layout)`  
  — Применяет layout к виджету.
- `setStyleSheet(str)`  
  — Устанавливает CSS-подобные стили для виджета.
- `setFixedSize(w, h)`  
  — Задаёт фиксированный размер.
- `move(x, y)`  
  — Перемещает виджет по координатам.

## QVBoxLayout, QHBoxLayout
- `addWidget(widget)`  
  — Добавляет виджет в layout.
- `addLayout(layout)`  
  — Вкладывает один layout в другой.

## QPushButton
- `QPushButton("текст")`  
  — Создаёт кнопку.
- `clicked.connect(function)`  
  — Подключает обработчик к событию нажатия.

## QLabel
- `QLabel("текст")`  
  — Создаёт текстовую метку.
- `setText(str)`  
  — Изменяет текст метки.
- `setStyleSheet(str)`  
  — Применяет стили.

## QLineEdit
- `QLineEdit()`  
  — Однострочное поле ввода.
- `setPlaceholderText(str)`  
  — Серый текст-подсказка внутри поля.
- `setText(str)`  
  — Устанавливает текст.
- `text()`  
  — Получает текст.

## QTextEdit
- `QTextEdit()`  
  — Многострочное текстовое поле.
- `append(str)`  
  — Добавляет строку в конец текста.

## QSlider
- `QSlider(Qt.Horizontal)`  
  — Горизонтальный ползунок.
- `setRange(min, max)`  
  — Диапазон значений.
- `valueChanged.connect(function)`  
  — Обработчик изменения значения.

## QProgressBar
- `QProgressBar()`  
  — Прогресс-бар.
- `setValue(int)`  
  — Устанавливает прогресс.

## QListWidget
- `addItems([str, ...])`  
  — Добавляет элементы в список.
- `addItem(str)`  
  — Добавляет один элемент.

## QStackedWidget
- `addWidget(widget)`  
  — Добавляет страницу/виджет.
- `setCurrentIndex(index)`  
  — Переключает страницу.

## QTableWidget, QTableWidgetItem
- `QTableWidget(row, col)`  
  — Таблица с заданным числом строк и столбцов.
- `setHorizontalHeaderLabels([str, ...])`  
  — Задает заголовки столбцов.
- `setItem(row, col, QTableWidgetItem(str))`  
  — Устанавливает элемент в ячейку.
- `insertRow(row)`  
  — Добавляет строку.
- `removeRow(row)`  
  — Удаляет строку.
- `currentRow()`  
  — Текущая выделенная строка.
- `currentColumn()`  
  — Текущий выделенный столбец.

## QHeaderView
- `setSectionResizeMode(QHeaderView.Stretch)`  
  — Растягивает столбцы таблицы по ширине.

## QMenu
- `addAction(str)`  
  — Добавляет пункт в меню.
- `exec_(pos)`  
  — Показывает меню в заданной позиции.

## QInputDialog
- `getText(...)`  
  — Диалог для ввода текста.

## QMessageBox
- `information(parent, title, message)`  
  — Показывает информационное сообщение.
- `warning(parent, title, message, buttons)`  
  — Показывает окно с предупреждением и кнопками (Yes/No).

## QFileDialog
- `getOpenFileName(parent, title, dir, filter)`  
  — Диалог выбора файла, возвращает путь.

## QColorDialog
- `getColor()`  
  — Диалог выбора цвета.

## QTimer
- `QTimer()`  
  — Создаёт таймер.
- `timeout.connect(function)`  
  — Подключает обработчик "тикания".
- `start(ms)`  
  — Запускает таймер с периодом ms миллисекунд.
- `stop()`  
  — Останавливает таймер.

## QPropertyAnimation
- `QPropertyAnimation(obj, b"property")`  
  — Анимация свойства (например, pos, geometry, size, color).
- `setDuration(ms)`  
  — Длительность анимации.
- `setStartValue(val)`  
  — Начальное значение.
- `setEndValue(val)`  
  — Конечное значение.
- `setEasingCurve(QEasingCurve.Type)`  
  — Кривая плавности анимации.
- `start()`  
  — Запускает анимацию.

## QEasingCurve
- `QEasingCurve.OutBounce`, `QEasingCurve.InOutQuad`  
  — Типы кривых для анимации (отскок, плавное начало и конец).

## QPoint, QRect
- `QPoint(x, y)`  
  — Координаты точки.
- `QRect(x, y, w, h)`  
  — Прямоугольник (позиция и размер).

## Property (PySide6.QtCore)
- `Property(QColor, getter, setter)`  
  — Декоратор для создания анимируемого свойства цвета.

## Qt
- `Qt.Horizontal`  
  — Ориентация (например, для QSlider).
- `Qt.CustomContextMenu`  
  — Флаг для включения кастомного контекстного меню.

## QColor
- `QColor("имя")` или `QColor("#HEX")`  
  — Создаёт цвет для использования в стиле или отрисовке.
- `name()`  
  — Получает HEX-код цвета.
- `lightness()`  
  — Яркость цвета.

## QPainter
- `QPainter(widget)`  
  — Позволяет кастомно рисовать на виджете.
- `setRenderHint(QPainter.Antialiasing)`  
  — Включает сглаживание.
- `setBrush(color)`  
  — Задает кисть для закраски.
- `setPen(color)`  
  — Задает цвет обводки.
- `drawRoundedRect(rect, rx, ry)`  
  — Рисует скругленный прямоугольник.

---

# Пример схемы (для одной из форм):

```
PySide6.QtWidgets
│
├─ QApplication
├─ QMainWindow
│   └─ setCentralWidget()
├─ QWidget
│   ├─ setLayout()
│   └─ setStyleSheet()
├─ QVBoxLayout
│   └─ addWidget()
├─ QPushButton
│   └─ clicked.connect()
├─ QLabel
│   └─ setText()
├─ QLineEdit
│   ├─ setPlaceholderText()
│   └─ text()
├─ QTextEdit
│   └─ append()
├─ QSlider
│   ├─ setMinimum()
│   ├─ setMaximum()
│   ├─ setValue()
│   └─ valueChanged.connect()
│
PySide6.QtCore
│
├─ QTimer
│   ├─ timeout.connect()
│   ├─ start()
│   └─ stop()
├─ QPropertyAnimation
│   ├─ setDuration()
│   ├─ setStartValue()
│   ├─ setEndValue()
│   ├─ setEasingCurve()
│   └─ start()
├─ QEasingCurve
├─ QPoint
├─ QRect
├─ Property
├─ Qt
│
PySide6.QtGui
│
├─ QColor
├─ QPainter
```

---

> Для любого класса или функции смотри описание выше: это поможет быстро понять, для чего она используется в проекте.
