import sys
import os
import yaml
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QLabel, QFileDialog, QLineEdit, QHBoxLayout, QMessageBox, QComboBox
)
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt


# --- фирменные цвета ŠKODA ---
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

        # ---- центрируем окно ----
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

        # ---- Заголовок ----
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

        # ---- форма ввода параметров ----
        self.inputs = {}
        form_fields = ["data", "model", "epochs", "imgsz", "device"]

        for field in form_fields:
            hl = QHBoxLayout()
            lbl = QLabel(f"{field}:")
            lbl.setMinimumWidth(80)
            edit = QLineEdit()
            edit.setPlaceholderText(f"Введите {field}...")
            hl.addWidget(lbl)
            hl.addWidget(edit)
            layout.addLayout(hl)
            self.inputs[field] = edit

        # --- Автоматическое чтение доступных моделей ---
        model_title = QLabel("Доступные модели:")
        model_title.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(model_title)

        self.model_list = QComboBox()
        self.scan_models()
        layout.addWidget(self.model_list)

        # ---- кнопка выбора файла ----
        self.file_btn = QPushButton("Выбрать файл data.yaml")
        self.file_btn.clicked.connect(self.open_file)
        layout.addWidget(self.file_btn)

        # ---- кнопка выбора папки ----
        self.folder_btn = QPushButton("Выбрать папку с изображениями")
        self.folder_btn.clicked.connect(self.open_folder)
        layout.addWidget(self.folder_btn)

        # ---- кнопка сохранения в YAML ----
        self.save_yaml_btn = QPushButton("Сохранить конфигурацию в YAML")
        self.save_yaml_btn.clicked.connect(self.save_yaml)
        layout.addWidget(self.save_yaml_btn)

        # ---- кнопка запуска тренировки ----
        self.run_btn = QPushButton("Запустить тренировку YOLO")
        self.run_btn.clicked.connect(self.run_training)
        layout.addWidget(self.run_btn)

        # ---- метка результата ----
        self.result_label = QLabel("Результаты будут отображаться здесь")
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

        # ---- стили Škoda ----
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
    #                ФУНКЦИИ GUI
    # ------------------------------------------------

    def scan_models(self):
        """Читает модели из папки ./models"""
        self.model_list.clear()
        model_path = "./models"

        if not os.path.exists(model_path):
            os.makedirs(model_path)

        files = [f for f in os.listdir(model_path) if f.endswith(".pt")]

        if files:
            self.model_list.addItems(files)
        else:
            self.model_list.addItem("(Нет файлов .pt)")
        
    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Выберите файл data.yaml", "", "YAML (*.yaml *.yml)")
        if path:
            self.inputs["data"].setText(path)
            self.result_label.setText(f"Выбран файл: {path}")
        else:
            self.result_label.setText("Файл не выбран")

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder:
            self.result_label.setText(f"Выбрана папка: {folder}")
        else:
            self.result_label.setText("Папка не выбрана")

    # -------- сохранение YAML --------
    def save_yaml(self):
        cfg = {
            key: self.inputs[key].text() for key in self.inputs
        }

        # Предлагаем сохранить файл
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить конфигурацию", "train_config.yaml", "YAML (*.yaml)")
        if not path:
            return

        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(cfg, f, allow_unicode=True)

        self.result_label.setText(f"Конфигурация сохранена в: {path}")

    # ---------- запуск тренировки ----------
    def run_training(self):
        vals = {key: self.inputs[key].text() for key in self.inputs}

        # Если пользователь выбрал модель из списка — подставим её
        if self.model_list.count() > 0 and self.model_list.currentText() != "(Нет файлов .pt)":
            vals["model"] = "./models/" + self.model_list.currentText()

        # Проверка
        if not vals["data"] or not vals["model"]:
            QMessageBox.warning(self, "Ошибка", "Нужно указать data= и model=")
            return

        # Генерация команды
        cmd = (
            f"yolo detect train "
            f"data={vals['data']} "
            f"model={vals['model']} "
            f"epochs={vals['epochs'] or '100'} "
            f"imgsz={vals['imgsz'] or '640'} "
            f"device={vals['device'] or '0'}"
        )

        self.result_label.setText(f"Сгенерирована команда:\n{cmd}")

        # Здесь можно запускать выполнение:
        # os.system(cmd)
        # но пока просто показываем

        QMessageBox.information(self, "Команда YOLO", f"Команда:\n{cmd}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DialogTestWindow()
    window.show()
    sys.exit(app.exec())
