class Amount:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def add(self, that):
        if (self.currency == that.currency):
            self.amount += that.amount
        else:
            raise CurrencyDoesNotMatchException(f'Currency does not match: {self.currency} and {that.currency}')
        
    def __repr__(self):
        return repr(
            (self.currency, self.amount)
        )
        

class CurrencyDoesNotMatchException(Exception):
    def __init__(self, message):
        super().__init__(message)        


amount1 = Amount('EURO', 70)
amount2 = Amount('INR', 35)
print(amount1)
print(amount2)
amount1.add(amount2)
print(amount1)
