def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    card_number = str(card_number)

    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked


def get_mask_account(account_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    account_number = str(account_number)

    if not account_number.isdigit():
        raise ValueError("Номер счета должен состоять только из цифр")

    masked = f"**{account_number[-4:]}" if len(account_number) >= 4 else "**" + account_number
    return masked
