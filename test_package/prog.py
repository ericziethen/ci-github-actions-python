"""Test Module."""


def sum_numbers(num1, num2):
    """Sum the given numbers."""
    return num1 + num2


def main():
    """Run Main function."""
    num1 = 5
    num2 = 2
    print(F'Summing "{num1}" and "{num2}" equals "{sum_numbers(num1, num2)}"')


if __name__ == '__main__':
    main()
