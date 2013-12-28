import csv
from collections import OrderedDict, namedtuple

def yearmonthshareprice():
    
    with open('datagen.csv') as datafile:
        reader = csv.reader(datafile)
        price_year_month = namedtuple('tup', ['price', 'year', 'month'])
        pricelist = OrderedDict()
        names = next(reader)[2:]
        for name in names:
            pricelist[name] = price_year_month(0, 'year', 'month')
        for row in reader:
            year, month = row[:2]         
            for name, price in zip(names, map(int, row[2:])): 
                if pricelist[name].price < price:
                    pricelist[name] = price_year_month(price, year, month)
    print pricelist        

yearmonthshareprice()
