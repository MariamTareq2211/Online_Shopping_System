from Customer import Customer
import datetime
class Order:
    def __init__(self,customer:Customer, status = "Processing",date=datetime.datetime.now()):
        self.set_CustomerName(customer.get_Name())
        self.set_Items(customer.cart.get_Items())
        self.set_Status(status)
        self.set_TotalPrice(customer.cart.calculate_TotalPrice())
        self.set_ShippingAddress(customer.get_ShippingAddress())
        self.set_Date(date)

    def set_CustomerName(self,name):
        self.__CustomerName = name
    def get_CustomerName(self):
        return self.__CustomerName
    
    def set_Items(self,items):
        self.__Items = items    
    def get_Items(self):
        return self.__Items
    
    def set_Status(self,status):
        self.__Status = status
    def get_Status(self):
        return self.__Status
    
    def set_TotalPrice(self,totalprice):
        self.__TotalPrice = totalprice
    def get_TotalPrice(self):
        return self.__TotalPrice
    
    def set_ShippingAddress(self,address):
        self.__ShippingAddress = address
    def get_ShippingAddress(self):
        return self.__ShippingAddress
    
    def set_Date(self,date):
        self.__Date = date
    def get_Date(self):
        return self.__Date
    
    def confirm_order(self,orders):
        orders.append(self)

    def cancel_order(self,orders):
        if self in orders:
            orders.remove(self)
            print(f"The order has been canceled")
        else:
            print("Order not found in system !!")
