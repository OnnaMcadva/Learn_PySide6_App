import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit, QFileDialog, QCheckBox,
    QDoubleSpinBox, QTextEdit, QSpinBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class YOLOTrainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLO Detect Train")
        self.resize(600, 600)

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        center_x = (screen_geometry.width() - self.width()) // 2 + screen_geometry.x()
        center_y = (screen_geometry.height() - self.height()) // 2 + screen_geometry.y()
        self.move(center_x, center_y)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(12)
        layout.setContentsMargins(24, 24, 24, 24)
        central_widget.setLayout(layout)

        title = QLabel("YOLO Detect Train")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("bigTitle")
        layout.addWidget(title)

        self.fields = {}

        # 1. Dataset folder
        self._add_file_selector(layout, "Dataset", "Choose dataset folder", folder=True)

        # 2. OUT folder
        self._add_file_selector(layout, "OUTFolder", "Choose output folder", folder=True)

        # 3. Model name
        self._add_text_input(layout, "Model Name", "String")

        # 4. Train full model (Yes/No)
        self._add_checkbox(layout, "Train full model")

        # 5. Epochs
        self._add_int_input(layout, "Epochs", 1, 1000, default=100)

        # 6. Batch size
        self._add_int_input(layout, "Batch size", 1, 128, default=16)

        # 7. Validation split
        self._add_float_input(layout, "Val", 0.0, 1.0, step=0.01, default=0.2)

        # 8. Test split
        self._add_float_input(layout, "Test", 0.0, 1.0, step=0.01, default=0.1)

        # 9. Train button
        train_btn = QPushButton("TRAIN!")
        train_btn.clicked.connect(self.start_training)
        layout.addWidget(train_btn)

        # 10. Log area
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        self.log_area.setMinimumHeight(150)
        self.log_area.setObjectName("resultBox")
        layout.addWidget(self.log_area)

        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #e8f5f8, stop:0.5 #f0f9f5, stop:1 #f5e8f8);
                font-family: "Segoe UI", "Roboto", sans-serif;
            }
            QLabel#bigTitle {
                font-size: 32px;
                font-weight: 700;
                color: #2d6a4f;
                padding: 8px;
            }
            QLabel {
                color: #1a535c;
                font-size: 14px;
                font-weight: 500;
            }
            QLineEdit, QSpinBox, QDoubleSpinBox {
                padding: 8px 12px;
                border: 2px solid #a0d6db;
                border-radius: 12px;
                background-color: #ffffff;
            }
            QPushButton {
                background-color: #74c69d;
                color: white;
                border: none;
                padding: 12px;
                border-radius: 14px;
                font-size: 15px;
                font-weight: 600;
            }
            QPushButton:hover { background-color: #95d5b2; }
            QPushButton:pressed { background-color: #52b788; }
            QTextEdit#resultBox {
                background-color: rgba(255, 255, 255, 0.92);
                border: 1px solid #cfe8e8;
                border-radius: 14px;
                padding: 12px;
                font-size: 14px;
                color: #1a535c;
            }
        """)
        app.setFont(QFont("Segoe UI", 10))


    def _add_file_selector(self, parent_layout, label_text, button_text, folder=False):
        hl = QHBoxLayout()
        lbl = QLabel(label_text)
        lbl.setMinimumWidth(120)
        line_edit = QLineEdit()
        line_edit.setReadOnly(True)
        btn = QPushButton(button_text)
        if folder:
            btn.clicked.connect(lambda: self._choose_folder(line_edit))
        else:
            btn.clicked.connect(lambda: self._choose_file(line_edit))
        hl.addWidget(btn)
        hl.addWidget(line_edit)
        parent_layout.addLayout(hl)
        self.fields[label_text] = line_edit

    def _choose_file(self, line_edit):
        path, _ = QFileDialog.getOpenFileName(self, "Choose File", "", "All Files (*)")
        if path: line_edit.setText(path)

    def _choose_folder(self, line_edit):
        path = QFileDialog.getExistingDirectory(self, "Choose Folder")
        if path: line_edit.setText(path)

    def _add_text_input(self, parent_layout, label_text, placeholder=""):
        hl = QHBoxLayout()
        lbl = QLabel(label_text)
        lbl.setMinimumWidth(120)
        edit = QLineEdit()
        edit.setPlaceholderText(placeholder)
        hl.addWidget(lbl)
        hl.addWidget(edit)
        parent_layout.addLayout(hl)
        self.fields[label_text] = edit

    def _add_checkbox(self, parent_layout, label_text):
        hl = QHBoxLayout()
        lbl = QLabel(label_text)
        lbl.setMinimumWidth(120)
        checkbox = QCheckBox()
        hl.addWidget(lbl)
        hl.addWidget(checkbox)
        parent_layout.addLayout(hl)
        self.fields[label_text] = checkbox

    def _add_int_input(self, parent_layout, label_text, min_val, max_val, default=0):
        hl = QHBoxLayout()
        lbl = QLabel(label_text)
        lbl.setMinimumWidth(120)
        spin = QSpinBox()
        spin.setRange(min_val, max_val)
        spin.setValue(default)
        hl.addWidget(lbl)
        hl.addWidget(spin)
        parent_layout.addLayout(hl)
        self.fields[label_text] = spin

    def _add_float_input(self, parent_layout, label_text, min_val, max_val, step=0.01, default=0.0):
        hl = QHBoxLayout()
        lbl = QLabel(label_text)
        lbl.setMinimumWidth(120)
        spin = QDoubleSpinBox()
        spin.setRange(min_val, max_val)
        spin.setSingleStep(step)
        spin.setValue(default)
        hl.addWidget(lbl)
        hl.addWidget(spin)
        parent_layout.addLayout(hl)
        self.fields[label_text] = spin

    def start_training(self):
        self.log_area.append("Training started...")

        for key, widget in self.fields.items():
            if isinstance(widget, (QLineEdit, QSpinBox, QDoubleSpinBox)):
                value = widget.text() if isinstance(widget, QLineEdit) else widget.value()
            elif isinstance(widget, QCheckBox):
                value = widget.isChecked()
            self.log_area.append(f"{key}: {value}")
        self.log_area.append("Training finished!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YOLOTrainWindow()
    window.show()
    sys.exit(app.exec())
