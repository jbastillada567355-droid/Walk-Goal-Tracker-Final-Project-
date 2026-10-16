from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QDialogButtonBox, QMessageBox

class LogProgress(QDialog):
    def __init__(self, goal_title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Log Progress: {goal_title}")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        self.added_distance_input = QLineEdit()
        self.added_distance_input.setPlaceholderText("e.g. 4.5")
        form_layout.addRow("Add Distance (km)", self.added_distance_input)
        layout.addLayout(form_layout)

        self.button = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.validate_and_accept)
        self.button.rejected.connect(self.reject)
        layout.addWidget(self.button)

    def validate_and_accept(self):
        text = self.added_distance_input.text().strip()
        if not text:
            QMessageBox.critical(self, "Input Error", "Please enter a distance value.")
            return
        try:
            val = float(text)
            if val < 0:
                raise ValueError()
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Distance must be a valid positive number.")
            return
        self.accept()

    def get_data(self):
        return float(self.added_distance_input.text().strip())