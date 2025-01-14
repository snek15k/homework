from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Обрабатывает строку с типом и номером карты или счета и возвращает замаскированный номер.
    """
    words = data.split()
    card_or_account_type = " ".join(words[:-1])  # Объединяем все слова, кроме последнего
    account_or_card_number = words[-1]          # Последнее слово — номер карты или счета

    # Если это счет
    if card_or_account_type.startswith("Счет"):
        masked_account = get_mask_account(account_or_card_number)
        return f"{card_or_account_type} {masked_account}"

    # Если это карта
    masked_card = get_mask_card_number(account_or_card_number)
    return f"{card_or_account_type} {masked_card}"


def get_date(date_string: str) -> str:
    """Функция преобразует строку формата 'ГГГГ-ММ-ДДTчч:мм:сс' в 'ДД.ММ.ГГГГ'"""
    # Разбиваем строку на две части: дата и время
    date_part = date_string.split("T")[0]  # Берем первую часть до символа 'T'

    # Разбиваем дату на год, месяц и день
    year, month, day = date_part.split("-")

    # Собираем дату в нужном формате
    formatted_date = f"{day}.{month}.{year}"

    return formatted_date
