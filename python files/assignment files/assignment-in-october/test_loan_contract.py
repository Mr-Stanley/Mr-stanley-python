import unittest
from tasks.loan_contract import LoanContract


class TestLoanContract(unittest.TestCase):

    def test_for_monthly_payment(self):
        loan_contract = LoanContract()
        loan_contract.setLoanAmount(500000z)
        loan_contract.setLoanPeriod(24)
        loan_contract.setBorrowerName("john")
        loan_contract.setInterestRate(0.12)
        monthly_payment = loan_contract.getMonthlyPayment()
        self.assertEqual(monthly_payment, 23120.42)

