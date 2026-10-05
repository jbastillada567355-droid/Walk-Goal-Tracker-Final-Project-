# Walk-Goal-Tracker-Final-Project-
The Walk Goal Tracker System is a desktop application designed to help users define, manage, and monitor their daily walks.
When tracking routine fitness challenges, individuals mostly struggle to log their progress or lose momentum due to disorganized note-keeping.

## Objectives
- Provide a persistent database to securely store goal targets.
- Give a responsive interface that is accessible and easy to navigate.

## Features
- Create Goal:
    Gather valid inputs such as title of goal, expected days, and distance(km) each day.
- Edit Goal:
    Modifies existing goal's title, days, and distance(km).
- Delete Goal:
    Removes a goal permanently from the database. 
- Calculate Total Distance:
    Calculates total distance by multiplying days and distance.
- Table of Goals:
    Displays existing goals. Goals can be selected to be edited or deleted.
- Search and Filter Goals:
    Filters listed table records based on keystroke matching.
- Dark Theme:
    Gives the application a sleek dark theme.

## Technologies Used
- Programing Language: Python 3
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
    Core entry point. Contains the GoalTracker main window class, event routing logic, search filtering loops, and visual dark theme configurations
- database.py:
    Holds the Database wrapper class. It isolates raw SQL interactions, tracking connections, table definitions, and transactional logic
- create_goal.py:
    Implements CreateGoal. Dialog box mapping containing input layouts alongside input type validations
- edit_goal.py:
    Implements EditGoal. Reuses form structures to populate existing goal dictionaries and process field alterations safely

## Installation and Setup
  ### Required Dependencies
  - Python 3.7+
  - PyQt6
  ### Step-by-Step Instructions
  1. Open Terminal or Command Prompt and change dictionaries into your root package folder:
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
2. Create Goal: Click Create Goal. Provide a title, total days (whole number), and target daily distance (number/decimal). Click OK to save.
3. Search/Filter: Type inside the Search Goals... input bar to filter existing records instantly by title.
4. Edit Goal: Select a row in the data grid and click Edit Selected Goal. Adjust title, days, or distance inside the dialog window and save changes. Click OK to save changes.
5. Delete Goal: Select a target row, click Delete Selected Goal, and confirm your decision on the popup alert prompt.

## OOP Implementation
### Important Classes & Runtime Objects
- GoalTracker (Class): Represents the primary structural window layout canvas.
- Database (Class): Defines the database connection and operational abstraction blueprint.
- app (Object): The master runtime QApplication instance powering global configuration flags and event loop cycles.
- window.db (Object): A persistent instance of the Database class embedded within the main window.
### OOP Principles Applied
- Encapsulation
    The Database class encapsulates configuration settings (self.db_name) and isolates the SQL execution logic from the UI code.
- Inheritance
    Custom UI architectures inherit structural properties directly from pre-compiled PyQt6 engine components, boosting structural reusability.
- Polymorphism
    Both CreateGoal and EditGoal expose identical method interfaces.

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
### yet to be implement
tracker

## Author
Joshua Marc G. Bastillada
CS26L(35181)
