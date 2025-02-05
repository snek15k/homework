import unittest
from unittest.mock import patch

from src.widget import get_date, mask_account_card


class TestMaskingFunctions(unittest.TestCase):

    @patch('src.widget.get_mask_account')
    def test_mask_account_card_valid_account(self, mock_get_mask_account):
        """Проверка маскировки номера счета с корректным номером"""
        mock_get_mask_account.return_value = "************3456"
        result = mask_account_card("Счет 1234567890123456")
        self.assertEqual(result, "Счет ************3456")

    def test_mask_account_card_invalid_account(self):
        """Проверка маскировки номера счета с некорректным номером"""
        result = mask_account_card("Счет 123")
        self.assertEqual(result, "Счет 123 (Некорректный номер счета)")

    @patch('src.widget.get_mask_card_number')
    def test_mask_account_card_valid_card(self, mock_get_mask_card_number):
        """Проверка маскировки номера карты с корректным номером"""
        mock_get_mask_card_number.return_value = "**** **** **** 3456"
        result = mask_account_card("Visa 1234567890123456")
        self.assertEqual(result, "Visa **** **** **** 3456")

    def test_mask_account_card_invalid_card(self):
        """Проверка маскировки номера карты с некорректным номером"""
        result = mask_account_card("MasterCard 12345")
        self.assertEqual(result, "MasterCard 12345 (Некорректный номер карты)")

    def test_mask_account_card_non_account_data(self):
        """Проверка данных, не содержащих счета или карты"""
        result = mask_account_card("Данные без счета или карты")
        self.assertEqual(result, "Данные без счета или карты")


class TestDateConversion(unittest.TestCase):

    def test_get_date_valid(self):
        """Проверка преобразования корректной даты"""
        result = get_date("2025-02-05T12:30:45")
        self.assertEqual(result, "05.02.2025")

    def test_get_date_invalid_format(self):
        """Проверка обработки некорректной даты"""
        result = get_date("2025/02/05T12:30:45")
        self.assertEqual(result, "2025/02/05T12:30:45")

    def test_get_date_empty(self):
        """Проверка обработки пустой строки"""
        result = get_date("")
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
