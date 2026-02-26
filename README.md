Project Overview
-----------------
This application allows users to manage daily tasks directly from the terminal. Tasks are saved locally so they persist even after the program is closed.

It is ideal for:
---------------
Python beginners
Backend development practice
Portfolio projects
Demonstrating real-world file handling

Features
---------
Add new tasks
Remove existing tasks
View all saved tasks
Persistent task storage using JSON
Desktop notification when a task is added
Graceful handling of invalid inputs and corrupted files

Technologies Used
------------------
Python 3
pathlib – modern file path handling
json – task persistence
plyer – cross-platform desktop notifications

Project Structure (Single File)
-------------------------------
todo-cli-app/
│
├── main.py          # Entire application logic
└── todo_list.json   # Auto-generated task storage

Installation & Setup
---------------------
1️⃣ Clone the repository
git clone https://github.com/kunmi14/Command-Line-To-Do-List-App.git
cd your-repo-name

2️⃣ Install dependencies
pip install plyer

▶️ How to Run the Application
python3 main.py
You’ll be presented with a menu:
1. Add task
2. Remove task
3. View task
4. Quit or Exit
Enter a number between 1 and 4 to perform an action.

How the Application Works
--------------------------
Tasks are stored in a local JSON file.
On startup, the app loads existing tasks.
When a task is added:
It is saved immediately to disk.
A desktop notification confirms the action.
Input validation prevents crashes from invalid user input.

Error Handling
----------------
This project safely handles:
Missing task files
Corrupted JSON data
Invalid numeric input
Empty task lists

Why This Project Matters
--------------------------
This project demonstrates:
Practical Python usage
File system operations
Data persistence
User input validation
Clean functional programming structure

It’s a strong foundation for:
Backend development
Automation scripts
CLI tools
DevOps utilities
