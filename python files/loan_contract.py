class LoanContract:
    def __init__(self,borrower_name: str, interest_rate: int,loan_period: int, loan_amount: int  ):
        # self.monthly_payment = monthly_payment
        self.borrower_name = borrower_name
        self.interest_rate = interest_rate
        self.loan_amount = loan_amount
        self.loan_period = loan_period


    def __str__(self):
        return f"""
        Borrowers name: {self.borrower_name}
        Interest rate: {self.interest_rate}
        Loan amount: {self.loan_amount}
        Loan period: {self.loan_period}
        
        """

    def setBorrowerName(self, borrower_name):
        self.borrower_name = borrower_name


    def setLoanAmount(self, loan_amount):
        self.loan_amount = loan_amount


    def getLoanAmount(self):
        return self.loan_amount

    def setInterestRate(self, interest_rate):
        self.interest_rate = interest_rate
        intrest_rate = int(interest_rate)
        return intrest_rate

    def getInterestRate(self):
        return self.interest_rate

    def setLoanPeriod(self, loan_period):
        self.loan_period = loan_period
        loan_period = int(loan_period)
        return loan_period

    def getLoanPeriod(self):
        return self.loan_period

    def setMonthlyPayment(self, monthly_payment):
        self.monthly_payment = (self.loan_amount * self.interest_rate) / 1 - (1 / (1 + self.interest_rate)) ** self.loan_period
        return monthly_payment

    def getMonthlyPayment(self):
        return self.monthly_payment

    def setTotalPayment(self, total_Payment):
        self.total_Payment = total_Payment
        total_Payment = int(total_Payment)
        return total_Payment

    def getTotalPayment(self):
        return self.total_Payment



loan = LoanContract("Femi", 15,3,2_000)
print(loan)




