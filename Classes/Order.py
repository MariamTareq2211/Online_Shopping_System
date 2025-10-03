import datetime

class Order:
    def __init__(self, customer=None, customer_name=None, status="Processing",
             total_price=None, shipping_address=None, date=None, items=None):
        if date is None:
            date = datetime.datetime.now()

        if customer:  # when placing a new order
            self.set_CustomerName(customer.get_Name())
            self.set_Items(list(customer.get_Cart().get_Items()))
            self.set_Status(status)
            self.set_TotalPrice(customer.get_Cart().calculate_TotalPrice())
            self.set_ShippingAddress(customer.get_ShippingAddress())
            self.set_Date(date)
        else:  # when loading from file
            self.set_CustomerName(customer_name)
            self.set_Items(items if items else [])
            self.set_Status(status)
            self.set_TotalPrice(float(total_price))
            self.set_ShippingAddress(shipping_address)
            self.set_Date(date)

    # ---------------- Getters & Setters ----------------
    def set_CustomerName(self, name):
        self.__CustomerName = name
    def get_CustomerName(self):
        return self.__CustomerName
    
    def set_Items(self, items):
        self.__Items = items    
    def get_Items(self):
        return self.__Items
    
    def set_Status(self, status):
        self.__Status = status
    def get_Status(self):
        return self.__Status
    
    def set_TotalPrice(self, totalprice):
        self.__TotalPrice = totalprice
    def get_TotalPrice(self):
        return self.__TotalPrice
    
    def set_ShippingAddress(self, address):
        self.__ShippingAddress = address
    def get_ShippingAddress(self):
        return self.__ShippingAddress
    
    def set_Date(self, date):
        self.__Date = date
    def get_Date(self):
        return self.__Date

    # ---------------- Behaviors ----------------
    def confirm_order(self, orders):
        orders.append(self)
        print("Order confirmed and added to system.")

    def cancel_order(self, orders):
        if self in orders:
            orders.remove(self)
            print("The order has been canceled.")
        else:
            print("Order not found in system !!")

    def display_order(self):
        print(f"""
        Customer: {self.get_CustomerName()}
        Status: {self.get_Status()}
        Date: {self.get_Date()}
        Shipping Address: {self.get_ShippingAddress()}
        Total Price: {self.get_TotalPrice()} EGP
        Items: {[(item.get_ProductName(), item.get_Quantity()) for item in self.get_Items()]}
        """)
