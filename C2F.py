def c2f(c):
    if -273.15 > c:
        return ""
    else:
        f = c * 9 / 5 + 32
        return f

with open('example.txt', 'r') as file:
    temperatures = file.readlines()

temperatures = [float(t.rstrip()) for t in temperatures]

for t in temperatures:
    print(c2f(t))


temperatures=[10,-20,-289,100]

def writer(temperatures):
    with open("example2.txt", 'w') as file:
        for c in temperatures:
            if c>-273.15:
                f=c*9/5+32
                file.write(str(f)+"\n")

writer(temperatures)
