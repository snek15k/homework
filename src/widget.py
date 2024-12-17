from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Обрабатывает строку с типом и номером карты или счета и возвращает замаскированный номер.
    """
    words = data.split()
    card_or_account_type = words[0]
    account_or_card_number = words[-1]

    # Если это счет
    if card_or_account_type == "Счет":
        masked_account = get_mask_account(account_or_card_number)
        return f"{card_or_account_type} {masked_account}"

    # Если это карта
    else:
        masked_card = get_mask_card_number(account_or_card_number)
        return f"{card_or_account_type} {masked_card}"
