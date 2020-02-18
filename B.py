from enum import Enum
while True:
    class converter (Enum):
        USD=1
        EUR=2
        CZK=3
        PLN=4
    try:
        p= converter [input('currency: ')]
        x=float(input('amount of money: '))
    except ValueError:
        print("Vedu shoc normalne plz")
    
    t=0
    if p==converter.USD:
        t=x*24.6
        print(f'The amount {t} UAH in {x} USD')
    elif p==converter.EUR:
        t=x*26.9
        print(f'The amount {t} UAH in {x} EUR')
    elif p==converter.CZK:
        t=x*1.1
        print(f'The amount {t} UAH in {x} CZK')
    elif p==converter.PLN:
        t=x*6.25
        print(f'The amount {t} UAH in {x} PLN')
    n = input("Введи число 1 якщо хочеш продовжити ")
    if n == '1':
        continue
    else:
        break
