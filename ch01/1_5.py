#应用序与正则序

def a():
    a()

def test(a,f):
    if a==0:
        return 0
    else:
        return f

if __name__ == '__main__':
    print(test(0,a))
