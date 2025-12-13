from Zad_1 import Student


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
    def __init__(self, employee, student, books):
        self.employee = employee

    def __str__(self):
        res=""
        #res = str(self.employee) + "\n"
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        for p in self.book:
            res = res + f"{p}\n"

def main():
    l1 = Library(city="Radom", street="Radomska", zip_code="12-345",open_hours=("pn - nieczynne", "wt 16 - 20", "śr 12 - 18"), phone="+48 1255645")
    l2 = Library(city="Kielce", street="Kielecka", zip_code="21-526", open_hours =("pn - 7 - 15", "wt nieczynne", "śr 12 - 18"), phone="+42 5864824")
    b1 = Book(library=l1, publication_date="2021-05-01", author_name="Kylo", author_surname="L", number_of_pages=333)
    b2 = Book(library=l1,publication_date="2022-01-05",author_name="Antoni", author_surname="S", number_of_pages=777)
    b3 = Book(library=l2,publication_date="2022-07-05",author_name="Jerzy", author_surname="T", number_of_pages=666)
    b4 = Book(library=l2, publication_date="2025-07-05", author_name="Karol", author_surname="W", number_of_pages=999)
    b5 = Book(library=l1, publication_date="2005-07-05", author_name="Tomasz", author_surname="W", number_of_pages=555)
    
    #print(l1)
    #print(l2)
    print(b1)
    print(b2)

if __name__ == '__main__':
    main()