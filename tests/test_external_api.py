import os
import sys
import unittest
from typing import Any, Dict
from unittest.mock import Mock, patch

from src.external_api import convert_to_rub, get_transaction_amount

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


class TestExternalAPI(unittest.TestCase):

    @patch("src.external_api.requests.get")
    def test_convert_to_rub_success(self, mock_get: Mock) -> None:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 100.0}
        mock_get.return_value = mock_response

        amount_in_rub = convert_to_rub(50.0, "USD")
        self.assertEqual(amount_in_rub, 100.0)

    @patch("src.external_api.requests.get")
    def test_convert_to_rub_error(self, mock_get: Mock) -> None:
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            convert_to_rub(50.0, "USD")

    @patch("src.external_api.requests.get")
    def test_get_transaction_amount_success(self, mock_get: Mock) -> None:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 100.0}
        mock_get.return_value = mock_response

        # Используем Any, чтобы разрешить строковые значения
        transaction: Dict[str, Any] = {"amount": 50.0, "currency": "USD"}
        amount_in_rub = get_transaction_amount(transaction)
        self.assertEqual(amount_in_rub, 100.0)

    @patch("src.external_api.requests.get")
    def test_get_transaction_amount_no_conversion(self, mock_get: Mock) -> None:
        # Используем Any, чтобы разрешить строковые значения
        transaction: Dict[str, Any] = {"amount": 100.0, "currency": "RUB"}
        amount_in_rub = get_transaction_amount(transaction)
        self.assertEqual(amount_in_rub, 100.0)


if __name__ == "__main__":
    unittest.main()
