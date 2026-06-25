# Python To-Do Manager

A professional, lightweight, and robust Command Line Interface (CLI) application for managing daily tasks. Built using native Python object-oriented patterns, featuring automatic JSON-based data persistence.

## Features

- ➕ **Add Task**: Quickly create tasks with unique, auto-incrementing tracking IDs.
- ❌ **Remove Task**: Delete tasks seamlessly by specifying their ID.
- ✅ **Mark Complete**: Keep track of your progress by updating task statuses dynamically.
- 💾 **Save Tasks**: Auto-saves your data instantly on every change into a readable `tasks.json` storage file.

---

## Directory Structure

``text
python-todo-manager/
├── todo.py     # Application core logic and CLI interface
├── tasks.json          # Persistent local storage (auto-generated)
└── README.md           # Project documentation
Prerequisites
To run this application, you only need Python 3.7 or higher installed on your system. No external dependencies or libraries required!

Getting Started
1. Clone the Repository
Bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/python-todo-manager.git](https://github.com/YOUR_GITHUB_USERNAME/python-todo-manager.git)
cd python-todo-manager
2. Run the Application
Launch the app directly from your terminal or command prompt:

On Windows:
Bash
    python To-do.py

On macOS / Linux:
Bash
  python3 To-do.py
How It Works (Code Architecture)
This manager is built with professional software engineering principles in mind:

Separation of Concerns: The engine logic (TodoManager) is decoupled from the user view (main()), making it highly adaptable for future GUI or Web framework upgrades.

Data Safety: Utilizes structured Python @dataclass contracts and explicit encoding patterns (utf-8) to prevent data corruption during read/write cycles.

Defensive Error Handling: Standardized error-trapping protects against empty strings, invalid structural text inputs, or system crashes.
