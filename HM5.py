import random
def genere():
    a = int(raw_input("plese enter first number"))
    b = int(raw_input("plese enter second number"))
    r = int(raw_input('please enter range'))
    l = [random.randint(a, b) for n in range(0, r)]
    print l
    return l
y = genere()
def u():
    while True:
            num1 = int(raw_input("plese enter value"))
            for i, b in enumerate(y):
                if num1 == y[i]+y[b]:
                    num = y[i], y[b]
            print num
            break
u()