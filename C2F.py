def c2f(c):
    if -273.15 > c:
        return "temperature too lower"
    else:
        f = c * 9 / 5 + 32
        return f

temperatures=[10, -20, -289, 100]

for t in temperatures:
    print(c2f(t))
