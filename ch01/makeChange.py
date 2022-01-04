def denomination(kinds):
    if kinds == 5:
        return 50
    elif kinds == 4:
        return 25
    elif kinds == 3:
        return 10
    elif kinds == 2:
        return 5
    elif kinds == 1:
        return 1


def makeChange(amount, kinds):
    if amount == 0:
        return 1
    if amount < 0 or kinds == 0:
        return 0
    return makeChange(amount, kinds - 1) + makeChange(amount - denomination(kinds), kinds)


if __name__ == '__main__':
    print(makeChange(100, 5))
