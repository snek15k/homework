import csv
from typing import Any, Dict, Hashable, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict[str, str]]:
    """
    Читает финансовые операции из CSV-файла и возвращает список словарей.
    """
    transactions = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(dict(row))
    return transactions


def read_excel_transactions(file_path: str) -> List[Dict[Hashable, Any]]:
    """
    Читает финансовые операции из Excel-файла и возвращает список словарей.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")
