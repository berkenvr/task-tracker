import json
import os.path
from datetime import datetime

def parse_command(command):
    command = command.split()

    c_code = command[:1]
    params = ' '.join(command[1:])

    return run_command(c_code[0], params)

def run_command(c_code, params):
    if not os.path.exists('tasks.json'):
        print('There is no file to edit')

        with open('tasks.json', 'w') as f:
            json.dump([], f, indent = 4)
        return f'File created, please write a command'
    else:
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
        else:
            return f'Unknown command'

def add_task(params):
    current_time = datetime.now()
    f_time = current_time.strftime('%H:%M %d %B %Y')

    with open('tasks.json', 'r') as f:
        data = json.load(f)
        data_id = 1

        if len(data) > 0:
            data_id = data[-1]['id'] + 1

        data.append(
            {
                'id': data_id,
                'description': params,
                'status': 'todo',
                'createdAt': f_time,
                'updatedAt': f_time
            }
        )

        with open('tasks.json', 'w') as f:
            json.dump(data, f, indent = 4)

    return f'Task added'

def list_task(params):
    data = json.load(open('tasks.json'))

    if len(data) == 0:
        return f'List is empty'
    elif params == '':
        for i in range(len(data)):
                print(data[i])
        return f'All tasks listed'
    elif params in ['todo', 'done', 'in-progress']:
        for i in range(len(data)):
            if data[i]['status'] == params:
                print(data[i])
    else:
        return f'Invalid status type'
    return f'All {params} tasks listed'

def delete_task(params):
    data = json.load(open('tasks.json'))
    temp_len = len(data)

    for i in range(temp_len):
        if data[i]['id'] == int(params):
            data.pop(i)
            break

    if temp_len == len(data):
        return f'No matching id'

    with open('tasks.json', 'w') as f:
        json.dump(data, f, indent = 4)
    return f'Task deleted'

def update_task(params):
    task_id = int(params[0:1])
    task_desc = params[2:]

    data = json.load(open('tasks.json'))

    for i in range(len(data)):
        if data[i]['id'] == task_id:
            data[i]['description'] = task_desc
            with open('tasks.json', 'w') as f:
                json.dump(data, f, indent=4)
            return f'Task description updated'
    return f'No mathing id'

def mark_task(c_code, params):
    data = json.load(open('tasks.json'))

    for i in range(len(data)):
        if data[i]['id'] == int(params):
            if c_code == 'mark-in-progress':
                data[i]['status'] = 'in-progress'
            else:
                data[i]['status'] = 'done'
            with open('tasks.json', 'w') as f:
                json.dump(data, f, indent=4)
            return f'Task status updated'
    return f'No mathing id'

def main():
    try:
        while True:
            command = input('task-cli ')
            result = parse_command(command)
            print(result)
    except KeyboardInterrupt:
        print('Tasking completed')

if __name__ == '__main__':
    main()