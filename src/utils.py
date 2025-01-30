import json
import os
from typing import Any, Dict, List


def load_transactions() -> List[Dict[str, Any]]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    :return: Список словарей с данными о транзакциях или пустой список в случае ошибки.
    """
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (json.JSONDecodeError, IOError):
        pass

    return []


# Пример использования
if __name__ == "__main__":
    transactions: List[Dict[str, Any]] = load_transactions()
    print(transactions)
