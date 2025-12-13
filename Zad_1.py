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


def main():
    s1 = Student("Kylo", [2, 5, 3, 3, 4, 5, 4])
    s2 = Student("Bolo", [3, 2, 2, 3, 3, 4, 4])
    print(s1)
    print(s1.is_passed())
    print(s2)
    print(s2.is_passed())


if __name__ == '__main__':
    main()
