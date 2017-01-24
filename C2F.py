def c2f(c):
    if -273.15 > c:
        return "temperature too lower"
    else:
        f = c * 9 / 5 + 32
        return f

print(c2f(-273.16))
