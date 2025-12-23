def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def count_volwels(text: str) -> int:
    sam = "aeiouyąęó"
    return sum(1 for znak in text.lower() if znak in sam)


def calculate_discount(price: float, discount: float) -> float:
    if (discount < 0) or (discount > 1) :
        raise ValueError("discount must be between 0 and 1")
    return price * discount


def flatten_list(nested_list: list) -> list:
    res = []
    for x in nested_list:
        res = res + [x]
    return res


def word_frequencies(text: str) -> dict:
    return 1


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False



def main():
    print(flatten_list([1, [2, 3], [4, [5]]]))



if __name__ == '__main__':
    main()
