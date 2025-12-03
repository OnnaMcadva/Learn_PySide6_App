import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QLabel, QMessageBox, QFileDialog, QColorDialog, QLineEdit, QHBoxLayout
)
from PySide6.QtGui import QColor, QScreen
from PySide6.QtCore import Qt


SKODA_GREEN = "#279107"
SKODA_DARK = "#000000"
SKODA_LIGHT = "#F5F5F5"
SKODA_HOVER = "#35AC0D"


class DialogTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YOLO Detect Train")
        self.resize(550, 380)

        # ---- center the window ----
        screen = QApplication.primaryScreen().geometry()
        self.move(
            (screen.width() - self.width()) // 2,
            (screen.height() - self.height()) // 2
        )

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        central_widget.setLayout(layout)

        # ---- header ----
        title = QLabel("YOLO Detect Train")
        title.setStyleSheet(f"""
            QLabel {{
                font-size: 24px;
                font-weight: bold;
                color: {SKODA_DARK};
                padding: 10px;
            }}
        """)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # ---- form for data= … ----
        self.inputs = {}
        form_fields = ["data", "model", "epochs", "imgsz", "device"]

        for field in form_fields:
            hl = QHBoxLayout()
            lbl = QLabel(f"{field}:")
            lbl.setMinimumWidth(70)
            edit = QLineEdit()
            edit.setPlaceholderText(f"Enter {field}...")
            hl.addWidget(lbl)
            hl.addWidget(edit)
            layout.addLayout(hl)
            self.inputs[field] = edit

        # ---- buttons ----
        self.file_btn = QPushButton("Choose File")
        self.file_btn.clicked.connect(self.open_file)
        layout.addWidget(self.file_btn)

        self.folder_btn = QPushButton("Choose Folder")
        self.folder_btn.clicked.connect(self.open_folder)
        layout.addWidget(self.folder_btn)

        # ---- result label ----
        self.result_label = QLabel("Results will be displayed here")
        self.result_label.setStyleSheet(f"""
            QLabel {{
                background-color: {SKODA_LIGHT};
                border: 2px solid #ccc;
                padding: 10px;
                border-radius: 5px;
            }}
        """)
        layout.addWidget(self.result_label)

        # ---- styles for all buttons ----
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {SKODA_GREEN};
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: {SKODA_HOVER};
            }}
            QPushButton:pressed {{
                background-color: {SKODA_DARK};
            }}
        """)

    # ---------------------------
    #       functionality
    # ---------------------------

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
