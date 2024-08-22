import os


def read_tasks_file(filename) -> list[str]:
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        return [task.strip() for task in file.readlines()]


def save_tasks_file(filename, list_of_tasks) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(list_of_tasks))


def read_users_file(filename: str) -> dict[str, str]:
    result: dict[str, str] = {}
    if not os.path.exists(filename):
        return result

    with open(filename, 'r', encoding='utf-8') as file:
        return {line.split(':')[0].strip(): line.split(':')[1].strip() for line in file.readlines()}


def save_users_file(filename: str, users: dict[str, str]) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join([f"{key}:{value}" for key, value in users]))

def add_user_to_file(filename: str, key: str, value: str):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{key}: {value}\n")
