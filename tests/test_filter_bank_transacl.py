import unittest

from src.filter_bank_transacl import count_transactions_by_category, filter_transactions


class TestBankOperations(unittest.TestCase):
    def setUp(self):
        self.transactions = [
            {"id": 1, "amount": 1000, "description": "Оплата услуг связи"},
            {"id": 2, "amount": 500, "description": "Покупка в супермаркете"},
            {"id": 3, "amount": 200, "description": "Кафе и рестораны"},
            {"id": 4, "amount": 1500, "description": "Оплата аренды"},
        ]

    def test_filter_transactions(self):
        result = filter_transactions(self.transactions, "оплата")
        expected = [
            {"id": 1, "amount": 1000, "description": "Оплата услуг связи"},
            {"id": 4, "amount": 1500, "description": "Оплата аренды"},
        ]
        self.assertEqual(result, expected)

    def test_count_transactions_by_category(self):
        categories = ["Оплата", "Покупка", "Кафе"]
        result = count_transactions_by_category(self.transactions, categories)
        expected = {"Оплата": 2, "Покупка": 1, "Кафе": 1}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
