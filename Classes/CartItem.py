
class CartItem:
    def __init__(self, product_name: str, quantity: int,inventory):
        self.set_ProductName(product_name)
        self.set_ProductQuantity(quantity)
        self.set_ProductSubtotal(inventory)

    def set_ProductName(self, product_name):
        self.__ProductName = product_name
    def get_ProductName(self):
        return self.__ProductName

    def set_ProductQuantity(self, quantity):
        self.__ProductQuantity = quantity
    def get_ProductQuantity(self):
        return self.__ProductQuantity

    def set_ProductSubtotal(self,inventory):
        if self.__ProductName in inventory:
            self.__ProductSubtotal = self.__ProductQuantity * inventory[self.__ProductName].get_Price()
        else:
            self.__ProductSubtotal = 0
    def get_ProductSubtotal(self):
        return self.__ProductSubtotal

    def increase_Quantity(self, amount=1):
        self.__ProductQuantity += amount
        self.set_ProductSubtotal()

    def decrease_Quantity(self, amount=1):
        if self.__ProductQuantity > amount:
            self.__ProductQuantity -= amount
        else:
            self.__ProductQuantity = 0
        self.set_ProductSubtotal()
