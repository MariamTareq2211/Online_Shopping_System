import datetime
from Classes.User import User
from Classes.CartItem import CartItem
from Classes.Cart import Cart
from Classes.Product import Product
from Classes.Order import Order
from Classes.Admin import Admin
from Classes.Customer import Customer
from SystemFunctions import SystemFunctions
def main():
    system = SystemFunctions()

    # Load data from files
    system.read_inventory()
    system.read_customers()
    system.read_admins()
    system.read_orders()
    system.Inventory.values
    system.Customers
    system.Admins
    system.Orders
    print("=== Welcome to Online Shopping System ===")

    
    while True:
        print("\n1. Login\n2. Signup\n3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "3":
            break

        username = input("Username: ").strip()
        password = input("Password: ").strip()

        user = next((u for u in system.Customers + system.Admins
                     if u.get_Username() == username and u.get_Password() == password), None)

        if choice == "2":  # Signup
            role = input("Role (Customer/Admin): ").strip()
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            gender = input("Gender: ").strip()

            if role.lower() == "customer":
                country = input("Country: ").strip()
                city = input("City: ").strip()
                cart = Cart(name)
                new_user = Customer(name, phone, email, gender, "Customer", username, password, country, city, cart)
                system.Customers.append(new_user)
                print("Customer account created successfully!")
            elif role.lower() == "admin":
                nationalid = input("National ID: ").strip()
                age = int(input("Age: ").strip())
                new_user = Admin(name, phone, email, gender, "Admin", username, password, nationalid, age)
                system.Admins.append(new_user)
                print("Admin account created successfully!")
            else:
                print("Invalid role! Try again.")
                continue
            user = new_user

        if not user:
            print("Invalid username/password. Try again.")
            continue

        
        if user.get_Role().lower() == "customer":
            while True:
                print(f"\n=== Customer Menu ({user.get_Name()}) ===")
                print("1. View Products\n2. Add to Cart\n3. Remove from Cart\n4. View Cart\n5. Place Order\n6. Logout")
                c_choice = input("Choose an option: ").strip()

                if c_choice == "6":
                    break
                elif c_choice == "1":
                    print("\nAvailable Products:")
                    for p in system.Inventory.values():
                        print(f"{p.get_Name()} | Category: {p.get_Category()} | Price: {p.get_Price()} EGP | Stock: {p.get_Stock()}")
                elif c_choice == "2":
                    prod_name = input("Enter product name: ").strip()
                    qty = int(input("Enter quantity: "))
                    if prod_name in system.Inventory:
                        product = system.Inventory[prod_name]
                        if qty <= product.get_Stock():
                            cart_item = CartItem(prod_name, qty,system.Inventory)
                            user.get_Cart().add_Item(cart_item)
                            print(f"{qty} x {prod_name} added to cart.")
                        else:
                            print("Not enough stock.")
                    else:
                        print("Product not found.")
                elif c_choice == "3":
                    prod_name = input("Enter product name to remove: ").strip()
                    user.get_Cart().remove_Item(prod_name)
                    print(f"{prod_name} removed from cart if it existed.")
                elif c_choice == "4":
                    user.get_Cart().display_Cart()
                elif c_choice == "5":
                    if not user.get_Cart().get_Items():
                        print("Your cart is empty!")
                    else:
                        order = Order(user)
                        order.confirm_order(system.Orders)
                        print("Order placed successfully!")
                        user.get_Cart().empty_Cart()
                else:
                    print("Invalid option!")

        
        elif user.get_Role().lower() == "admin":
            while True:
                print(f"\n=== Admin Menu ({user.get_Name()}) ===")
                print("1. View Inventory\n2. Add Product\n3. Update Product\n4. Remove Product")
                print("5. View Orders\n6. Update Order Status\n7. View Customers\n8. Generate Reports\n9. Logout")
                a_choice = input("Choose an option: ").strip()

                if a_choice == "9":
                    break
                elif a_choice == "1":
                    print("\nInventory:")
                    for p in system.Inventory.values():
                        print(f"{p.get_Name()} | Category: {p.get_Category()} | Price: {p.get_Price()} EGP | Stock: {p.get_Stock()}")
                elif a_choice == "2":
                    name = input("Product Name: ").strip()
                    category = input("Category: ").strip()
                    price = float(input("Price: "))
                    stock = int(input("Stock: "))
                    user.add_product(name, category, price, stock, system.Inventory)
                elif a_choice == "3":
                    name = input("Product Name to update: ").strip()
                    price = input("New Price (or leave blank): ").strip()
                    stock = input("New Stock (or leave blank): ").strip()
                    price = float(price) if price else None
                    stock = int(stock) if stock else None
                    user.update_product(name, price, stock, system.Inventory)
                elif a_choice == "4":
                    name = input("Product Name to remove: ").strip()
                    user.remove_product(name, system.Inventory)
                elif a_choice == "5":
                    user.view_all_orders(system.Orders)
                elif a_choice == "6":
                    cust_name = input("Customer Name for Order: ").strip()
                    order = next((o for o in system.Orders if o.get_CustomerName() == cust_name), None)
                    if order:
                        status = input("New Status: ").strip()
                        user.update_order_status(order, status)
                    else:
                        print("Order not found.")
                elif a_choice == "7":
                    user.view_all_customers(system.Customers)
                elif a_choice == "8":
                    print("\n=== Customer Report ===")
                    user.generate_customer_report(system.Customers, system.Orders)
                    print("\n=== Sales per Day ===")
                    user.sales_per_day(system.Orders)
                else:
                    print("Invalid option!")

    
    system.save_inventory()
    system.save_customers()
    system.save_admins()
    system.save_orders()
    print("\nSystem data saved. Goodbye!")

if __name__ == "__main__":
    main()
