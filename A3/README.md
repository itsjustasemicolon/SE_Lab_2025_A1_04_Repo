# Task Management CLI with Version Control

This repository contains the solution for Assignment 1 of the Software Engineering Lab 2025 course. The project implements a command-line task manager with Git-like version control using Python and SQLite.

## Files

- `task_management.py`: Main Python script with CLI interface
- `tasks.db`: SQLite database (automatically created on first run)
- `database_schema.sql`: Database schema

## Key Features

- **Full Version History**: Automatic tracking of all task changes
- **Priority Management**: Set low/medium/high priorities
- **Status Tracking**: Pending → In-Progress → Completed workflow
- **Change Restoration**: Revert tasks to any previous state
- **SQLite Backend**: Robust data storage with automatic history triggers
- **CLI Interface**: Intuitive menu-driven interaction

## Installation

1. Clone the repository:
```bash
git clone https://github.com/itsjustasemicolon/SE_Lab_2025_A1_04.git
```

2. Navigate to project directory:
```bash
 cd .\SE_Lab_2025_A1_04\Q3
```

3. Run the application:
```bash
python3 task_management.py    # Linux/MacOS
py task_management.py         # Windows
```

## Usage

The system supports these commands:

| Command    | Description                               | Example                     |
|------------|-------------------------------------------|-----------------------------|
| `add`      | Create new task with title/description    | `add "Code Review"`         |
| `edit`     | Modify task properties                    | `edit 15 (new title)`       |
| `complete` | Mark task as completed                    | `complete 23`               |
| `list`     | Show all tasks                            | `list`                      |
| `history`  | View full change timeline                 | `history 42`                |
| `restore`  | Revert to previous version                | `restore 42 (version 3)`    |
| `delete`   | Remove task (preserves history)           | `delete 18`                 |

## Database Design

### Core Tables
```sql
tasks (               -- Current task states
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  status TEXT DEFAULT 'pending',
  priority TEXT DEFAULT 'medium',
  created_at TIMESTAMP,
  updated_at TIMESTAMP
)

tasks_history (       -- Complete change history
  history_id INTEGER PRIMARY KEY,
  task_id INTEGER,
  title TEXT,
  status TEXT,
  priority TEXT,
  operation TEXT,
  changed_at TIMESTAMP
)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
