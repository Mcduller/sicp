# 求一个数与另一个数的绝对值的和

def a_plus_abs_b(a, b):
    return a + b if b > 0 else a - b


if __name__ == '__main__':
    print(a_plus_abs_b(1, -2))
