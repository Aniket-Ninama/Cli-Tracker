# CLI Task Tracker

A simple command-line tool to manage tasks with statuses like todo, in-progress, and done. Tasks are stored in a JSON file for easy persistence.

---

## Requirements

- Python 3.6+
- `argparse` (comes pre-installed with Python)

---

## Installation

1. **Clone the repository or download the script:**

```bash
git clone https://github.com/your-username/cli-task-tracker.git
cd cli-task-tracker

Install dependencies:
pip install -r requirements.txt

Add a new task:
python main.py add "Your Task"

Update an existing task:
python main.py update <task_id> --title "New description" --status <todo|in-progress|done>

Delete a task:
python main.py delete <task_id>

List all tasks:
python main.py list

List tasks by status:
python main.py todo
python main.py in-progress
python main.py done
