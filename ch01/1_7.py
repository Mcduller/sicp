# 牛顿法求平方根

def good_enough(odlguess, newguess):
    return abs(newguess - odlguess) / odlguess < 0.00001


def improve(guess, x):
    return (guess + (x / guess)) / 2


def sqrt_iter(guess, x):
    if good_enough(guess, improve(guess, x)):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)

def sqrt(x):
    return sqrt_iter(1.0, x)

if __name__ == '__main__':
    print(sqrt(sqrt(4)+sqrt(4)))
