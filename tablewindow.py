import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QTableWidget, QTableWidgetItem, QPushButton,
                              QHeaderView, QMenu, QInputDialog)
from PySide6.QtCore import Qt

class TableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тест таблицы")
        self.setGeometry(100, 100, 800, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Создаем таблицу
        self.table = QTableWidget(5, 3)
        self.table.setHorizontalHeaderLabels(["Имя", "Возраст", "Город"])
        
        # Заполняем тестовыми данными
        test_data = [
            ["María", "25", "Madrid"],
            ["Juan", "30", "Barcelona"],
            ["Lucía", "22", "Valencia"],
            ["Pedro", "35", "Sevilla"],
            ["Carmen", "28", "Zaragoza"]
        ]
        
        for row, data in enumerate(test_data):
            for col, value in enumerate(data):
                self.table.setItem(row, col, QTableWidgetItem(value))
        
        # Настраиваем растягивание колонок
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        layout.addWidget(self.table)
        
        # Кнопки управления
        btn_layout = QVBoxLayout()
        
        add_btn = QPushButton("Добавить строку")
        add_btn.clicked.connect(self.add_row)
        btn_layout.addWidget(add_btn)
        
        remove_btn = QPushButton("Удалить выбранную строку")
        remove_btn.clicked.connect(self.remove_row)
        btn_layout.addWidget(remove_btn)
        
        layout.addLayout(btn_layout)
        
        # Включаем контекстное меню
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.show_context_menu)
    
    def add_row(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
    
    def remove_row(self):
        current_row = self.table.currentRow()
        if current_row >= 0:
            self.table.removeRow(current_row)
    
    def show_context_menu(self, position):
        menu = QMenu()
        
        edit_action = menu.addAction("Редактировать")
        delete_action = menu.addAction("Удалить")
        add_action = menu.addAction("Добавить строку")
        
        action = menu.exec_(self.table.mapToGlobal(position))
        
        if action == edit_action:
            self.edit_cell()
        elif action == delete_action:
            self.remove_row()
        elif action == add_action:
            self.add_row()
    
    def edit_cell(self):
        current_row = self.table.currentRow()
        current_col = self.table.currentColumn()
        
        if current_row >= 0 and current_col >= 0:
            current_item = self.table.item(current_row, current_col)
            if current_item:
                new_text, ok = QInputDialog.getText(
                    self, "Редактирование",
                    "Введите новое значение:",
                    text=current_item.text()
                )
                if ok and new_text:
                    current_item.setText(new_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableWindow()
    window.show()
    sys.exit(app.exec())
