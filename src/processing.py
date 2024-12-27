def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа state.
    """
    # Возвращаем отфильтрованный список
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """
    Сортирует список словарей по ключу 'date'.
    """
    # Сортируем список, преобразуя строку даты в объект datetime для сравнения
    return sorted(
        data,
        key=lambda x: x.get('date', ''),
        reverse=descending
    )
