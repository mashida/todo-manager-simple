from files import read_tasks_file, save_tasks_file
from tasks import tasks_process

FILENAME = "tasks.txt"


def main() -> None:
    """
    Main function
    :return: nothing
    """
    # Объявляем список задач
    tasks = read_tasks_file(FILENAME)
    # Главный цикл
    try:
        tasks_process(tasks)
    finally:
        save_tasks_file(FILENAME, tasks)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\nExit")