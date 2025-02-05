import re


def filter_transactions(transactions: list[dict], search_string: str) -> list[dict]:
    """
    Фильтрует список банковских операций по наличию строки поиска в описании.

    :param transactions: Список словарей с данными о транзакциях.
    :param search_string: Строка поиска (регулярное выражение).
    :return: Список словарей, содержащих совпадение в описании.
    """
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]


def count_transactions_by_category(transactions: list[dict], categories: list[str]) -> dict:
    """
    Подсчитывает количество операций в каждой категории.

    :param transactions: Список словарей с данными о транзакциях.
    :param categories: Список категорий операций.
    :return: Словарь с количеством операций в каждой категории.
    """
    category_count = {category: 0 for category in categories}

    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
                break

    return category_count


def filter_transactions_by_description(transactions: list[dict], search_string: str) -> list[dict]:
    """
    Фильтрует транзакции по слову в описании.
    """
    filtered = [
        transaction
        for transaction in transactions
        if re.search(search_string, transaction["description"], re.IGNORECASE)
    ]
    return filtered
