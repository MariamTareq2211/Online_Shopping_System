from collections import defaultdict
from User import User
from Product import Product

class Admin(User):
    def __init__(self, name, phone, email, gender, role, username, password, nationalid, age):
        super().__init__(name, phone, email, gender, role, username, password)
        self.set_NationalID(nationalid)
        self.set_Age(age)

    
    def set_NationalID(self, nationalid):
        self.__NationalID = nationalid
    def get_NationalID(self):
        return self.__NationalID
    
    def set_Age(self, age):
        self.__Age = age
    def get_Age(self):
        return self.__Age 
    
    def display_profile(self):
        print(f"""
                Name: {self.get_Name()}
                Age: {self.get_Age()}
                Phone Number: {self.get_Phone()}
                Email: {self.get_Email()}
                National ID: {self.get_NationalID()}
                """)

    
    def add_product(self, name, category, price, stock, inventory: dict):
        if name in inventory:
            print("This product is already in the inventory\n")
        else:
            inventory[name] = Product(name, category, price, stock)
            print(f"{name} added to inventory.")

    def update_product(self, product_name, price=None, stock=None, inventory: dict=None):
        if product_name in inventory:
            product = inventory[product_name]
            if price is not None:
                product.set_Price(price)
            if stock is not None:
                product.set_Stock(stock)
            print(f"{product_name} updated.")
        else:
            print("Product not found.")

    def remove_product(self, product_name, inventory: dict):
        if product_name in inventory:
            del inventory[product_name]
            print(f"{product_name} removed from inventory.")
        else:
            print("Product not found.")

   
    def view_all_orders(self, orders):
        for order in orders:
            print(f"{order.get_CustomerName()} | {order.get_Status()} | {order.get_TotalPrice()} EGP")

    def update_order_status(self, order, new_status):
        order.set_Status(new_status)
        print(f"Order for {order.get_CustomerName()} updated to {new_status}")

    
    def view_all_customers(self, customers):
        for customer in customers:
            customer.display_profile()

    def remove_customer(self, customers, username):
        customers[:] = [c for c in customers if c.get_Username() != username]

    def search_customer(self, customers, username):
        return next((c for c in customers if c.get_Username() == username), None)

    
    def generate_customer_report(self, customers, orders):
        total_customers = len(customers)
        total_sales = sum(order.get_TotalPrice() for order in orders)

        print("Customer Report:")
        print(f"Total Customers: {total_customers}")
        print(f"Total Sales: {total_sales} EGP")

    def sales_per_day(self, orders):
        sales_by_day = defaultdict(float)
        for order in orders:
            date_str = order.get_Date().strftime("%Y-%m-%d")  # group by date
            sales_by_day[date_str] += order.get_TotalPrice()

        print("Sales Per Day:")
        for date, total in sales_by_day.items():
            print(f"{date}: {total} EGP")
