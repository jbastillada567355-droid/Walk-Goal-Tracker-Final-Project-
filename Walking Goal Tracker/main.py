import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QMessageBox, QLineEdit, QProgressBar, QCheckBox, QComboBox)

from features.create_goal import CreateGoal
from features.edit_goal import EditGoal
from features.progress import LogProgress
from features.reminder import ReminderDialog
from database.database import Database


class GoalTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goal Tracker")
        self.resize(900, 600)

        self.db = Database()
        self.db.initialize_database()

        self.init_ui()
        self.refresh_table()

        self.check_reminder()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # search
        search_layout = QHBoxLayout()
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search Goals..")
        self.search.setStyleSheet("""
                    QLineEdit {
                        color: #ffffff;
                        font-style: italic;
                    }
                    QLineEdit::placeholder {
                        color: #aaaaaa;
                        font-style: italic;
                    }
                """)
        self.search.textChanged.connect(self.filter)
        search_layout.addWidget(self.search)

        # filter
        self.button_filter = QPushButton("Show Completed Only")
        self.button_filter.setCheckable(True)
        self.button_filter.clicked.connect(self.toggle_completed_filter)
        search_layout.addWidget(self.button_filter)

        # sort
        self.sort_combo = QComboBox()
        self.sort_combo.addItems([
            "Sort by: Default",
            "Title (A-Z)",
            "Total Distance",
            "Distance Walked",
            "Progress"
        ])
        self.sort_combo.currentIndexChanged.connect(self.refresh_table)
        search_layout.addWidget(self.sort_combo)

        main_layout.addLayout(search_layout)

        # table (Columns: Title, Target, Progress Bar, Status)
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Title", "Total Target", "Distance Walked", "Progress", "Completed"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        main_layout.addWidget(self.table)

        # buttons
        button_layout = QHBoxLayout()
        self.button_create = QPushButton("Create Goal")
        self.button_edit = QPushButton("Edit Goal")
        self.button_log = QPushButton("Log Progress")
        self.button_delete = QPushButton("Delete Goal")

        self.button_create.clicked.connect(self.create_goal)
        self.button_edit.clicked.connect(self.edit_goal)
        self.button_log.clicked.connect(self.log_progress)
        self.button_delete.clicked.connect(self.delete_goal)

        button_layout.addWidget(self.button_create)
        button_layout.addWidget(self.button_edit)
        button_layout.addWidget(self.button_log)
        button_layout.addWidget(self.button_delete)
        main_layout.addLayout(button_layout)

    def filter(self, search_text=""):
        search_text = search_text.lower()
        show_completed_only = self.button_filter.isChecked()

        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)
            if not item:
                continue
            match = search_text in item.text().lower()
            checkbox_widget = self.table.cellWidget(row, 4)
            checkbox = checkbox_widget.findChild(QCheckBox) if checkbox_widget else None
            is_completed = checkbox.isChecked() if checkbox else False

            if show_completed_only and not is_completed:
                self.table.setRowHidden(row, True)
            elif not match:
                self.table.setRowHidden(row, True)
            else:
                self.table.setRowHidden(row, False)

    def toggle_completed_filter(self):
        if self.button_filter.isChecked():
            self.button_filter.setText("Show All Goals")
        else:
            self.button_filter.setText("Show Completed Only")
        self.filter(self.search.text())

    def refresh_table(self):
        self.table.setRowCount(0)
        self.goals = self.db.get_all_goals()

        sort_index = self.sort_combo.currentIndex() if hasattr(self, "sort_combo") else 0
        if sort_index == 1:
            self.goals.sort(key=lambda x: x["title"].lower())
        elif sort_index == 2:
            self.goals.sort(key=lambda x: int(x["days"]) * float(x["distance"]), reverse=True)
        elif sort_index == 3:
            self.goals.sort(key=lambda x: float(x["logged_distance"]), reverse=True)
        elif sort_index == 4:
            def get_progress(g):
                total = int(g["days"]) * float(g["distance"])
                return (float(g["logged_distance"]) / total) if total > 0 else 0

            self.goals.sort(key=get_progress, reverse=True)

        for row_id, goal in enumerate(self.goals):
            self.table.insertRow(row_id)

            title = goal["title"]
            total_distance = int(goal["days"]) * float(goal["distance"])
            logged_distance = float(goal["logged_distance"])

            self.table.setItem(row_id, 0, QTableWidgetItem(title))
            self.table.setItem(row_id, 1, QTableWidgetItem(f"{total_distance} km"))
            self.table.setItem(row_id, 2, QTableWidgetItem(f"{logged_distance} km"))

            # progress Bar
            progress_bar = QProgressBar()
            progress_bar.setRange(0, 100)
            percentage = int((logged_distance / total_distance) * 100) if total_distance > 0 else 0
            progress_bar.setValue(min(percentage, 100))
            progress_bar.setStyleSheet("""
                            QProgressBar {
                                border: 1px solid #3a3b3f;
                                border-radius: 4px;
                                background-color: #1a1b1f;
                                text-align: center;
                                color: #ffffff;
                            }
                            QProgressBar::chunk {
                                background-color: #2ecc71;
                                border-radius: 3px;
                            }
                        """)
            self.table.setCellWidget(row_id, 3, progress_bar)

            # checkbox
            checkbox_widget = QWidget()
            checkbox_layout = QHBoxLayout(checkbox_widget)
            checkbox = QCheckBox()
            checkbox.setChecked(logged_distance >= total_distance > 0)
            checkbox.setEnabled(False)
            checkbox_layout.addWidget(checkbox)
            checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            self.table.setCellWidget(row_id, 4, checkbox_widget)

        if hasattr(self, 'search'):
            self.filter(self.search.text())

    def check_reminder(self):
        goals = self.db.get_all_goals()
        dialog = ReminderDialog(goals, self)
        dialog.exec()

    def create_goal(self):
        create = CreateGoal(self)
        if create.exec():
            data = create.get_data()
            self.db.save_goal(data["title"], data["days"], data["distance"])
            self.refresh_table()

    def edit_goal(self):
        selected_row = self.table.currentRow()
        if selected_row < 0 or selected_row >= len(self.goals):
            QMessageBox.warning(self, "No Selection", "Please select a goal")
            return

        old_goal_data = self.goals[selected_row]
        edit = EditGoal(old_goal_data, self)

        if edit.exec():
            new_data = edit.get_data()
            self.db.update_goal(old_goal_data["title"], new_data["title"], new_data["days"], new_data["distance"])
            self.refresh_table()

    def log_progress(self):
        selected_row = self.table.currentRow()
        if selected_row < 0 or selected_row >= len(self.goals):
            QMessageBox.warning(self, "No Selection", "Please select a goal to log progress for")
            return

        goal_data = self.goals[selected_row]
        log_dialog = LogProgress(goal_data["title"], self)
        if log_dialog.exec():
            added_distance = log_dialog.get_data()
            self.db.update_progress(goal_data["title"], added_distance)
            self.refresh_table()

    def delete_goal(self):
        selected_row = self.table.currentRow()
        if selected_row < 0 or selected_row >= len(self.goals):
            QMessageBox.warning(self, "No Selection", "Please select a goal")
            return

        target_title = self.goals[selected_row]["title"]
        confirmation = QMessageBox.question(
            self, "Confirm Delete", f"Delete {target_title}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirmation == QMessageBox.StandardButton.Yes:
            self.db.delete_goal(target_title)
            self.refresh_table()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    dark_theme = QPalette()
    dark_background = QColor("#222429")
    dark_background_inputs = QColor("#1a1b1f")
    text_color = QColor("#ffffff")
    selected_color_blueish = QColor("#273252")
    disabled_color = QColor("#2a2b2e")

    dark_theme.setColor(QPalette.ColorRole.Window, dark_background)
    dark_theme.setColor(QPalette.ColorRole.WindowText, text_color)
    dark_theme.setColor(QPalette.ColorRole.Base, dark_background_inputs)
    dark_theme.setColor(QPalette.ColorRole.Text, text_color)
    dark_theme.setColor(QPalette.ColorRole.Button, dark_background)
    dark_theme.setColor(QPalette.ColorRole.ButtonText, text_color)
    dark_theme.setColor(QPalette.ColorRole.Highlight, selected_color_blueish)
    dark_theme.setColor(QPalette.ColorRole.HighlightedText, text_color)

    app.setPalette(dark_theme)
    window = GoalTracker()
    window.show()
    sys.exit(app.exec())
