class Property:
    area: float
    rooms: [int]
    price: int
    adres: str

    def __init__(self, area: float, rooms: int, price: int, adres: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.adres = adres

    def __str__(self):
        res = ""
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        return res


class House(Property):
    plot: int

    def __init__(self, area: float, rooms: int, price: int, adres: str, plot: int):
        Property.__init__(self, area, rooms, price, adres)
        self.plot = plot

    def __str__(self):
        res = ""
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        return res


class Flat(Property):
    floor: int

    def __init__(self, area: float, rooms: int, price: int, adres: str, floor: int):
        Property.__init__(self, area, rooms, price, adres)
        self.floor = floor

    def __str__(self):
        res = ""
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        return res


def main():
    h = House(area=485, rooms=12, price=25458456, adres="Sielanka", plot=1254)
    f = Flat(area=275, rooms=7, price=1256, adres="Sielanka", floor=2)
    print(h)
    print(f)


if __name__ == "__main__":
    main()
