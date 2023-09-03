from enum import Enum

class Currency(Enum):
    USD = 1
    INR = 2
    EURO = 3


for currency in Currency:
    print(f'{currency.name} val is {currency.value}')

