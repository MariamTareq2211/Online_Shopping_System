from Product import Product

class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.set_Product(product)
        self.set_ProductQuantity(quantity)
        self.set_ProductSubtotal()

    def set_Product(self, product):
        self.__Product = product
    def get_Product(self):
        return self.__Product

    def set_ProductQuantity(self, quantity):
        self.__ProductQuantity = quantity
    def get_ProductQuantity(self):
        return self.__ProductQuantity

    def set_ProductSubtotal(self):
        self.__ProductSubtotal = self.__ProductQuantity * self.__Product.get_Price()
    def get_ProductSubtotal(self):
        return self.__ProductSubtotal

    def get_ProductName(self):
        return self.__Product.get_Name()

    def increase_Quantity(self, amount=1):
        self.__ProductQuantity += amount
        self.set_ProductSubtotal()

    def decrease_Quantity(self, amount=1):
        if self.__ProductQuantity > amount:
            self.__ProductQuantity -= amount
        else:
            self.__ProductQuantity = 0 
        self.set_ProductSubtotal()