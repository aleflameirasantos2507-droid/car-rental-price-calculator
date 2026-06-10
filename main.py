km = float(input('How many kilometers were driven? '))
days = int(input('For how many days was the car rented? '))

price = km * 0.15 + days * 60

print(
    'Considering that you drove {} km during a period of {} days, the amount to pay is R${:.2f}'.format(
        km, days, price
    )
)
