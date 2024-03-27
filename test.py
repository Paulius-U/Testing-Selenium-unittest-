class BankAccount:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self):
        return self.balance


import unittest

class TestBankAccount(unittest.TestCase):
    
    def test_init(self):
        account = BankAccount("0000", 100)
        self.assertEqual(account.account_id, "0000")
        self.assertEqual(account.balance, 100)

    def test_deposit(self):
        account = BankAccount("0000", 100)
        account.deposit(50)
        self.assertEqual(account.balance, 150)
        with self.assertRaises(ValueError):
            account.deposit(-50)

    def test_withdraw(self):
        account = BankAccount("0000", 100)
        account.withdraw(50)
        self.assertEqual(account.balance, 50)
        with self.assertRaises(ValueError):
            account.withdraw(-50)
        with self.assertRaises(ValueError):
            account.withdraw(200)

    def test_get_balance(self):
        account = BankAccount("0000", 100)
        self.assertEqual(account.get_balance(), 100)

    def test_multiple_deposits(self):
        account = BankAccount("0000", 100)
        account.deposit(50)
        account.deposit(25)
        self.assertEqual(account.balance, 175)

    def test_multiple_withdrawals(self):
        account = BankAccount("0000", 100)
        account.withdraw(50)
        account.withdraw(25)
        self.assertEqual(account.balance, 25)

    def test_deposit_withdraw(self):
        account = BankAccount("0000", 100)
        account.deposit(50)
        account.withdraw(25)
        self.assertEqual(account.balance, 125)

    def test_withdraw_deposit(self):
        account = BankAccount("0000", 100)
        account.withdraw(50)
        account.deposit(25)
        self.assertEqual(account.balance, 75)

    def test_insufficient_balance(self):
        account = BankAccount("0000", 100)
        with self.assertRaises(ValueError):
            account.withdraw(200)

    def test_negative_deposit(self):
        account = BankAccount("0000", 100)
        with self.assertRaises(ValueError):
            account.deposit(-50)

    def test_negative_withdraw(self):
        account = BankAccount("0000", 100)
        with self.assertRaises(ValueError):
            account.withdraw(-50)

    def test_get_balance_after_deposit(self):
        account = BankAccount("0000", 100)
        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)

    def test_get_balance_after_withdraw(self):
        account = BankAccount("0000", 100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)

    def test_get_balance_after_multiple_transactions(self):
        account = BankAccount("0000", 100)
        account.deposit(50)
        account.withdraw(25)
        account.deposit(75)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 150)

    def test_deposit_zero_amount(self):
        account = BankAccount("0000", 100)
        account.deposit(0)
        self.assertEqual(account.balance, 100)

    def test_withdraw_zero_amount(self):
        account = BankAccount("0000", 100)
        account.withdraw(0)
        self.assertEqual(account.balance, 100)

    def test_withdraw_full_balance(self):
        account = BankAccount("0000", 100)
        account.withdraw(100)
        self.assertEqual(account.balance, 0)

    def test_deposit_and_withdraw_same_amount(self):
        account = BankAccount("0000", 100)
        account.deposit(50)
        account.withdraw(50)
        self.assertEqual(account.balance, 100)

    def test_get_balance_initially_zero(self):
        account = BankAccount("0000", 0)
        self.assertEqual(account.get_balance(), 0)

    def test_withdraw_entire_balance(self):
        account = BankAccount("0000", 50)
        account.withdraw(50)
        self.assertEqual(account.balance, 0)
        with self.assertRaises(ValueError):
            account.withdraw(1)

    def test_deposit_large_amount(self):
        account = BankAccount("0000", 100)
        account.deposit(1000000)
        self.assertEqual(account.balance, 1000100)

    def test_deposit_negative_amount(self):
        account = BankAccount("0000", 100)
        with self.assertRaises(ValueError):
            account.deposit(-50)

    def test_withdraw_more_than_balance(self):
        account = BankAccount("0000", 100)
        with self.assertRaises(ValueError):
            account.withdraw(200)

    def test_withdraw_negative_amount(self):
        account = BankAccount("0000", 100)
        with self.assertRaises(ValueError):
            account.withdraw(-50)

    def test_get_balance_after_multiple_deposits_and_withdrawals(self):
        account = BankAccount("0000", 100)
        account.deposit(50)
        account.withdraw(25)
        account.deposit(75)
        account.withdraw(50)
        account.deposit(10)
        account.withdraw(20)
        self.assertEqual(account.get_balance(), 140)

    def test_get_balance_with_initial_balance_zero(self):
        account = BankAccount("0000", 0)
        self.assertEqual(account.get_balance(), 0)

    def test_get_balance_with_initial_negative_balance(self):
        account = BankAccount("0000", -50)
        self.assertEqual(account.get_balance(), -50)

    def test_deposit_large_negative_amount(self):
        account = BankAccount("0000", 100)
        with self.assertRaises(ValueError):
            account.deposit(-1000000)

    def test_withdraw_large_negative_amount(self):
        account = BankAccount("0000", 100)
        with self.assertRaises(ValueError):
            account.withdraw(-1000000)


if __name__ == '__main__':
    unittest.main()