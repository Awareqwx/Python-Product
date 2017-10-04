class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    def sell(self):
        self.status = "Sold"
        return self
    def addTax(self, t):
        return self.price + self.price * t
    def takeBack(self, r):
        if r == "Defective":
            self.status = "Defective"
            self.price = 0
        elif r == "Like new"
            self.status = "For Sale"
        elif r == "Opened"
            self.status = "For Sale, used"
            self.price *= 0.8
        else
            print "You can't return that"
        return self
    def displayInfo(self):                
        print "Price: $" + str(self.price)
        print "Name: " + self.name
        print "Weight: " + str(self.weight) + "kg"
        print "Brand: " + self.brand
        print "Status: " + self.status
        return self