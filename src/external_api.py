import os
from typing import Dict

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(amount: float, from_currency: str) -> float:
    """
    Конвертирует сумму из одной валюты в рубли.

    :param amount: сумма для конвертации
    :param from_currency: исходная валюта
    :return: сумма в рублях
    """
    if from_currency == "RUB":
        return amount  # Если валюта уже в рублях

    # Формируем запрос к API для получения курса
    headers = {"apikey": API_KEY}
    params = {"from": from_currency, "to": "RUB", "amount": str(amount)}  # Убедимся, что amount передается как строка

    # Отправляем запрос и обрабатываем ответ
    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code == 200:
        result = response.json()
        return float(result.get("result", 0.0))  # Преобразуем результат в float
    else:
        raise Exception(f"Error while fetching exchange rates: {response.status_code}")


def get_transaction_amount(transaction: Dict[str, float]) -> float:
    """
    Возвращает сумму транзакции в рублях.

    :param transaction: словарь с данными транзакции (amount, currency)
    :return: сумма в рублях
    """
    amount = transaction["amount"]
    currency = transaction["currency"]

    # Если валюта уже рубли, возвращаем сумму как есть
    if currency == "RUB":
        return float(amount)

    # Иначе конвертируем сумму в рубли
    try:
        amount_in_rub = convert_to_rub(amount, str(currency))  # Убедимся, что currency передается как строка
        return amount_in_rub
    except Exception as e:
        print(f"Error: {e}")
        return 0.0
