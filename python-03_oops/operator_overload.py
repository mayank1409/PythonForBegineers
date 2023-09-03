from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.currency, self.amount + other.amount)
        else:
            raise Exception('Currency does not match')
        

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.currency, self.amount - other.amount)
        else:
            raise Exception('Currency does not match')
        

    def __eq__(self, other):
        return (self.currency, self.amount) == (other.currency, other.amount)
    

    def __gt__(self, other):
        return self.amount > other.amount
    

    def __repr__(self):
        return repr(
            (self.currency, self.amount)
        )


amt1 = Money('USD', 10)
amt2 = Money('USD', 10)
print(amt1 + amt2)
print(amt2 - amt1)
print('Is amt1 == amt2 ', amt1 == amt2)
print('Is amt1 != amt2 ', amt1 != amt2)
print('Is amt1 > amt2 ', amt1 > amt2)
print('Is amt1 < amt2 ', amt1 < amt2)
print('Is amt1 >= amt2 ', amt1 >= amt2)
print('Is amt1 <= amt2 ', amt1 <= amt2)
