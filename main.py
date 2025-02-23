import json
import os
from datetime import datetime

def load_tasks():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as f:
            json.dump([], f, indent=4)
    with open('tasks.json', 'r') as f:
        return json.load(f)

def save_tasks(data):
    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent=4)

def parse_command(command):
    command_parts = command.split()
    if not command_parts:
        return "Empty command. Please type a command."
    c_code = command_parts[0]
    params = " ".join(command_parts[1:]) if len(command_parts) > 1 else ""
    return run_command(c_code, params)

def run_command(c_code, params):
    if c_code == 'add':
        return add_task(params)
    elif c_code in ['list', 'list todo', 'list done', 'list in-progress']:
        return list_task(params)
    elif c_code == 'delete':
        return delete_task(params)
    elif c_code == 'update':
        return update_task(params)
    elif c_code in ['mark-in-progress', 'mark-done']:
        return mark_task(c_code, params)
    elif c_code == 'exit':
        print('Tasking completed')
        exit()
    elif c_code == 'help':
        return get_help()
    else:
        return "Unknown command, please write 'help' to list all commands"

def add_task(params):
    current_time = datetime.now().strftime('%H:%M %d %B %Y')
    tasks = load_tasks()
    task_id = 1 if not tasks else tasks[-1]['id'] + 1

    tasks.append({
        'id': task_id,
        'description': params,
        'status': 'todo',
        'createdAt': current_time,
        'updatedAt': current_time
    })

    save_tasks(tasks)
    return "Task added"

def list_task(params):
    tasks = load_tasks()
    if not tasks:
        return "List is empty"
    if params == "":
        for task in tasks:
            print(task)
        return "All tasks listed"
    elif params in ['todo', 'done', 'in-progress']:
        for task in tasks:
            if task['status'] == params:
                print(task)
        return f"All {params} tasks listed"
    else:
        return "Invalid status type"

def delete_task(params):
    tasks = load_tasks()
    original_length = len(tasks)
    try:
        task_id = int(params)
    except ValueError:
        return "Invalid task ID"

    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(i)
            break

    if len(tasks) == original_length:
        return "No matching id"

    save_tasks(tasks)
    return "Task deleted"

def update_task(params):
    try:
        task_id_str, task_desc = params.split(maxsplit=1)
        task_id = int(task_id_str)
    except ValueError:
        return "Invalid parameters. Correct format: update <id> <description>"

    tasks = load_tasks()
    current_time = datetime.now().strftime('%H:%M %d %B %Y')

    for task in tasks:
        if task['id'] == task_id:
            task['description'] = task_desc
            task['updatedAt'] = current_time
            save_tasks(tasks)
            return "Task description updated"
    return "No matching id"

def mark_task(c_code, params):
    tasks = load_tasks()
    try:
        task_id = int(params)
    except ValueError:
        return "Invalid task ID"

    current_time = datetime.now().strftime('%H:%M %d %B %Y')

    for task in tasks:
        if task['id'] == task_id:
            if c_code == 'mark-in-progress':
                if task['status'] == 'in-progress':
                    return "Task's status is already in-progress"
                task['status'] = 'in-progress'
            else:  # mark-done
                if task['status'] == 'done':
                    return "Task's status is already done"
                task['status'] = 'done'
            task['updatedAt'] = current_time
            save_tasks(tasks)
            return "Task status updated"
    return "No matching id"

def get_help():
    command_list = [
        'add <description> -> to add task',
        'list -> to list all tasks',
        'list todo -> to list "status: todo" tasks',
        'list in-progress -> to list "status: in-progress" tasks',
        'list done -> to list "status: done" tasks',
        'delete <id> -> to delete selected task',
        'update <id> <description> -> to update selected task\'s description',
        'mark-in-progress <id>, mark-done <id> -> to change selected task\'s status',
        'exit -> to exit',
        'help -> to get help about commands',
    ]
    for cmd in command_list:
        print(cmd)
    return "All commands listed"

def main():
    try:
        while True:
            command = input('task-cli ')
            result = parse_command(command)
            print(result)
    except KeyboardInterrupt:
        print('\nTasking completed')

if __name__ == '__main__':
    main()
