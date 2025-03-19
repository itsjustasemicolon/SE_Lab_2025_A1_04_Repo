# Task Management CLI with Version Control

A robust command-line task manager built in Python with SQLite backing, featuring complete version control of all tasks. This application allows you to track and manage your tasks while maintaining a comprehensive history of all changes.

## Key Features

- **Complete Task Management**: Create, edit, complete, and delete tasks with ease
- **Version Control**: Every change to any task is tracked and can be restored
- **Priority Levels**: Assign low, medium, or high priority to tasks
- **Status Tracking**: Monitor task status (pending, in-progress, completed)
- **Filtering Capabilities**: View tasks by status (all, pending, completed)
- **History Viewing**: See the complete timeline of changes to any task
- **Version Restoration**: Restore tasks to any previous state

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/task-manager-cli.git

# Navigate to the project directory
cd task-manager-cli

# No external dependencies required - uses standard Python libraries!
# Python 3.6+ recommended
```

## Usage

Run the application by executing the main script:

```bash
python task_manager.py
```

The interactive menu will guide you through all available commands:

- `add` - Create a new task
- `edit` - Modify an existing task
- `complete` - Mark a task as completed
- `list` - View all tasks
- `pending` - Show only pending tasks
- `completed` - Show only completed tasks
- `delete` - Remove a task
- `history` - View the complete history of a task
- `restore` - Revert a task to a previous version
- `quit` - Exit the application

## Database Structure

The application uses SQLite with two main tables:

### Tasks Table
Stores the current state of all tasks:
```
tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'pending',
    priority TEXT DEFAULT 'medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

### Tasks History Table
Records every change to any task:
```
tasks_history (
    history_id INTEGER PRIMARY KEY,
    task_id INTEGER,
    title TEXT,
    description TEXT,
    status TEXT,
    priority TEXT,
    operation TEXT NOT NULL,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(id)
)
```

## How It Works

### Database Initialization

The system creates an SQLite database file (`tasks.db`) when first launched. Two tables are created - one for current tasks and one for historical changes[1].

### Version Control Implementation

The application uses SQLite triggers to automatically record all changes:

1. **INSERT Trigger**: When a new task is created, its initial state is recorded
2. **UPDATE Trigger**: When a task is modified, the new state is recorded
3. **DELETE Trigger**: When a task is deleted, its final state is preserved[1]

This comprehensive history makes it possible to view the complete evolution of any task and restore it to any previous state.

### Core Functions

- `create_database()`: Sets up the SQLite database and tables[1]
- `setup_triggers()`: Creates database triggers for history tracking[1]
- `add_task()`: Creates a new task with specified attributes[1]
- `update_task()`: Modifies an existing task[1]
- `complete_task()`: Specialized function to mark tasks complete[1]
- `delete_task()`: Removes a task from the active list[1] 
- `list_tasks()`: Displays tasks with optional filtering[1]
- `get_task_history()`: Retrieves the change history of a specific task[1]
- `display_task_history()`: Shows task history in a readable format[1]
- `restore_task_version()`: Reverts a task to a previous state[1]

### User Interface

The CLI provides a simple but powerful menu-driven interface. Each operation is performed through specific commands, with the system guiding users through required inputs[1].

## Code Overview

### Main Components

1. **Database Management**: Functions for creating and interacting with the SQLite database
2. **Task Operations**: Functions for manipulating tasks
3. **History Management**: Functions for tracking and displaying task history
4. **Version Control**: Functions for restoring previous versions
5. **User Interface**: CLI interface with a command menu system[1]

The code uses SQLite triggers extensively to maintain version history without requiring explicit history-tracking calls within the application logic.

## Example Workflow

1. Add a task with `add` command
2. View tasks with `list` command
3. Edit a task with `edit` command
4. View its history with `history` command
5. If needed, restore to a previous version with `restore` command[1]

## Contributing

Interested in contributing? Here are some ways to help:

1. Add support for task categories or tags
2. Implement task search functionality
3. Create a simple GUI frontend
4. Add export/import capabilities
5. Improve the output formatting

Please keep the version control functionality intact when making changes, as it's a core feature of this application.

