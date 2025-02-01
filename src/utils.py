import json
import logging
import os
from typing import Any, Dict, List

# Создание логера
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Создание форматера
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логеру
logger.addHandler(file_handler)


def load_transactions() -> List[Dict[str, Any]]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    :return: Список словарей с данными о транзакциях или пустой список в случае ошибки.
    """
    logger.debug("Загружаем транзакции из файла.")

    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")

    if not os.path.exists(file_path):
        logger.warning(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций.")
                return data
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Ошибка при чтении файла или декодировании JSON: {e}")

    return []
