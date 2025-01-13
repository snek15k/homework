import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты для get_mask_card_number
@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
])
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid_length() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("123")  # Недопустимая длина


# Тесты для get_mask_account
@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "**7890"),
    ("67890", "**7890"),
])
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


def test_get_mask_account_invalid_input() -> None:
    with pytest.raises(ValueError):
        get_mask_account("invalid")
