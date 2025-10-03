from CartItem import CartItem

class Cart:
    def __init__(self, customer_name, items=None):
        self.set_CustomerName(customer_name)
        self.__items = items if items is not None else []

    def set_CustomerName(self, customer_name):
        self.__CustomerName = customer_name
    def get_CustomerName(self):
        return self.__CustomerName

    def set_Items(self, items):
        self.__items = items
    def get_Items(self):
        return self.__items

    def add_Item(self, cart_item: CartItem):
        for item in self.__items:
            if item.get_ProductName() == cart_item.get_ProductName():
                item.set_ProductQuantity(item.get_ProductQuantity() + cart_item.get_ProductQuantity())
                item.set_ProductSubtotal()  
                return
        self.__items.append(cart_item)

    def remove_Item(self, product_name):
        self.__items = [item for item in self.__items if item.get_ProductName() != product_name]


    def decrease_ItemQuantity(self, product_name, amount=1):
        for item in self.__items:
            if item.get_ProductName() == product_name:
                if item.get_ProductQuantity() > amount:
                    item.set_ProductQuantity(item.get_ProductQuantity() - amount)
                    item.set_ProductSubtotal()
                else:
                    self.__items.remove(item) 
                return

    def empty_Cart(self):
        self.__items.clear()

    def calculate_TotalPrice(self):
        total = 0
        for item in self.__items:
            total += item.get_ProductSubtotal()
        return total

    def display_Cart(self):
        if self.__items:
            print("\n================= Your Cart =================")
            print(f"{'Product':<15}{'Quantity':<10}{'Subtotal':<10}")
            print("-" * 40)

            for item in self.__items:
                print(f"{item.get_ProductName():<15}{item.get_ProductQuantity():<10}{item.get_ProductSubtotal():<10}")

            print("-" * 40)
            print(f"Total Items: {len(self.__items)}")
            print(f"Shipping Cost: 50 EGP")
            print(f"Total Price (incl. Shipping): {self.calculate_TotalPrice() + 50} EGP")
            print("============================================\n")
        else:
            print("\nYour Cart is Empty !!\n")
