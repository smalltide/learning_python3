def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars

r = input('rate: ')
e = input('euros: ')

print(currency_converter(float(r), float(e)))
