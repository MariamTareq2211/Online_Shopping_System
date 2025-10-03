from Classes.User import User
from Classes.Cart import Cart
from Classes.CartItem import CartItem

class Customer(User):
    def __init__(self,name, phone,email,gender,role,username,password,country,city,cart):
        super().__init__(name, phone,email,gender,role,username,password)
        self.set_Country(country)
        self.set_City(city)
        self.set_Cart(cart)
        self.set_ShippingAddress()


    def set_Country(self,country):
        self.__Country = country
    def get_Country(self):
        return self.__Country
    
    def set_City(self,city):
        self.__City = city
    def get_City(self):
        return self.__City 
    
    def set_Cart(self,cart):
        self.__Cart = cart
    def get_Cart(self):
        return self.__Cart

    def set_ShippingAddress(self):
        self.__ShippingAddress = f"{self.__Country}, {self.__City}"  
    def get_ShippingAddress(self):
        return self.__ShippingAddress

    def update_profile(self, name=None, phone=None, email=None, city=None, country=None):
        if name: self.set_Name(name)
        if phone: self.set_Phone(phone)
        if email: self.set_Email(email)
        if city: self.set_City(city)
        if country: self.set_Country(country)
        self.set_ShippingAddress()

    def change_password(self, new_password):
        self.set_Password(new_password)

    def add_to_cart(self, product_name, quantity, inventory):
        if product_name in inventory:
            product = inventory[product_name]
            if quantity <= product.get_Stock():
                cart_item = CartItem(product_name, quantity)
                self.__Cart.add_Item(cart_item)
                print(f"{quantity} x {product_name} added to your cart.")
            else:
                print(f"Only {product.get_Stock()} units of {product_name} available in stock.")
        else:
            print("Product not found in inventory.")

    def remove_from_cart(self, product_name):
        self.__Cart.remove_Item(product_name)
        print(f"{product_name} removed from cart.")

    def decrease_cart_item(self, product_name, amount=1):
        self.__Cart.decrease_ItemQuantity(product_name, amount)

    def empty_cart(self):
        self.__Cart.empty_Cart()
        print("Cart emptied.")

    def view_cart(self):
        self.__Cart.display_Cart()


    def place_order(self, orders):
        import datetime
        from Classes.Order import Order

        if not self.__Cart.get_Items():
            print("Your cart is empty. Add products before placing an order.")
            return

        order = Order(
            customer_name=self.get_Name(),
            items=self.__Cart.get_Items(),
            total_price=self.__Cart.calculate_TotalPrice(),
            shipping_address=self.get_ShippingAddress(),
            status="Processing",
            date=datetime.datetime.now()
        )
        orders.append(order)
        print(f"Order placed for {self.get_Name()} on {order.get_Date()}")
        self.empty_cart()

    def cancel_order(self, orders, order):
        if order in orders and order.get_Status() == "Processing":
            orders.remove(order)
            print("Order cancelled.")
        else:
            print("Cannot cancel this order.")

    def view_my_orders(self, orders):
        my_orders = [o for o in orders if o.get_CustomerName() == self.get_Name()]
        if not my_orders:
            print("No orders found.")
        else:
            for o in my_orders:
                print(f"{o.get_Date()} | {o.get_Status()} | {o.get_TotalPrice()} EGP")


    def display_info(self):
        print(f"""
                Name: {self.get_Name()}
                Phone Number: {self.get_Phone()}
                Email: {self.get_Email()}
                Shipping Address: {self.get_ShippingAddress()}
                """)
        
    