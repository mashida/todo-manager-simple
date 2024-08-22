from errors import NoMoreAttempts, RefuseToCreateNewUser
from files import read_tasks_file, save_tasks_file
from get_user import get_user
from tasks import tasks_process

TASKS_FILENAME = "tasks.txt"
USERS_FILENAME = "users.txt"


def main() -> None:
    """
    Main function
    :return: nothing
    """
    # Объявляем список задач
    tasks = read_tasks_file(TASKS_FILENAME)
    try:
        # Проверка пользователя
        user = get_user(USERS_FILENAME)
        # Главный цикл
        tasks_process(tasks)
    except (NoMoreAttempts, RefuseToCreateNewUser) as e:
        print(f"Ошибка | {e}")
    finally:
        save_tasks_file(TASKS_FILENAME, tasks)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\nExit")
