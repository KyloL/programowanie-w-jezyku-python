import requests
from cupshelpers.debug import nonfatalException

url = 'https://api.openbrewerydb.org/v1/breweries' #'https://api.openbrewerydb.org/breweries'

class Brewery:
    id: str
    name: str
    brewery_type = ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor', 'closed']
    address_1:str
    address_2:str
    address_3:str
    city:str
    state_province:str
    postal_code:str
    country:str
    longitude:int
    latitude:int
    phone:str
    website_url:str
    state:str
    street:str
    def __init__(self, brewery):
        self.id=brewery["id"]
        self.name=brewery["name"]
        self.brewery_type=brewery["brewery_type"]
        self.address_1=brewery["address_1"]
        self.address_2=brewery["address_2"]
        self.address_3=brewery["address_3"]
        self.city=brewery["city"]
        self.state_province=brewery["state_province"]
        self.postal_code=brewery["postal_code"]
        self.country=brewery["country"]
        self.longitude=brewery["longitude"]
        self.latitude=brewery["latitude"]
        self.phone=brewery["phone"]
        self.website_url=brewery["website_url"]
        self.state=brewery["state"]
        self.street=brewery["street"]
    def __str__(self):
        #return f"Id: {self.id}, Nazwa: {self.name}, Typ: {self.brewery_type}"
        return str([w for w in self.__dict__.values()])

res = requests.get(url)
breweries = res.json()
bw = []
i=0

#for i in range(20):
#return [n**3 for n in tmp]

for b in breweries:
    bw.append(Brewery(brewery=b))
    print(str(i) + " - " + str(bw[i]))
    i = i + 1
    if i > 10: break