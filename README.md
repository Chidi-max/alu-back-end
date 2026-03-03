# API Data Export Project

This project uses the JSONPlaceholder REST API to fetch and export employee TODO tasks in various formats.

## Scripts

### 1. Gather Data from API (`api/0-gather_data_from_an_API.py`)

Prints an employee's completed tasks and progress.

```bash
python api/0-gather_data_from_an_API.py <employee_id>
```

### 2. Export to CSV (`api/1-export_to_CSV.py`)

Exports all employee tasks to a CSV file named with the employee ID.

```bash
python api/1-export_to_CSV.py <employee_id>
```

### 3. Export to JSON (`api/2-export_to_JSON.py`)

Exports employee tasks to a JSON file named with the employee ID in the required structure.

```bash
python api/2-export_to_JSON.py <employee_id>
```

### 4. Dictionary of List of Dictionaries (`api/3-dictionary_of_list_of_dictionaries.py`)

Fetches all users and all tasks from the API and saves them into one JSON file that groups every user's tasks under their user ID.

```bash
python api/3-dictionary_of_list_of_dictionaries.py
```

## Output Files

- `{employee_id}.csv` - CSV file with employee tasks
- `{employee_id}.json` - JSON file with employee tasks
- `todo_all_employees.json` - Combined JSON file with all employees' tasks
