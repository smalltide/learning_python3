print(1)

def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars

print(currency_converter(100, 1000))

functions = [currency_converter(10, 100), currency_converter(5,100)]

print(functions)
