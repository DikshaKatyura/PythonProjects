def grid(n, m):
    """
    This function will calculate
    the number of square in a
    grid of any dimensions.
    """
    if n == 1 or m == 1:
        return n * m
    else:
        return n * m + grid(n - 1, m - 1)


num1 = int(input("Enter 1st dimension of the Grid\n"))
num2 = int(input("Enter 2nd dimension of the Grid\n"))
square = grid(num1, num2)
print(square)

