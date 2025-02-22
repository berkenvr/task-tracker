import json
import os.path
from datetime import datetime

def parse_command(command):
    command = command.split()

    c_code = command[:1]
    params = ' '.join(command[1:])

    return run_command(c_code[0], params)

def run_command(c_code, params):
    if c_code == 'add':
        return add_task(params)
    elif c_code == 'list':
        return list_task()
    else:
        return f'Unknown command'

def add_task(params):
    current_time = datetime.now()
    f_time = current_time.strftime('%H:%M %d %B %Y')

    if not os.path.exists('tasks.json'):
        w_json = [
            {
            'id': 1,
            'description': params,
            'status': 'todo',
            'createdAt': f_time,
            'updatedAt': f_time
            }
        ]
        with open('tasks.json', 'w') as f:
            json.dump(w_json, f, indent = 4)
    else:
        with open('tasks.json', 'r') as f:
            data = json.load(f)
            data.append(
                {
                    'id': data[-1]['id'] + 1,
                    'description': params,
                    'status': 'todo',
                    'createdAt': f_time,
                    'updatedAt': f_time
                }
            )
        with open('tasks.json', 'w') as f:
            json.dump(data, f, indent = 4)

    return f'Task added'

def list_task():
    if not os.path.exists('tasks.json'):
        return f'There is no file to list.'
    else:
        with open('tasks.json', 'r') as f:
            data = json.load(f)
            for i in range(0, len(data)):
                print(data[i])
    return f'All tasks listed'

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