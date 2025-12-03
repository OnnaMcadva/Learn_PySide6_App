import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QLabel, QFileDialog, QLineEdit, QHBoxLayout
)
from PySide6.QtGui import QScreen, QFont, QPalette, QColor
from PySide6.QtCore import Qt

class DialogTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLO Detect Train")
        self.resize(560, 420)

        # ───── Исправляем центрирование под любой DPI и мультимонитор ─────
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()  # именно availableGeometry!
        center_x = (screen_geometry.width() - self.width()) // 2 + screen_geometry.x()
        center_y = (screen_geometry.height() - self.height()) // 2 + screen_geometry.y()
        self.move(center_x, center_y)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(16)
        layout.setContentsMargins(32, 32, 32, 32)
        central_widget.setLayout(layout)

        # ───── Заголовок ─────
        title = QLabel("YOLO Detect Train")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("bigTitle")
        layout.addWidget(title)

        # ───── Поля ввода ─────
        self.inputs = {}
        form_fields = ["data", "model", "epochs", "imgsz", "device"]
        for field in form_fields:
            hl = QHBoxLayout()
            lbl = QLabel(f"{field}:")
            lbl.setMinimumWidth(80)
            edit = QLineEdit()
            edit.setPlaceholderText(f"Enter {field}...")
            hl.addWidget(lbl)
            hl.addWidget(edit)
            layout.addLayout(hl)
            self.inputs[field] = edit

        # ───── Кнопки ─────
        self.file_btn = QPushButton("Choose File")
        self.file_btn.clicked.connect(self.open_file)
        layout.addWidget(self.file_btn)

        self.folder_btn = QPushButton("Choose Folder")
        self.folder_btn.clicked.connect(self.open_folder)
        layout.addWidget(self.folder_btn)

        # ───── Результат ─────
        self.result_label = QLabel("Results will be displayed here")
        self.result_label.setWordWrap(True)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setMinimumHeight(80)
        self.result_label.setObjectName("resultBox")
        layout.addWidget(self.result_label)

        # ───── КРАСИВОЕ ОФОРМЛЕНИЕ — ТОЛЬКО РАБОЧИЕ СВОЙСТВА Qt! ─────
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #e8f5f8, stop:0.5 #f0f9f5, stop:1 #f5e8f8);
                font-family: "Segoe UI", "Roboto", sans-serif;
            }
            
            QLabel#bigTitle {
                font-size: 34px;
                font-weight: 700;
                color: #2d6a4f;
                padding: 10px;
                margin-bottom: 10px;
            }
            
            QLabel {
                color: #1a535c;
                font-size: 14px;
                font-weight: 500;
            }
            
            QLineEdit {
                padding: 12px 16px;
                border: 2px solid #a0d6db;
                border-radius: 14px;
                background-color: #ffffff;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #52b788;
                background-color: #f8fffe;
            }
            
            QPushButton {
                background-color: #74c69d;
                color: white;
                border: none;
                padding: 14px;
                border-radius: 16px;
                font-size: 15px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #95d5b2;
            }
            QPushButton:pressed {
                background-color: #52b788;
            }
            
            #resultBox {
                background-color: rgba(255, 255, 255, 0.92);
                border: 1px solid #cfe8e8;
                border-radius: 18px;
                padding: 20px;
                font-size: 15px;
                color: #1a535c;
            }
        """)

        # Более приятный системный шрифт
        app.setFont(QFont("Segoe UI", 10))

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Choose File", "", "All Files (*);;Text Files (*.txt)"
        )
        if file_path:
            self.result_label.setText(f"Selected file: {file_path}")
        else:
            self.result_label.setText("No file selected")

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Choose Folder")
        if folder_path:
            self.result_label.setText(f"Selected folder: {folder_path}")
        else:
            self.result_label.setText("No folder selected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DialogTestWindow()
    window.show()
    sys.exit(app.exec())