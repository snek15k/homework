import logging

# Создание логера
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Создание форматера
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логеру
logger.addHandler(file_handler)


# masks.py
def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, скрывая все, кроме последних четырех цифр"""
    if not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("Некорректный номер карты")

    masked_card = "**** **** **** " + card_number[-4:]
    return masked_card


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, скрывая все, кроме последних четырех цифр"""
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Некорректный номер счета")

    masked_account = "*" * (len(account_number) - 4) + account_number[-4:]
    return masked_account
