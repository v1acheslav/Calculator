#!/usr/bin/python3


class ProductPrice:
    pass


class product:

    def __init__(self, price, name, description =""):
        self.price = ProductPrice()
        self.name = name
        self.description = description

    def get_sell_price (self, vat=0.2):
        print(self.name + " product")
        return self.price + self.price * vat


tv = product(10, 'tv')
radio = product(5, 'radio')

print(tv.get_sell_price())
print(radio.get_sell_price())


class Product2(product):

    def get_sell_price(self, vat=0.2):
        print(self.name + " product2")
        return self.price + 10



tv2 = Product2(10, 'tv2')

print(tv2.get_sell_price())












