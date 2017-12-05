# 4poznanski
import unittest
from kol1 import Bank, Client

class MyTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.client1 = Client("Brown")
        self.client2 = Client("Castley")
        self.client1.input(100)
        self.client2.input(100)

    def test_bank_create(self):
        self.assertIsNotNone(self.bank)

    def test_client_create(self):
        self.assertIsNotNone(self.client1)

    def test_client_name(self):
        self.assertEquals(self.client2.name, "Castley")

    def test_client_cash(self):
        self.assertEquals(self.client1.cash, 100)
        self.assertEquals(self.client2.cash, 100)

    def test_add_client(self):
        self.bank.addClient(self.client1)
        self.assertTrue(self.client1 in self.bank.clients)

    def test_input(self):
        self.client1.input(50)
        self.assertEquals(self.client1.cash, 150)

    def test_withdraw(self):
        self.client1.withdraw(20)
        self.assertEquals(self.client1.cash, 80)

    def test_transfer(self):
        self.bank.transfer(self.client1, self.client2, 30)
        self.assertEquals(self.client1.cash, 70)
        self.assertEquals(self.client2.cash, 130)

    def test_input_negative_value(self):
        self.client1.input(-20)
        self.assertNotEquals(self.client1.cash, -80)

    def test_withdraw_negative_value(self):
        self.client2.withdraw(-20)
        self.assertNotEquals(self.client2.cash, 120)

    def test_transfer_negative_value(self):
        self.bank.transfer(self.client1, self.client2, -20)
        self.assertNotEquals(self.client1.cash, 120)
        self.assertNotEquals(self.client2.cash, 80)

    def test_withdraw_more_than_account_balance(self):
        self.client1.withdraw(120)
        self.assertNotEquals(self.client1.cash, -20)

if __name__ == '__main__':
    unittest.main()
