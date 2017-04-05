import unittest

class StudentFinanceTestCases(unittest.TestCase):
    def setUp(self):
        self.sf = StudentFinance()

    def test_student_finance_is_subclass(self):
        self.assertTrue(isinstance(self.sf, Student), msg = 'StudentFinance is not a subclass of Student')

    def test_student_finance_takes_valid_input(self):
        p = StudentFinance()
        result = p.validate("string")
        self.assertEqual(result, "Invalid input")

    def test_negative_input(self):
        p = StudentFinance()
        result = p.validate(-10000)
        self.assertEqual(result, "Balance cannot be less than 0)


class StudentPocketMoneyTestCases(unittest.TestCase):

    def test_student_finance_is_subclass(self):
        self.assertTrue(isinstance(StudentPocketMoney, Student), msg = 'StudentPocketMoney is not a subclass of Student')
                         
    def takes_in_valid_input(self):
        p = StudentPocketMoney()
        result = p.validate("string")
        self.assertEqual(result, "Invalid input")

    def test_negative_input(self):
        p = StudentPocketMoney()'
        result = p.validate(-1000)
        self.assertEqual(result,"Balance cannot be less than 0")

    def test_withdraw_amount_is_valid(self):
        p = StudentPocketMoney(1000)
        result = p.withdraw("gvghgh")
        self.assertEqual(result, "Invalid input")

    def test_withdrawal_amount_is_not_greater_than_balance(self):
        p = StudentPocketMoney(1000)
        result = p.withdraw(2000)
        self.assertEqual(result, "Invalid amount. Insufficient funds")

    def test_deposit_amt_is_valid(self):
        p = StudentPocketMoney()
        result = p.deposit("string")
        self.assertEqual(result, "Invalid input")


    
        
