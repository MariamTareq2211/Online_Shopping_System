# 🛒 E-Commerce Management System

This project is a Python-based console application for managing an e-commerce system.
It supports Admins, Customers, Products, Carts, and Orders, with data persistence using text files.

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

# 🛠️ Future Improvements

    Add product search and filtering

    Implement discount codes and promotions

    Add export to CSV/Excel reports

    Build a GUI or web interface

# 👨‍💻 Author

    Developed by Mariam Tarek Mohamed
    📧 Contact: mariemtarek283@gmail.com