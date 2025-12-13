from Zad_1 import Student
from datetime import date

class Library:
    city: str
    street: str
    zip_code: str
    open_hours:list
    phone:str
    def __init__(self, city: str, street: str, zip_code: str, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
        self.open_hours = open_hours
        #def open_hours(self, open_hours: str):

    def __str__(self):
        res = ""
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        return res

class Employee:
    first_name: str
    last_name: str
    hire_date: str
    birth_date: str
    city: str
    street: str
    zip_code: str
    phone: str

    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        res = ""
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        return res

class Book:
    library: Library
    publication_date: str
    author_name: str
    author_surname: str
    number_of_pages: int

    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        res = ""
        #res = str(self.library) + "\n"
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        return res

class Order:
    employee: Employee
    student: str
    books: [Book]
    order_date:str
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.books= books
        self.order_date = order_date

    def __str__(self):
        res=""
        #res = str(self.employee) + "\n"
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        for p in self.books:
            res = res + f"{p}\n"
        return res

def main():
    l1 = Library(city="Radom", street="Radomska", zip_code="12-345",open_hours=("pn - nieczynne", "wt 16 - 20", "śr 12 - 18"), phone="+48 1255645")
    l2 = Library(city="Kielce", street="Kielecka", zip_code="21-526", open_hours =("pn - 7 - 15", "wt nieczynne", "śr 12 - 18"), phone="+42 5864824")

    b1 = Book(library=l1, publication_date="2021-05-01", author_name="Kylo", author_surname="L", number_of_pages=333)
    b2 = Book(library=l1,publication_date="2022-01-05",author_name="Antoni", author_surname="S", number_of_pages=777)
    b3 = Book(library=l2,publication_date="2022-07-05",author_name="Jerzy", author_surname="T", number_of_pages=666)
    b4 = Book(library=l2, publication_date="2025-07-05", author_name="Karol", author_surname="W", number_of_pages=999)
    b5 = Book(library=l1, publication_date="2005-07-05", author_name="Tomasz", author_surname="W", number_of_pages=555)

    e1 = Employee("Kylo", "L", hire_date="2025-02-15", birth_date="2018-06-12", city="Gdynia", street="Gdyńska", zip_code="12-345", phone="+48 1255645")
    e2 = Employee("Adam", "Z", hire_date="2024-01-15", birth_date="2048-06-12", city="Gdynia", street="Gdyńska",zip_code="12-345", phone="+48 1255645")
    e3 = Employee("Bolo", "L", hire_date="2025-02-15", birth_date="2018-06-12", city="Gdynia", street="Gdyńska", zip_code="12-345", phone="+48 1255645")

    s1 = Student("Jan",[])
    s2 = Student("Andrzej", [])

    o1 = Order(employee=e1, student=s1, books=[b1,b4,b5], order_date=date.today())
    o2 = Order(employee=e2, student=s2, books=[b2, b3], order_date=date.today())

    print(o1)
    print(o2)

if __name__ == '__main__':
    main()