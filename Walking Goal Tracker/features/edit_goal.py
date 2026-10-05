from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QDialogButtonBox, QMessageBox

class EditGoal(QDialog):
    def __init__(self, current_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Goal")
        self.current_data = current_data
        self.init_ui()
        self.populate_data()


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

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.validate_and_accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)


    def populate_data(self):
        self.title_input.setText(self.current_data['title'])
        self.days_input.setText(str(self.current_data['days']))
        self.distance_input.setText(str(self.current_data['distance']))


    def validate_and_accept(self):
        if not self.title_input.text().strip() or not self.days_input.text().strip() or not self.distance_input.text().strip():
            QMessageBox.critical(self, "Input Error", "Please enter required fields.")
            return
        if not self.days_input.text().strip().isdigit():
            QMessageBox.critical(self, "Input Error", "Days must be whole number.")
            return
        try:
            float(self.days_input.text().strip())
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