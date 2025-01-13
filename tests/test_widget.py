import pytest

from src.widget import get_date, mask_account_card


# Тесты для mask_account_card
@pytest.mark.parametrize("input_data, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 12345678901234567890", "Счет **7890"),
])
def test_mask_account_card(input_data: str, expected: str) -> None:
    """
    Тестирует корректность маскирования номера карты или счета.
    """
    assert mask_account_card(input_data) == expected


def test_mask_account_card_invalid_input() -> None:
    """
    Тестирует обработку некорректных входных данных.
    """
    with pytest.raises(ValueError):
        mask_account_card("Invalid Input")


# Тесты для get_date
@pytest.mark.parametrize("date_string, expected", [
    ("2024-12-27T10:00:00.000000", "27.12.2024"),
    ("2018-06-30T02:08:58.425572", "30.06.2018"),
])
def test_get_date(date_string: str, expected: str) -> None:
    """
    Тестирует преобразование строки даты в формат 'ДД.ММ.ГГГГ'.
    """
    assert get_date(date_string) == expected


def test_get_date_invalid_format() -> None:
    """
    Тестирует обработку некорректных форматов даты.
    """
    with pytest.raises(ValueError):
        get_date("InvalidDate")
