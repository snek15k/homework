import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src import data_reader
from src.data_reader import read_excel_transactions


class TestDataReader(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="date,amount,description\n2024-01-01,1000,Salary\n2024-01-02,-500,Rent",
    )
    def test_read_csv_transactions(self, mock_file):
        expected_result = [
            {"date": "2024-01-01", "amount": "1000", "description": "Salary"},
            {"date": "2024-01-02", "amount": "-500", "description": "Rent"},
        ]
        result = data_reader.read_csv_transactions("dummy.csv")
        self.assertEqual(result, expected_result)

    @patch("pandas.read_excel")
    def test_read_excel_transactions(self, mock_read_excel):
        # Создаём DataFrame вместо словаря
        mock_read_excel.return_value = pd.DataFrame(
            {"date": ["2024-01-01", "2024-01-02"], "amount": [1000, -500], "description": ["Salary", "Rent"]}
        )

        expected_result = [
            {"date": "2024-01-01", "amount": 1000, "description": "Salary"},
            {"date": "2024-01-02", "amount": -500, "description": "Rent"},
        ]

        result = read_excel_transactions("dummy.xlsx")
        assert result == expected_result


if __name__ == "__main__":
    unittest.main()
