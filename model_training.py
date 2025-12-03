import sys
import os
import yaml
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QLabel, QFileDialog, QLineEdit, QHBoxLayout, QMessageBox, QComboBox
)
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt


# --- ŠKODA brand colors ---
SKODA_GREEN  = "#4BA82E"
SKODA_GREEN2 = "#5CC13A"
SKODA_DARK   = "#1A1A1A"
SKODA_GRAY   = "#E5E5E5"
SKODA_LIGHT  = "#F7F7F7"
SKODA_HOVER  = "#3f8f22"


class DialogTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YOLO Detect Train")
        self.resize(600, 520)

        # ---- Center window/obrazovka ----
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

        # ---- Title ----
        title = QLabel("ŠKODA — YOLO Detect Train")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(f"""
            QLabel {{
                font-size: 26px;
                font-weight: bold;
                padding: 12px;
                color: {SKODA_GREEN};
            }}
        """)
        layout.addWidget(title)

        # ---- Input form ----
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

        # --- Automatic scanning for available models ---
        model_title = QLabel("Available models:")
        model_title.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(model_title)

        self.model_list = QComboBox()
        self.scan_models()
        layout.addWidget(self.model_list)

        # ---- Select data.yaml file ----
        self.file_btn = QPushButton("Select data.yaml file")
        self.file_btn.clicked.connect(self.open_file)
        layout.addWidget(self.file_btn)

        # ---- Select images folder ----
        self.folder_btn = QPushButton("Select images folder")
        self.folder_btn.clicked.connect(self.open_folder)
        layout.addWidget(self.folder_btn)

        # ---- Save configuration to YAML ----
        self.save_yaml_btn = QPushButton("Save configuration to YAML")
        self.save_yaml_btn.clicked.connect(self.save_yaml)
        layout.addWidget(self.save_yaml_btn)

        # ---- Run YOLO training ----
        self.run_btn = QPushButton("Run YOLO training")
        self.run_btn.clicked.connect(self.run_training)
        layout.addWidget(self.run_btn)

        # ---- Result output ----
        self.result_label = QLabel("Results will be shown here")
        self.result_label.setStyleSheet(f"""
            QLabel {{
                background-color: {SKODA_LIGHT};
                border: 2px solid #ccc;
                padding: 12px;
                border-radius: 7px;
                margin-top: 12px;
            }}
        """)
        layout.addWidget(self.result_label)

        # ---- ŠKODA style ----
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {SKODA_GREEN};
                color: white;
                border: none;
                padding: 10px;
                border-radius: 6px;
                font-size: 15px;
            }}
            QPushButton:hover {{
                background-color: {SKODA_HOVER};
            }}
            QPushButton:pressed {{
                background-color: {SKODA_DARK};
            }}
        """)

    # ------------------------------------------------
    #                GUI FUNCTIONS
    # ------------------------------------------------

    def scan_models(self):
        """Reads .pt models from ./models"""
        self.model_list.clear()
        model_path = "./models"

        if not os.path.exists(model_path):
            os.makedirs(model_path)

        files = [f for f in os.listdir(model_path) if f.endswith(".pt")]

        if files:
            self.model_list.addItems(files)
        else:
            self.model_list.addItem("(No .pt files)")
        
    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select data.yaml file", "", "YAML (*.yaml *.yml)")
        if path:
            self.inputs["data"].setText(path)
            self.result_label.setText(f"Selected file: {path}")
        else:
            self.result_label.setText("No file selected")

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select folder")
        if folder:
            self.result_label.setText(f"Selected folder: {folder}")
        else:
            self.result_label.setText("No folder selected")

    # -------- Save YAML --------
    def save_yaml(self):
        cfg = {
            key: self.inputs[key].text() for key in self.inputs
        }

        path, _ = QFileDialog.getSaveFileName(self, "Save configuration", "train_config.yaml", "YAML (*.yaml)")
        if not path:
            return

        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(cfg, f, allow_unicode=True)

        self.result_label.setText(f"Configuration saved to: {path}")

    # ---------- Run training ----------
    def run_training(self):
        vals = {key: self.inputs[key].text() for key in self.inputs}

        # If user selected model from list, use it
        if self.model_list.count() > 0 and self.model_list.currentText() != "(No .pt files)":
            vals["model"] = "./models/" + self.model_list.currentText()

        # Check required fields
        if not vals["data"] or not vals["model"]:
            QMessageBox.warning(self, "Error", "You must specify data= and model=")
            return

        # Generate command
        cmd = (
            f"yolo detect train "
            f"data={vals['data']} "
            f"model={vals['model']} "
            f"epochs={vals['epochs'] or '100'} "
            f"imgsz={vals['imgsz'] or '640'} "
            f"device={vals['device'] or '0'}"
        )

        self.result_label.setText(f"Generated command:\n{cmd}")

        QMessageBox.information(self, "YOLO Command", f"Command:\n{cmd}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DialogTestWindow()
    window.show()
    sys.exit(app.exec())
