## Task Manager-CLI

**Task CLI** is a simple and efficient command-line interface tool for managing your daily tasks.
Add, update, delete, or track your tasks directly from your terminal — no web UI required.

---

## Features

* Add new tasks instantly
* Update existing tasks by ID
* Delete tasks when completed or unnecessary
* List all tasks or filter by status (`todo`, `done`)
* Mark tasks as `done` or `in-progress`
---

##  Installation

```bash
# Clone this repository
git clone https://github.com/your-username/task-cli.git

# Navigate to the project directory
cd Task-Manager

# Install dependencies (if using virtualenv)
pip install typer
pip install build

#To setup CLI
python -m build
#Implement pip install for the package
pip install dist/taskmanager-0.1.0-py3-none-any.whl 

#
```

---

## Usage

### Add a new task

```bash
task-cli add "Finish the project report"
```

Adds a new task with the given name and sets its status to **todo** by default.

---

### Update a task

```bash
task-cli update <task_id> "Update the report with latest figures"
```

Updates the task name for the specified ID.

---

### Delete a task

```bash
task-cli delete <task_id>
```

Deletes the task with the given ID.

---

### List all tasks

```bash
task-cli list
```

Displays all tasks, regardless of their status.

---

### List tasks by status

```bash
task-cli list todo
task-cli list done
```

Shows tasks that are either pending (`todo`) or completed (`done`).

---

### Mark a task as done

```bash
task-cli mark-done <task_id>
```

Marks the specified task as **done**.

---

### Mark a task as in-progress

```bash
task-cli mark-in-progress <task_id>
```

Marks the specified task as **in-progress**.

---

## Example

```bash
$ task-cli add "Complete CLI documentation"
✅ Task added successfully!

$ task-cli list
1. Complete CLI documentation — [todo]

$ task-cli mark-in-progress 1
⏳ Task #1 marked as in-progress

$ task-cli mark-done 1
🎉 Task #1 marked as done

$ task-cli list done
1. Complete CLI documentation — [done]
```
## Project Idea 
    [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)
---

