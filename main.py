import json
import os.path


def load_database(path):
    try:
        with open(path) as f:
            database = json.load(f)
    except FileNotFoundError:
        database = {}
    return database

def save_database(database, path):
    with open(path, "w") as f:
        json.dump(database, f)

def main():
    DATABASE_PATH = os.path.expanduser("~/tasks.json")
    database = load_database(DATABASE_PATH)
    save_database(database, DATABASE_PATH)

if __name__ == '__main__':
    main()