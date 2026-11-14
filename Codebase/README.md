# Mini E-Commerce System (PS 34)

A console shopping application written in Python 3. An admin can add, update, delete and view products. A customer can add products to a cart and check out. All products are saved in a file, so the data is still there the next time the program runs.

**Name:** [Your Full Name]
**ERP:** [Your ERP Number]
**Section:** [Your Section]

## Concepts used
- Lists and dictionaries (products are a list of dictionaries, the cart is a dictionary)
- Functions
- CRUD operations (Create, Read, Update, Delete)
- File handling (reading and writing `products.txt`)
- Input validation with `try/except`

## How to run
1. Install Python 3.
2. Open a terminal in the `Codebase` folder.
3. Run:
   ```
   python mini_ecommerce.py
   ```
4. Choose an option from the menu.

## Menu
| Option | Action |
|---|---|
| 1 | Add product |
| 2 | Update product |
| 3 | Delete product |
| 4 | View products |
| 5 | Add to cart |
| 6 | View cart |
| 7 | Checkout |
| 0 | Exit |

## How the data is stored
Products are saved in `products.txt`, one product per line:

```
ID,name,price,stock
P101,Laptop,50000.0,5
```

The file is created automatically the first time a product is added. The first product ID is `P101`. The program loads the file at the start and saves it after every change.

## Rules followed
- Price must be a positive number.
- Stock cannot be negative. A product with stock 0 shows a warning.
- A customer cannot order more than the available stock.
- Checkout reduces the stock of every product in the cart.

## Test cases
| Test case | Input | Expected output |
|---|---|---|
| 1. Normal input | Add product: Laptop, price 50000, stock 5 | `Product added.` then `ID: P101 \| Laptop \| Price: 50000 \| Stock: 5` |
| 2. Boundary input | Add product: Pen, price 1, stock 0 | `Product added.`, `ID: P101 \| Pen \| Price: 1 \| Stock: 0`, `Warning: Pen is out of stock.` |
| 3a. Invalid price | Add product: Mouse, price -500 | `Invalid price. Price must be a positive number.` |
| 3b. Unknown product | Add to cart: P999 | `Product P999 not found.` |
| 4a. Add to cart | P101 (Laptop, 50000, stock 5), quantity 2 | `Laptop x2 added \| Amount: 100000` |
| 4b. Checkout | Checkout | `Order total: 100000 \| Laptop stock left: 3` |
| 4c. Delete | Delete P101 | `Product 'Laptop' deleted. Products left: 0` |

Screenshots of these runs are in the `Testcases` folder.
