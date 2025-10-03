class Product:
    def __init__(self, name, category, price, stock):
        self.set_Name(name)
        self.set_Category(category)
        self.set_Price(price)
        self.set_Stock(stock)

    def set_Name(self, name):
        self.__Name = name
    def get_Name(self):
        return self.__Name 
    
    def set_Category(self, category):
        self.__Category = category
    def get_Category(self):
        return self.__Category
    
    def set_Price(self, price):
        self.__Price = price
    def get_Price(self):
        return self.__Price

    def set_Stock(self, stock):
        self.__Stock = stock
    def get_Stock(self):
        return self.__Stock
