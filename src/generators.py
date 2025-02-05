from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """
    Фильтрует список транзакций по заданной валюте и возвращает итератор.
    """
    return (
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
    )


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой операции из списка транзакций.
    """
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.
    """
    for number in range(start, end + 1):
        yield (
            f"{number:016d}"[:4]
            + " "
            + f"{number:016d}"[4:8]
            + " "
            + f"{number:016d}"[8:12]
            + " "
            + f"{number:016d}"[12:16]
        )
