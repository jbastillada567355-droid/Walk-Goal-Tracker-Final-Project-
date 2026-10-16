from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox

class ReminderDialog(QDialog):
    def __init__(self, goals, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Goal Reminder")
        self.resize(350, 200)
        self.goals = goals
        self.init_ui()

    def init_ui(self):
        form_layout = QVBoxLayout(self)

        if not self.goals:
            status_text = "<b>Status:</b> No existing goals found. Time to make one!"
        else:
            all_completed = True
            for goal in self.goals:
                total = int(goal["days"]) * float(goal["distance"])
                logged = float(goal["logged_distance"])
                if logged < total:
                    all_completed = False
                    break

            if all_completed:
                status_text = "<b>Status:</b> All goals are completed! Great job!"
            else:
                status_text = "<b>Status:</b> You have active goals remaining. Don't give up!"

        self.status_label = QLabel(status_text)
        self.status_label.setWordWrap(True)
        form_layout.addWidget(self.status_label)

        if self.goals:
            details = "<b>Your Current Goals:</b><br>"
            for g in self.goals:
                total = int(g["days"]) * float(g["distance"])
                logged = float(g["logged_distance"])
                details += f"- {g['title']}: {logged} / {total} km<br>"
            self.details_label = QLabel(details)
            self.details_label.setWordWrap(True)
            form_layout.addWidget(self.details_label)

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.button_box.accepted.connect(self.accept)
        form_layout.addWidget(self.button_box)