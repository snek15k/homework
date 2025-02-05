from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Маскирует номер счета или карты в строке"""
    if "Счет" in data:
        # Если это счет, проверяем, является ли номер корректным
        account_number = "".join(filter(str.isdigit, data))
        if not account_number or len(account_number) < 4:  # Если номер счета некорректен
            return f"{data} (Некорректный номер счета)"
        masked_account = get_mask_account(account_number)
        return f"Счет {masked_account}"
    elif "MasterCard" in data or "Visa" in data:
        # Если это номер карты, применяем маскировку для карты
        card_number = "".join(filter(str.isdigit, data))
        if len(card_number) != 16:  # Если номер карты некорректен
            return f"{data} (Некорректный номер карты)"
        masked_card = get_mask_card_number(card_number)
        return f"{data.split()[0]} {masked_card}"
    else:
        return data


def get_date(date_string: str) -> str:
    """Функция преобразует строку формата 'ГГГГ-ММ-ДДTчч:мм:сс' в 'ДД.ММ.ГГГГ'"""
    if not date_string:
        return date_string  # Если строка пустая, возвращаем её как есть
    try:
        # Разбиваем строку на две части: дата и время
        date_part = date_string.split("T")[0]  # Берем первую часть до символа 'T'

        # Разбиваем дату на год, месяц и день
        year, month, day = date_part.split("-")
        return f"{day}.{month}.{year}"
    except ValueError:
        return date_string  # Если произошла ошибка, возвращаем исходную строку
