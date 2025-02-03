import logging

# Создание логера
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Создание форматера
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты."""
    logger.debug(f"Получен запрос на маскировку номера карты: {card_number}")

    if len(card_number) != 16 or not card_number.isdigit():
        logger.error(f"Неверный формат номера карты: {card_number}")
        raise ValueError("Номер карты должен состоять из 16 цифр")

    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Маскированный номер карты: {masked}")
    return masked


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета."""
    logger.debug(f"Получен запрос на маскировку номера счета: {account_number}")

    if not account_number.isdigit():
        logger.error(f"Неверный формат номера счета: {account_number}")
        raise ValueError("Номер счета должен состоять только из цифр")

    masked = f"**{account_number[-4:]}" if len(account_number) >= 4 else "**" + account_number
    logger.info(f"Маскированный номер счета: {masked}")
    return masked
