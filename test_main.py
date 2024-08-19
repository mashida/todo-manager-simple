from unittest.mock import patch

from tasks import print_list, add_task_to_list, delete_task_from_list


def test_print_list_empty(capsys):
    tasks = []
    print_list(tasks)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Список задач пуст"


def test_print_list_not_empty(capsys):
    tasks = []
    tasks.append("task-01")
    print_list(tasks)
    captured = capsys.readouterr()
    assert captured.out.strip() == "[0]: task-01"


@patch('builtins.input')
def test_add_task_to_list(mock_input):
    mock_input.return_value = 'task-01'
    tasks = []
    add_task_to_list(tasks)
    assert tasks[0] == 'task-01'


@patch('builtins.input')
def test_delete_task_from_list(mock_input):
    mock_input.return_value = '0'
    tasks: list[str] = ['task-01']
    delete_task_from_list(tasks)
    assert len(tasks) == 0


def test_delete_task_from_empty_list(capsys):
    tasks = []
    delete_task_from_list(tasks)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Список задач пуст"
