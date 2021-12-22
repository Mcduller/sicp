# 求三个数中较大两个数得平方和
def square(args):
    return args * args


def min(a, b):
    return a if a < b else b


def max_two_of_three(a, b, c):
    return - min(min(a, b), c)


def sum_two_max_define_of_three(a, b, c, f):
    return (f(a) + f(b) + f(c)) - f(min(min(a, b), c))


if __name__ == '__main__':
    print(sum_two_max_define_of_three(1, 2, 3, square))
