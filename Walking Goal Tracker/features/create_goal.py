from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QDialogButtonBox, QMessageBox

class CreateGoal(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Goal")
        self.init_ui()


    def init_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        self.title_input = QLineEdit()
        self.days_input = QLineEdit()
        self.distance_input = QLineEdit()

        form_layout.addRow("Title of Goal", self.title_input)
        form_layout.addRow("Days of Goal", self.days_input)
        form_layout.addRow("Distance(km) each Day", self.distance_input)
        layout.addLayout(form_layout)

        self.button = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.validate_and_accept)
        self.button.rejected.connect(self.reject)
        layout.addWidget(self.button)


    def validate_and_accept(self):
        if not self.title_input.text().strip() or not self.days_input.text().strip() or not self.distance_input.text().strip():
            QMessageBox.critical(self, "Input Error", "Please enter required fields.")
            return
        if not self.days_input.text().strip().isdigit():
            QMessageBox.critical(self, "Input Error", "Days must be whole number.")
            return
        try:
            float(self.distance_input.text().strip())
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Distance must be valid number.")
            return
        self.accept()


    def get_data(self):
        return {
            "title": self.title_input.text().strip(),
            "days": int(self.days_input.text().strip()),
            "distance": float(self.distance_input.text().strip())
        }