**Name:** Kishan Kumar Agrawal
**ERP:** RU-26-03399
**Section:** 1C

# Mini E-Commerce System

This is a console-based shopping application written in Python. The project uses basic Data Structures (Lists, Dictionaries) and File Handling to store product data.

## Features
- **Admin Panel:** Add, View, Update, and Delete products (CRUD operations).
- **Customer Cart:** Add products to the cart based on available stock.
- **Checkout:** Calculates the total amount and updates the remaining stock.
- **Data Storage:** All products are saved in `products.txt`, so data is not lost after closing the program.

## How to Run
1. Keep `mini_ecommerce.py` in your folder.
2. Open the terminal and run: `python mini_ecommerce.py`
3. The `products.txt` file will be created automatically when you add the first product.

## Key Logic / Concepts Used
- **List of Dictionaries:** All products are stored in a list. Each product is a dictionary (e.g., `{"id": "P101", "name": "Laptop", "price": 50000.0, "stock": 5}`).
- **Dictionary for Cart:** Used to map Product IDs to Quantities (e.g., `{"P101": 2}`) for fast lookup.
- **File Handling:** `load_products()` reads the text file at startup. `save_products()` updates the file after every change.
- **Exception Handling:** `try/except` blocks are used to prevent crashes when the user enters invalid data (like text instead of numbers).
