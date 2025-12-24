import ast
from os import name
from unittest import case


class UnitTests:
    def is_palindrome(s: str) -> bool:
        return s.lower().replace(' ', '') == s[::-1].lower().replace(' ', '')

    def fibonacci(self, n: int) -> int:
        if n < 0:
            raise ValueError("n < 0")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(self, n - 1) + self.fibonacci(self, n - 2)

    def count_volwels(text: str) -> int:
        sam = "aeiouyąęó"
        return sum(1 for znak in text.lower() if znak in sam)

    def calculate_discount(price: float, discount: float) -> float:
        if (discount < 0) or (discount > 1):
            raise ValueError("discount must be between 0 and 1")
        return price - (price * discount)

    def flatten_list(self, nested_list: list) -> list:
        res = []
        for x in nested_list:
            if isinstance(x, list):
                res = res + self.flatten_list(self, x)
            else:
                res.append(x)
        return res

    def word_frequencies(text: str) -> dict:
        return 1

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def getInput(self):
        self.print_help()
        f = input("Podaj numer funkcji: ")
        match f:
            case "1":
                print(self.is_palindrome(input("Podaj palindrome: ")))
            case "2":
                print(self.fibonacci(self, input("Podaj n: ")))
            case "3":
                print(self.count_volwels(input("Podaj ciąg znaków: ")))
            case "4":
                f1, f2 = map(float, input("Podaj cenę i upust: ").split())
                print(self.calculate_discount(f1, f2))
            case "5":
                lista = ast.literal_eval(input("Podaj listę do spłaszczenia: "))
                print(self.flatten_list(self, lista))
            case "6":
                print(self.word_frequencies(input("Podaj ciąg do analizy: ")))
            case "7":
                print(self.is_prime(input("Podaj liczbe do przetestowania: ")))
            case _:
                self.print_help()

    def print_help():
        print("Wybierz funkcję:")
        print("  1, is_palindrome()")
        print("  2, fibonacci()")
        print("  3, count_volwels()")
        print("  4, calculate_discount()")
        print("  5, flatten_list()")
        print("  6, word_frequencies()")
        print("  7, is_prime()")


def main():
    Funkcje = UnitTests
    Funkcje.getInput(self=Funkcje)


if __name__ == '__main__':
    main()
