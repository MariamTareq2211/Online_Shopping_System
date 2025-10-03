# 🛒 E-Commerce Management System

This project is a Python-based console application for managing an e-commerce system.
It supports Admins, Customers, Products, Carts, and Orders, with data persistence using text files.

# 📂 Project Structure
E-Commerce-System/
│
├── Classes/
│   ├── User.py
│   ├── Customer.py
│   ├── Admin.py
│   ├── Product.py
│   ├── Cart.py
│   ├── CartItem.py
│   └── Order.py
│
├── Files/
│   ├── Inventory.txt   # Stores products
│   ├── Customers.txt   # Stores customer data
│   ├── Admins.txt      # Stores admin data
│   └── Orders.txt      # Stores order history
│
├── SystemFunctions.py   # Core read/write system logic
├── main.py              # Entry point of the application
└── README.md            # Project documentation

# ⚙️ Features
    👤 Customers

Register and update profile

Manage cart (add, remove, decrease, empty)

Place orders and view order history

Cancel pending orders

    👨‍💼 Admins

Manage products in the inventory (add, update, delete)

View customers and orders

Save system state to files

    📦 Products

Stored in Inventory.txt

Each line contains:

name,category,price,stock

    🛍️ Orders

Stored in Orders.txt

Each line contains:

customer_name|status|total_price|shipping_address|date

    💾 Persistence

Data is saved and loaded from the Files/ directory using the SystemFunctions class.

# ▶️ How to Run

Clone the repository or download the project folder.

Ensure you are using Python 3.8+.

Open a terminal in the project folder.

Run:

python main.py


Interact with the system via the console menu.

# 📑 Example Data
Inventory.txt
Laptop,Electronics,1500.0,10
Phone,Electronics,800.0,20
T-Shirt,Fashion,20.0,50

Customers.txt
Mariam,01012345678,mariam@mail.com,Female,Customer,mariam123,pass123,Egypt,Cairo
Mohamed,01098765432,mohamed@mail.com,Male,Customer,mohamed321,pass321,Egypt,Giza

Admins.txt
Admin1,01000000000,admin1@mail.com,Male,Admin,admin1,adminpass,1234567890,35

Orders.txt
Mariam|Processing|260.0|Egypt, Cairo|2025-10-04 00:00:40
Mohamed|Processing|250.0|Egypt, Giza|2025-10-03 00:00:40

# 🛠️ Future Improvements

Add product search and filtering

Implement discount codes and promotions

Add export to CSV/Excel reports

Build a GUI or web interface

# 👨‍💻 Author

Developed by Mariam Tarek Mohamed
📧 Contact: mariemtarek283@gmail.com