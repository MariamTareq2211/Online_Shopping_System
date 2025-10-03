import os
import datetime
from Classes.User import User
from Classes.Customer import Customer
from Classes.Admin import Admin
from Classes.Product import Product
from Classes.Cart import Cart
from Classes.CartItem import CartItem
from Classes.Order import Order

class SystemFunctions:
    def __init__(self):
        self.Orders = []
        self.Customers = []
        self.Admins = []
        self.Inventory = {}

    # -------------------- Read Methods --------------------
    def read_inventory(self, file_path="Files/Inventory.txt"):
        self.Inventory = {}
        if not os.path.exists(file_path):
            print(f"Inventory file '{file_path}' not found!")
            return

        with open(file_path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue  # skip empty lines
                parts = [x.strip() for x in line.split(",")]
                if len(parts) != 4:
                    print(f"[Inventory] Line {line_no} skipped (expected 4 values): {line}")
                    continue
                try:
                    name, category, price, stock = parts
                    self.Inventory[name] = Product(name, category, float(price), int(stock))
                except Exception as e:
                    print(f"[Inventory] Error on line {line_no}: {line} -> {e}")

        print(f"{len(self.Inventory)} products loaded into inventory.")

    def read_customers(self, file_path="Files/Customers.txt"):
        self.Customers = []
        if not os.path.exists(file_path):
            print(f"Customers file '{file_path}' not found!")
            return

        with open(file_path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = [x.strip() for x in line.split(",")]
                if len(parts) != 9:
                    print(f"[Customer] Line {line_no} skipped (expected 9 values): {line}")
                    continue
                try:
                    name, phone, email, gender, role, username, password, country, city = parts
                    cart = Cart(name)
                    self.Customers.append(Customer(name, phone, email, gender, role, username, password, country, city, cart))
                except Exception as e:
                    print(f"[Customer] Error on line {line_no}: {line} -> {e}")

        print(f"{len(self.Customers)} customers loaded.")

    def read_admins(self, file_path="Files/Admins.txt"):
        self.Admins = []
        if not os.path.exists(file_path):
            print(f"Admins file '{file_path}' not found!")
            return

        with open(file_path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = [x.strip() for x in line.split(",")]
                if len(parts) != 9:
                    print(f"[Admin] Line {line_no} skipped (expected 9 values): {line}")
                    continue
                try:
                    name, phone, email, gender, role, username, password, nationalid, age = parts
                    self.Admins.append(Admin(name, phone, email, gender, role, username, password, nationalid, int(age)))
                except Exception as e:
                    print(f"[Admin] Error on line {line_no}: {line} -> {e}")

        print(f"{len(self.Admins)} admins loaded.")

    def read_orders(self, file_path="Files/Orders.txt"):
        self.Orders = []
        if not os.path.exists(file_path):
            print(f"Orders file '{file_path}' not found!")
            return

        with open(file_path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = [x.strip() for x in line.split("|")]
                if len(parts) != 5:
                    print(f"[Orders] Line {line_no} skipped (expected 5 values): {line}")
                    continue
                try:
                    customer_name, status, total_price, shipping_address, date_str = parts
                    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

                    # create a fake customer object with empty cart
                    fake_customer = Customer(customer_name, "", "", "", "Customer", customer_name, "", "", "", Cart(customer_name))
                    order = Order(fake_customer, status, date)
                    self.Orders.append(order)
                except Exception as e:
                    print(f"[Orders] Error on line {line_no}: {line} -> {e}")

        print(f"{len(self.Orders)} orders loaded.")

    
    def save_inventory(self, file_path="Files/Inventory.txt"):
        with open(file_path, "w", encoding="utf-8") as f:
            for product in self.Inventory.values():
                line = f"{product.get_Name()},{product.get_Category()},{product.get_Price()},{product.get_Stock()}\n"
                f.write(line)
        print(f"{len(self.Inventory)} products saved to {file_path}.")

    def save_customers(self, file_path="Files/Customers.txt"):
        with open(file_path, "w", encoding="utf-8") as f:
            for c in self.Customers:
                line = f"{c.get_Name()},{c.get_Phone()},{c.get_Email()},{c.get_Gender()},{c.get_Role()},{c.get_Username()},{c.get_Password()},{c.get_Country()},{c.get_City()}\n"
                f.write(line)
        print(f"{len(self.Customers)} customers saved to {file_path}.")

    def save_admins(self, file_path="Files/Admins.txt"):
        with open(file_path, "w", encoding="utf-8") as f:
            for a in self.Admins:
                line = f"{a.get_Name()},{a.get_Phone()},{a.get_Email()},{a.get_Gender()},{a.get_Role()},{a.get_Username()},{a.get_Password()},{a.get_NationalID()},{a.get_Age()}\n"
                f.write(line)
        print(f"{len(self.Admins)} admins saved to {file_path}.")

    def save_orders(self, file_path="Files/Orders.txt"):
        with open(file_path, "w", encoding="utf-8") as f:
            for o in self.Orders:
                line = f"{o.get_CustomerName()}|{o.get_Status()}|{o.get_TotalPrice()}|{o.get_ShippingAddress()}|{o.get_Date().strftime('%Y-%m-%d %H:%M:%S')}\n"
                f.write(line)
        print(f"{len(self.Orders)} orders saved to {file_path}.")