import os
from typing import Any, List

from src.decorators import log  # Замените `your_module` на имя файла с вашим кодом


@log("test_log.txt")
def add(a: int, b: int) -> int:
    return a + b


@log("test_log.txt")
def faulty_function() -> None:
    raise ValueError("Intentional error")


@log()
def subtract(a: int, b: int) -> int:
    return a - b


def test_log_to_file() -> None:
    """
    Тест записи логов в файл.
    """
    log_file = "test_log.txt"

    # Удаляем лог-файл перед тестом, если он существует
    if os.path.exists(log_file):
        os.remove(log_file)

    # Проверяем успешное выполнение функции
    assert add(3, 5) == 8
    assert os.path.exists(log_file)

    # Читаем лог и проверяем его содержимое
    with open(log_file, "r") as file:
        logs: List[str] = file.readlines()

    assert any("Начало выполнения функции 'add'" in line for line in logs)
    assert any("Успешное завершение функции 'add'" in line for line in logs)

    # Проверяем логирование ошибки
    try:
        faulty_function()
    except ValueError:
        pass

    with open(log_file, "r") as file:
        logs = file.readlines()

    assert any("Ошибка в функции 'faulty_function'" in line for line in logs)
    assert any("Intentional error" in line for line in logs)

    # Удаляем лог-файл после теста
    os.remove(log_file)


def test_log_to_console(capsys: Any) -> None:
    """
    Тест записи логов в консоль.
    """
    assert subtract(10, 4) == 6

    captured = capsys.readouterr()  # Перехватываем вывод
    assert "Начало выполнения функции 'subtract'" in captured.out
    assert "Успешное завершение функции 'subtract'" in captured.out
