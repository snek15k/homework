from typing import Dict, List, Union

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def test_data() -> List[Dict[str, Union[str, int]]]:
    """
    Предоставляет тестовые данные для тестов.
    """
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-12-27T10:00:00.000000'},
        {'id': 2, 'state': 'CANCELED', 'date': '2024-12-25T10:00:00.000000'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-12-26T10:00:00.000000'},
    ]


# Тесты для filter_by_state
def test_filter_by_state_default(test_data: List[Dict[str, str]]) -> None:
    """
    Тестирует фильтрацию по умолчанию (state='EXECUTED').
    """
    result = filter_by_state(test_data)
    assert len(result) == 2  # Должно вернуть только 'EXECUTED'
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_custom(test_data: List[Dict[str, str]]) -> None:
    """
    Тестирует фильтрацию по пользовательскому значению state.
    """
    result = filter_by_state(test_data, state="CANCELED")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_state_empty() -> None:
    """
    Тестирует обработку пустого списка данных.
    """
    assert filter_by_state([]) == []


# Тесты для sort_by_date
def test_sort_by_date_desc(test_data: List[Dict[str, str]]) -> None:
    """
    Тестирует сортировку по убыванию дат.
    """
    result = sort_by_date(test_data)
    assert result[0]["date"] == '2024-12-27T10:00:00.000000'  # Самая поздняя дата
    assert result[-1]["date"] == '2024-12-25T10:00:00.000000'  # Самая ранняя дата


def test_sort_by_date_asc(test_data: List[Dict[str, str]]) -> None:
    """
    Тестирует сортировку по возрастанию дат.
    """
    result = sort_by_date(test_data, descending=False)
    assert result[0]["date"] == '2024-12-25T10:00:00.000000'  # Самая ранняя дата
    assert result[-1]["date"] == '2024-12-27T10:00:00.000000'  # Самая поздняя дата


def test_sort_by_date_empty() -> None:
    """
    Тестирует обработку пустого списка данных.
    """
    assert sort_by_date([]) == []
