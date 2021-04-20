from Polynomial.polynomial import Polynomial


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    p = Polynomial([1, 2])
    p2 = Polynomial([5, 3, 4, 2])
    print(p + 2)
    print(2 + p)
    print(p)
    print(p2)
    p = p * p2
    print(p)
    p = p * 2
    print(p == p2)

    p1 = Polynomial([1, 1, 3])
    p2 = Polynomial([2, 2])
    print(p1 * p2)
    print(p2 * p1)

    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([2, 2])
    p3 = Polynomial([1, 2, 1])

    # Subtraction
    print(p1 - p2)
    print(p2 - p1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
