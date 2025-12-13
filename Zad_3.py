class Property:
    area:float
    rooms:[int]
    price:int
    adres:str
    def __init__(self,area:float,rooms:int,price:int,adres:str):
        self.area=area
        self.rooms=rooms
        self.price=price
        self.adres=adres
    def __str__(self):
        res = ""
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        return res
class House(Property):
    area:float
    rooms:int
    price:int

