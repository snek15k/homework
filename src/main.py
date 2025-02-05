import os

from src.data_reader import read_csv_transactions  # Добавьте импорт функции для работы с CSV
from src.data_reader import read_excel_transactions  # Добавьте импорт функции для работы с XLSX
from src.external_api import convert_to_rub
from src.filter_bank_transacl import filter_transactions_by_description
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        transactions = load_transactions()  # загрузка из JSON
    elif choice == "2":
        transactions = read_csv_transactions(os.path.join("data", "your_csv_file.csv"))  # загрузка из CSV
    elif choice == "3":
        transactions = read_excel_transactions(os.path.join("data", "your_excel_file.xlsx"))  # загрузка из XLSX
    else:
        print("Неверный выбор.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции.")
        return

    print(f"Загружено {len(transactions)} транзакций.")

    # Фильтрация по статусу
    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING")

    status = input("Ваш выбор: ").strip().upper()

    # Проверяем, что статус корректен
    while status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции '{status}' недоступен.")
        status = (
            input(
                "Введите статус, по которому необходимо выполнить фильтрацию. Доступные: EXECUTED, CANCELED, PENDING"
            )
            .strip()
            .upper()
        )

    # Фильтруем транзакции по статусу
    transactions = filter_by_state(transactions, status)
    print(f"Операции отфильтрованы по статусу '{status}'.")

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == "да":
        order_choice = input("По возрастанию или по убыванию? ").strip().lower()
        descending = order_choice == "по убыванию"
        transactions = sort_by_date(transactions, descending)

    # Фильтрация по валюте
    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_choice == "да":
        transactions = [t for t in transactions if t["operationAmount"]["currency"]["code"] == "RUB"]

    # Фильтрация по описанию
    description_choice = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    )
    if description_choice == "да":
        search_string = input("Введите слово для поиска в описании: ").strip()
        transactions = filter_transactions_by_description(transactions, search_string)

    # Печать итогового списка
    if transactions:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions)}")

        for transaction in transactions:
            date = get_date(transaction["date"])

            # Проверяем наличие ключа 'from' в транзакции
            from_account = mask_account_card(transaction["from"]) if "from" in transaction else "Не указано"
            to_account = mask_account_card(transaction["to"]) if "to" in transaction else "Не указано"

            amount = convert_to_rub(
                float(transaction["operationAmount"]["amount"]), transaction["operationAmount"]["currency"]["code"]
            )

            print(f"{date} {transaction['description']}")
            print(f"{from_account} -> {to_account}")
            print(f"Сумма: {amount} руб.\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
