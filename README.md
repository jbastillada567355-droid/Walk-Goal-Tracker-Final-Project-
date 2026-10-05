# Walk-Goal-Tracker-Final-Project-
The Walk Goal Tracker System is a desktop application designed to help users create plans, manage, and monitor their daily walks.
When tracking routine fitness tasks, individuals tend to struggle on logging their progress or lose momentum due to disorganized note-keeping.

## Objectives
- Store goal targets in a database.
- Provide an easy-to-use interface.

## Features
- Create Goal:
    Gather valid inputs such as title of goal, expected days, and distance(km) each day.
- Edit Goal:
    Modifies existing goal's title, days, and distance(km).
- Delete Goal:
    Removes a goal permanently from the database. 
- Calculate Total Distance:
    Calculates total distance by multiplying days and distance.
- Goals Table:
    Displays existing goals. Goals can be selected to be edited or deleted.
- Search and Filter Goals:
    Filters listed table records based on keystroke matching.
- Dark Theme:
    Gives the application a dark theme.

## Technologies Used
- Programming Language: Python 3
- GUI Framework/Library: PyQt6
- Database Engine: SQLite
- Theme Styling: PyQt6 Fusion Layout with custom QPalette colors

## Project Structure
my_goal_app/
├── main.py
├── database/
│   └── database.py
└── features/
    ├── create_goal.py
    └── edit_goal.py
### File Descriptions
- main.py:
    Core entry point. Contains the GoalTracker main window class, handles user actions and events, search filtering loops, and visual dark theme configurations
- database.py:
    Holds the Database wrapper class. It handles the SQL and database operations, tracking connections, table definitions, and transactional logic
- create_goal.py:
    Implements CreateGoal. Dialog box provides the input form and validates the user's input
- edit_goal.py:
    Implements EditGoal. Reuses form structures to load existing goal information and allows users to edit it

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
3. Search/Filter: Type inside the Search Goals... input bar to filter existing records instantly by title.
4. Edit Goal: Select a row in the data grid and click Edit Selected Goal. Adjust title, days, or distance inside the dialog window and save changes. Click OK to save changes.
5. Delete Goal: Select a target row, click Delete Selected Goal, and confirm your decision on the popup alert prompt.

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
  goals: three columns; title, days, distance
### CRUD
- (CREATE) save_goal(): using INSERT OR IGNORE INTO goals. It commits structural records safely and ignores requests if a duplicate primary key title is entered.
- (READ) get_all_goals(): using SELECT title, days, distance FROM goals. Pulls all raw data from storage and parses it into standard Python dictionaries for UI rendering.
- (UPDATE) update_goal(): using UPDATE goals SET... WHERE title=?. Looks up records via their original string key identifier and updates values in-place.
- (DELETE) delete_goal(): using DELETE FROM goals WHERE title=?. Permanently drops the selected row matching the specified target title.

## Screenshots
<img width="400" height="300" alt="Screenshot 2026-10-06 015330" src="https://github.com/user-attachments/assets/48d8b8b6-d6e8-4e1c-9f23-d0b15bfd4df1" />

**Main window with goal examples**

<img width="400" height="300" alt="Screenshot 2026-10-06 015402" src="https://github.com/user-attachments/assets/c0cffa73-fbb0-4555-8001-17c95ac1e3b2" />

**Using the search bar to filter goals**

<img width="239" height="166" alt="Screenshot 2026-10-06 015051" src="https://github.com/user-attachments/assets/3db1c1de-3744-4a03-8d25-68b2d2d1b052" />

**Create dialog box**

<img width="240" height="166" alt="Screenshot 2026-10-06 015143" src="https://github.com/user-attachments/assets/7a66e6c5-4a32-4075-adeb-23e329a01d70" />

**Edit dialog box**

<img width="190" height="133" alt="Screenshot 2026-10-06 015214" src="https://github.com/user-attachments/assets/edd0c927-8e4e-4ac3-a00e-e70bb4e24d14" />

**Delete confirmation**

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
- Tracker - tracks user's location and calculates the distance they have done.

## Author
Joshua Marc G. Bastillada
CS26L(35181)
