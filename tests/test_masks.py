import unittest

from src.masks import get_mask_account, get_mask_card_number


class TestMasks(unittest.TestCase):
    def test_mask_card_number(self):
        # Тестирование маскировки номера карты
        card = "1234567890123456"
        masked_card = get_mask_card_number(card)
        self.assertEqual(masked_card, "**** **** **** 3456")  # Ожидаемый результат

    def test_mask_account(self):
        # Тестирование маскировки счета
        account = "12345678901234567890"
        masked_account = get_mask_account(account)
        self.assertEqual(masked_account, "****************7890")  # Ожидаемый результат

    def test_invalid_card(self):
        # Тестирование некорректной карты
        card = "1234abcd5678"  # Некорректный номер карты
        with self.assertRaises(ValueError):
            get_mask_card_number(card)

    def test_invalid_account(self):
        # Тестирование некорректного счета
        account = "12345abc"  # Некорректный номер счета
        with self.assertRaises(ValueError):
            get_mask_account(account)


if __name__ == "__main__":
    unittest.main()
