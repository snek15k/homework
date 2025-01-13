import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# Тестовые данные
transactions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-01-01T00:00:00.000000",
        "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
        "description": "Payment 1",
        "from": "Account 1",
        "to": "Account 2",
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2024-01-02T00:00:00.000000",
        "operationAmount": {"amount": "200.00", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Payment 2",
        "from": "Account 3",
        "to": "Account 4",
    },
    {
        "id": 3,
        "state": "EXECUTED",
        "date": "2024-01-03T00:00:00.000000",
        "operationAmount": {"amount": "300.00", "currency": {"name": "USD", "code": "USD"}},
        "description": "Payment 3",
        "from": "Account 5",
        "to": "Account 6",
    },
]


# Тесты для filter_by_currency
def test_filter_by_currency_usd() -> None:
    usd_transactions = filter_by_currency(transactions, "USD")
    result = list(usd_transactions)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_currency_eur() -> None:
    eur_transactions = filter_by_currency(transactions, "EUR")
    result = list(eur_transactions)
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_currency_empty() -> None:
    empty_transactions = filter_by_currency([], "USD")
    result = list(empty_transactions)
    assert len(result) == 0


def test_filter_by_currency_no_match() -> None:
    no_match_transactions = filter_by_currency(transactions, "JPY")
    result = list(no_match_transactions)
    assert len(result) == 0


def test_filter_by_currency_invalid_structure() -> None:
    invalid_transactions = [{"id": 4, "operationAmount": {"amount": "500.00", "currency": {}}}]
    invalid_result = filter_by_currency(invalid_transactions, "USD")
    assert list(invalid_result) == []


# Тесты для функции transaction_descriptions
@pytest.fixture
def sample_transactions() -> list[dict]:
    """Фикстура с тестовыми транзакциями."""
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2024-01-01T00:00:00.000000",
            "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Account 1",
            "to": "Account 2",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2024-01-02T00:00:00.000000",
            "operationAmount": {"amount": "200.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Account 3",
            "to": "Account 4",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2024-01-03T00:00:00.000000",
            "operationAmount": {"amount": "300.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Account 5",
            "to": "Account 6",
        },
    ]


def test_transaction_descriptions(sample_transactions: list[dict]) -> None:
    """Тест на корректную генерацию описаний."""
    descriptions = transaction_descriptions(sample_transactions)
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]
    for expected in expected_descriptions:
        assert next(descriptions) == expected


def test_transaction_descriptions_empty() -> None:
    """Тест на пустой список транзакций."""
    descriptions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(descriptions)


def test_transaction_descriptions_stop_iteration(sample_transactions: list[dict]) -> None:
    """Тест на завершение генератора после всех элементов."""
    descriptions = transaction_descriptions(sample_transactions)
    # Исчерпываем генератор
    for _ in range(len(sample_transactions)):
        next(descriptions)

    # После исчерпания должен быть StopIteration
    with pytest.raises(StopIteration):
        next(descriptions)


# Тесты функции card_number_generator
def test_card_number_generator() -> None:
    """
    Тесты для генератора card_number_generator.
    """

    # Тест на корректный диапазон
    result = list(card_number_generator(1, 5))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert result == expected, f"Expected {expected}, but got {result}"

    # Тест на генерацию одного значения
    result = list(card_number_generator(42, 42))
    expected = ["0000 0000 0000 0042"]
    assert result == expected, f"Expected {expected}, but got {result}"

    # Тест на пустой диапазон
    result = list(card_number_generator(100, 99))
    expected = []
    assert result == expected, f"Expected {expected}, but got {result}"

    # Тест на максимальный номер
    result = list(card_number_generator(9999999999999999, 9999999999999999))
    expected = ["9999 9999 9999 9999"]
    assert result == expected, f"Expected {expected}, but got {result}"
