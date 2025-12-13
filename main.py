from datetime import date
import magazine.Product as Product
import magazine.Utils as Utils
import magazine.Order as Order


def main():
    l1 = Utils.Library(city="Radom", street="Radomska", zip_code="12-345",
                       open_hours=("pn - nieczynne", "wt 16 - 20", "śr 12 - 18"), phone="+48 1255645")
    l2 = Utils.Library(city="Kielce", street="Kielecka", zip_code="21-526",
                       open_hours=("pn - 7 - 15", "wt nieczynne", "śr 12 - 18"), phone="+42 5864824")

    b1 = Product.Book(library=l1, publication_date="2021-05-01", author_name="Kylo", author_surname="L", number_of_pages=333)
    b2 = Product.Book(library=l1, publication_date="2022-01-05", author_name="Antoni", author_surname="S", number_of_pages=777)
    b3 = Product.Book(library=l2, publication_date="2022-07-05", author_name="Jerzy", author_surname="T", number_of_pages=666)
    b4 = Product.Book(library=l2, publication_date="2025-07-05", author_name="Karol", author_surname="W", number_of_pages=999)
    b5 = Product.Book(library=l1, publication_date="2005-07-05", author_name="Tomasz", author_surname="W", number_of_pages=555)

    e1 = Utils.Employee("Kylo", "L", hire_date="2025-02-15", birth_date="2018-06-12", city="Gdynia", street="Gdyńska",
                        zip_code="12-345", phone="+48 1255645")
    e2 = Utils.Employee("Adam", "Z", hire_date="2024-01-15", birth_date="2048-06-12", city="Gdynia", street="Gdyńska",
                        zip_code="12-345", phone="+48 1255645")
    e3 = Utils.Employee("Bolo", "L", hire_date="2025-02-15", birth_date="2018-06-12", city="Gdynia", street="Gdyńska",
                        zip_code="12-345", phone="+48 1255645")

    s1 = Utils.Student("Jan", [])
    s2 = Utils.Student("Andrzej", [])

    o1 = Order.Order(employee=e1, student=s1, books=[b1, b4, b5], order_date=date.today())
    o2 = Order.Order(employee=e2, student=s2, books=[b2, b3], order_date=date.today())

    print(o1)
    print(o2)


if __name__ == '__main__':
    main()
