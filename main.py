import polynomial


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    p = polynomial.Polynomial([1, 2])
    p2 = polynomial.Polynomial([5, 3, 4, 2])
    p = p * 2
    print(p.coeffs)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
