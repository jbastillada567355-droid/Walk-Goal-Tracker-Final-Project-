import sys

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QMessageBox, QLineEdit)

from features.create_goal import CreateGoal
from features.edit_goal import EditGoal
from database.database import Database


class GoalTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goal Tracker")
        self.resize(800, 600)

        self.db = Database()
        self.db.initialize_database()

        self.init_ui()
        self.refresh_table()

    #UI (table, buttons, search)
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        # search
        search_layout = QHBoxLayout()
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search Goals..")
        self.search.textChanged.connect(self.filter)
        search_layout.addWidget(self.search)
        main_layout.addLayout(search_layout)

        #table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Title", "Days", "Distance", "Total Distance Target"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        main_layout.addWidget(self.table)
        #buttons
        button_layout = QHBoxLayout()
        self.button_create = QPushButton("Create Goal")
        self.button_edit = QPushButton("Edit Selected Goal")
        self.button_delete = QPushButton("Delete Selected Goal")

        self.button_create.clicked.connect(self.create_goal)
        self.button_edit.clicked.connect(self.edit_goal)
        self.button_delete.clicked.connect(self.delete_goal)

        button_layout.addWidget(self.button_create)
        button_layout.addWidget(self.button_edit)
        button_layout.addWidget(self.button_delete)
        main_layout.addLayout(button_layout)

    #filter (connected to search)
    def filter(self, search):
        for row in range(self.table.rowCount()):
            if search.lower() in self.table.item(row,0).text().lower():
                self.table.setRowHidden(row, False)
            elif search.lower() not in self.table.item(row, 0).text().lower():
                self.table.setRowHidden(row, True)

    #restart table if something changed
    def refresh_table(self):
        self.table.setRowCount(0)
        self.goals = self.db.get_all_goals()
        # loop trough table
        for row_id, goal in enumerate(self.goals):
            self.table.insertRow(row_id)
            self.table.setItem(row_id, 0, QTableWidgetItem(goal["title"]))
            self.table.setItem(row_id, 1, QTableWidgetItem(str(goal["days"])))
            self.table.setItem(row_id, 2, QTableWidgetItem(str(goal["distance"])))
            total_distance = int(goal["days"]) * float(goal["distance"])
            self.table.setItem(row_id, 3, QTableWidgetItem(str(total_distance)))

    #create
    def create_goal(self):
        create = CreateGoal(self)
        if create.exec():
            data = create.get_data()
            self.db.save_goal(data["title"], data["days"], data["distance"])
            self.refresh_table()

    #update
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

    #delete
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
    #dark_theme
    app.setStyle("Fusion")
    dark_theme = QPalette()
    dark_background = QColor("#222429")
    dark_background_inputs = QColor("#1a1b1f")
    text_color = QColor("#ffffff")
    selected_color = QColor("#2f3033")
    selected_color_blueish = QColor("#273252")
    disabled_color = QColor("#2a2b2e")

    dark_theme.setColor(QPalette.ColorRole.Window, dark_background)
    dark_theme.setColor(QPalette.ColorRole.WindowText, text_color)
    dark_theme.setColor(QPalette.ColorRole.Base, dark_background_inputs)
    dark_theme.setColor(QPalette.ColorRole.AlternateBase, dark_background)
    dark_theme.setColor(QPalette.ColorRole.ToolTipBase, text_color)
    dark_theme.setColor(QPalette.ColorRole.ToolTipText, text_color)
    dark_theme.setColor(QPalette.ColorRole.Text, text_color)
    dark_theme.setColor(QPalette.ColorRole.Button, dark_background)
    dark_theme.setColor(QPalette.ColorRole.ButtonText, text_color)
    dark_theme.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    dark_theme.setColor(QPalette.ColorRole.PlaceholderText, text_color)
    dark_theme.setColor(QPalette.ColorRole.Highlight, selected_color_blueish)
    dark_theme.setColor(QPalette.ColorRole.HighlightedText, text_color)
    dark_theme.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, disabled_color)
    dark_theme.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, disabled_color)
    dark_theme.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, disabled_color)
    dark_theme.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, disabled_color)

    app.setPalette(dark_theme)
    window = GoalTracker()
    window.show()
    sys.exit(app.exec())