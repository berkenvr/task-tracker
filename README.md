Task CLI
========

A simple command-line task management application built in Python.
(https://roadmap.sh/projects/task-tracker)

Features
--------
- Add Task: Create a new task with a description.
- List Tasks: Display all tasks or filter by status (todo, in-progress, done).
- Update Task: Modify the description of an existing task.
- Delete Task: Remove a task by its ID.
- Change Status: Mark tasks as in-progress or done.
- Help: Display a list of available commands.

How It Works
------------
Data Storage:
- Tasks are saved in a file named "tasks.json" in JSON format.

Task Attributes:
- id: A unique identifier.
- description: Details about the task.
- status: The task's current status ("todo", "in-progress", or "done").
- createdAt: Timestamp when the task was created.
- updatedAt: Timestamp for the last update.

Getting Started
---------------
1. Clone or download the code.
2. Open your terminal and navigate to the project directory.
3. Run the application by executing:
   python <script_name.py>
   (Replace <script_name.py> with the name of the Python file containing the code.)

Commands
--------
- add <description>           -> Add a new task.
- list                        -> List all tasks.
- list todo                   -> List tasks with status "todo".
- list in-progress            -> List tasks with status "in-progress".
- list done                   -> List tasks with status "done".
- delete <id>                 -> Delete a task by its ID.
- update <id> <description>   -> Update a task's description.
- mark-in-progress <id>       -> Mark a task as in-progress.
- mark-done <id>              -> Mark a task as done.
- help                        -> Show available commands.
- exit                        -> Exit the application.

License
-------
MIT License

Copyright (c) 2025 berkenvr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
