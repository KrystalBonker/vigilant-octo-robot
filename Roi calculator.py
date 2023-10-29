class RentalRoi:
    def __init__(self,income,expenses,cash_on_cashroi):
        self.income = income
        self.expenses = expenses
        self.cash_on_cashroi = cash_on_cashroi

    def return_on_investment(self):
        monthly_cashflow = self.income - self.expenses
        annual_cashflow = monthly_cashflow * 12
        roi = annual_cashflow/self.cash_on_cashroi * 100
        return roi


   
property = RentalRoi(2800,1500,70000)
percent = property.return_on_investment()
print(f"The return on investment for this property is {percent} %")
