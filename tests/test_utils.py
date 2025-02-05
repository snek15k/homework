import unittest
from typing import Dict, List
from unittest.mock import mock_open, patch

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": "100.50"}]')
    def test_load_transactions_valid_data(
        self, mock_file: unittest.mock.MagicMock, mock_exists: unittest.mock.MagicMock
    ) -> None:
        result: List[Dict[str, str]] = load_transactions()
        self.assertEqual(result, [{"id": 1, "amount": "100.50"}])

    @patch("os.path.exists", return_value=False)
    def test_load_transactions_file_not_exists(self, mock_exists: unittest.mock.MagicMock) -> None:
        result: List[Dict[str, str]] = load_transactions()
        self.assertEqual(result, [])

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_load_transactions_invalid_json_structure(
        self, mock_file: unittest.mock.MagicMock, mock_exists: unittest.mock.MagicMock
    ) -> None:
        result: List[Dict[str, str]] = load_transactions()
        self.assertEqual(result, [])

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data="invalid json")
    def test_load_transactions_json_decode_error(
        self, mock_file: unittest.mock.MagicMock, mock_exists: unittest.mock.MagicMock
    ) -> None:
        result: List[Dict[str, str]] = load_transactions()
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
