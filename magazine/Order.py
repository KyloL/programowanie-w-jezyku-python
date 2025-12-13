import magazine.Utils as Utils
import  magazine.Product as Product

class Order:
    employee: Utils.Employee
    student: str
    books: [Product.Book]
    order_date: str

    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.books = books
        self.order_date = order_date

    def __str__(self):
        res = ""
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        for p in self.books:
            res = res + f"{p}\n"
        return res