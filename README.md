# Walk-Goal-Tracker-Final-Project-
The Walk Goal Tracker System is a desktop application designed to help users create plans, manage, and monitor their daily walks.
When tracking routine fitness tasks, individuals tend to struggle on logging their progress or lose momentum due to disorganized note-keeping.

## Objectives
Store goal targets in a database and to provide an easy-to-use interface.

## Features
- Calculate Total Distance:
    Calculates total distance by multiplying days and distance.
- Goals Table:
    Displays existing goals. Goals can be selected to be edited or deleted.
- Search Goals:
    Search through listed table records based on keystroke matching.
- Filter Completed Goals:
    A feature that allows the user to toggle whether to only show completed goals or all goals.
- Sort Goals:
    Lets the user sort the goals by; title, total distance, distance walked, and completion percentage.
- Log Progress:
    Lets the user manually input the amount of distance the user has covered to record their progress.
- Progress Bar:
    Shows the progress of the user, filling a percentage of the bar based on the user's progress.
- Check Box:
    Automatically check and mark a goal if it is completed.
- Reminder:
    Reminds the user of the unfinished goals that the user has, or if the users has completed all goals.
- Dark Theme:
    Gives the application a dark theme.

## Technologies Used
- Programming Language: Python 3
- GUI Framework/Library: PyQt6
- Database Engine: SQLite
- Theme Styling: PyQt6 Fusion Layout with custom QPalette colors

## Project Structure
```text
my_goal_app/
├── main.py
├── database/
│   └── database.py
└── features/
    ├── create_goal.py
    ├── edit_goal.py
    ├── progress.py
    └── reminder.py
```
### File Descriptions
- main.py:
    Core entry point. Contains the GoalTracker main window class, handles user actions and events, search filtering loops, and visual dark theme configurations
- database.py:
    Holds the Database wrapper class. It handles the SQL and database operations, tracking connections, table definitions, and transactional logic
- create_goal.py:
    Implements CreateGoal. Dialog box provides the input form and validates the user's input
- edit_goal.py:
    Implements EditGoal. Reuses form structures to load existing goal information and allows users to edit it
- progress.py
    Implements LogProgress. A dialog box allowing users to input and append distance walked to their active goal.
- reminder.py
    Implements ReminderDialog. A pop-up dialog displayed on startup of application to show goal progress statuses.

## Installation and Setup
  ### Required Dependencies
  - Python 3.7+
  - PyQt6
  ### Step-by-Step Instructions
  1. Open Terminal or Command Prompt and change directories to the root project folder:
     type into terminal or command prompt:
       cd path/to/my_goal_app
  2. Create a Virtual Environment to separate dependencies safely:
     type into terminal or command prompt:
     - Windows:
         python -m venv venv
         venv\Scripts\activate
     - macOS/Linux:
         python3 -m venv venv
         source venv/bin/activate
  3. Install PyQt6 using pip:
     type into terminal or command prompt:
       pip install PyQt6
  4. Boot the application from the root file tree location:
     type into terminal or command prompt or PyCharm:
       python main.py

## How to Use the System
1. Launch App: Run "python main.py" in terminal or command prompt to open the main window interface.
2. Create Goal: Click Create Goal. Provide a title, total days (whole number), and target daily distance (number or decimal value). Click OK to save.
3. Search: Type inside the Search Goals... input bar to only show existing goals which titles matches with the input.
4. Filter Completed Goals: Click Completed Only to only show the goals that are finished.
5. Sort: Select how you would like the goals to be sorted using the sort combo box.
7. Edit Goal: Select a row in the data grid and click Edit Selected Goal. Adjust title, days, or distance inside the dialog window and save changes. Click OK to save changes.
8. Log Progress: Select a goal row and click Log Progress to input additional distance completed.
9. Delete Goal: Select a target row, click Delete Selected Goal, and confirm your decision on the popup alert prompt.

## OOP Implementation
### Important Classes & Runtime Objects
- GoalTracker (Class): Represents the main window of the application.
- Database (Class): Defines the database connection and handles the database connection and operations.
- app (Object): The master runtime QApplication instance powering global configuration flags and event loop cycles.
- window.db (Object): A persistent instance of the Database class embedded within the main window.
### OOP Principles Applied
- Encapsulation
    The Database class encapsulates configuration settings (self.db_name) and isolates the SQL execution logic from the UI code.
- Inheritance
    The UI classes inherit from PyQt6 classes, allowing the application to reuse existing functionality.
- Polymorphism
    Both CreateGoal and EditGoal have similar methods for handling goal data.

## Database
### Database Structure
  A single-file SQLite database architecture mapped locally to tracker_database.db
### Important tables
  goals: four columns; title, days, distance, logged_distance
### CRUD
- (CREATE) save_goal(): using INSERT OR IGNORE INTO goals. It commits structural records safely and ignores requests if a duplicate primary key title is entered.
- (READ) get_all_goals(): using SELECT title, days, distance FROM goals. Pulls all raw data from storage and parses it into standard Python dictionaries for UI rendering.
- (UPDATE) update_goal(): using UPDATE goals SET... WHERE title=?. Looks up records via their original string key identifier and updates values in-place.
- (UPDATE) update_progress(): updates logged_distance by adding incremental progress values.
- (DELETE) delete_goal(): using DELETE FROM goals WHERE title=?. Permanently drops the selected row matching the specified target title.

## Screenshots
<img width="348" height="230" alt="WalkingGoalTracker_Reminder_DialogBox" src="https://github.com/user-attachments/assets/a75a8dc8-f967-49f4-ad91-07d21b98d6f2" />

**Reminder dialog box**


<img width="894" height="624" alt="WalkingGoalTracker_Table_Window" src="https://github.com/user-attachments/assets/479a8298-f0a3-4cd4-8f7f-2fdee00d7b3a" />

**Main window with goal examples**


<img width="893" height="625" alt="WalkingGoalTracker_Table_UsingSearchBar" src="https://github.com/user-attachments/assets/16ddac6a-5c4a-4a2b-b065-be73c0e33b73" />

**Using the search bar**


<img width="894" height="625" alt="WalkingGoalTracker_Table_FilterCompleted" src="https://github.com/user-attachments/assets/07b11aa7-402e-4fbe-aa28-859f9d41510f" />

**Using Filter button**


<img width="894" height="623" alt="WalkingGoalTracker_Table_UsingSortComboBox" src="https://github.com/user-attachments/assets/a40df696-ed30-4166-a3a3-eba382d8e16a" />

**Using Sort combo box (example: sort by Progress)**


<img width="239" height="166" alt="WalkingGoalTracker_Create_DialogBox" src="https://github.com/user-attachments/assets/1731f8bd-7969-4f10-adde-31e8a530bb54" />

**Create dialog box**


<img width="240" height="166" alt="WalkingGoalTracker_Edit_DialogBox" src="https://github.com/user-attachments/assets/8a2a77d4-3402-46a3-a5d3-2b8f2583f1b1" />

**Edit dialog box**


<img width="190" height="133" alt="WalkingGoalTracker_DeleteConfirmation_DialogBox" src="https://github.com/user-attachments/assets/31018fac-1110-498b-b163-bd2aa13a00e9" />

**Delete confirmation**


<img width="211" height="101" alt="WalkingGoalTracker_LogProgress_DialogBox" src="https://github.com/user-attachments/assets/4ac90267-d7e1-4b9b-bf11-03ae54cc9002" />

**Log Progress dialog box**


## Testing
- Create:
  + valid input:
    * Expected results: accept and save
    * Actual results: accept and save
  + invalid input
    * Expected results: reject and show error message
    * Actual results: reject and show error message
- Edit:
  + valid input
    * Expected results: accept and save changes
    * Actual results: accept and save changes
  + invalid input
    * Expected results: reject and show error message
    * Actual results: reject and show error message
  + press Edit Selected Goal without selecting a goal:
    * Expected results: show error message
    * Actual results: show error message
- Delete:
  + delete goal Yes confirmation
    * Expected results: delete goal
    * Actual results: delete goal
  + delete goal No confirmation
    * Expected results: deletion canceled
    * Actual results: deletion canceled
  + press delete Selected Goal without selecting a goal:
    * Expected results: show error message
    * Actual results: show error message
- Search:
  + search for existing goal:
    * Expected results: show goal
    * Actual results: show goal
  + search for nonexistent goal:
    * Expected results: blank
    * Actual results: blank
   
## Known Issues / Limitations
### Issues
No issues as of now.
### Yet to be implemented
None

## Author
Joshua Marc G. Bastillada
CS26L(35181)
