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


class Library:
    city: str
    street: str
    zip_code: str
    open_hours: list
    phone: str

    def __init__(self, city: str, street: str, zip_code: str, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
        self.open_hours = open_hours

    def __str__(self):
        res = ""
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        return res

    class Student:
        avg = 3
        name: str
        marks = []

        def __init__(self, name: str, marks: list):
            self.name = name
            self.marks = marks

        def is_passed(self):
            if self.average() > self.avg:
                return True
            else:
                return False

        def average(self):
            return sum(self.marks) / len(self.marks)

        def add_mark(self, mark: int):
            self.marks.append(mark)

        def __str__(self):
            return f"{self.name}: {self.average()}"


class Student:
    avg = 3
    name: str
    marks = []

    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if self.average() > self.avg:
            return True
        else:
            return False

    def average(self):
        return sum(self.marks) / len(self.marks)

    def add_mark(self, mark: int):
        self.marks.append(mark)

    def __str__(self):
        return f"{self.name}: {self.average()}"