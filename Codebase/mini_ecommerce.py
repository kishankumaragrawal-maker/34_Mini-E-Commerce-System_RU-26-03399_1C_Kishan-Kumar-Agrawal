# Mini E-Commerce System (PS 34)
# Admin can add, update, delete and view products.
# Customer can add products to a cart and checkout.
# Products are saved in products.txt, one product per line: ID,name,price,stock

FILE_NAME = "products.txt"

# each product is a dictionary, all products are stored in this list
products = []

# the cart is a dictionary: product ID -> quantity
cart = {}


def show_number(num):
    # prints 50000.0 as 50000, so the output looks clean
    if num == int(num):
        return int(num)
    return num


def find_product(pid):
    # look for a product with this ID, return None if it is not there
    for p in products:
        if p["id"].upper() == pid.upper():
            return p
    return None


def make_new_id():
    # the first product is P101, after that we take the biggest number and add 1
    if len(products) == 0:
        return "P101"
    biggest = 100
    for p in products:
        number = int(p["id"][1:])      # "P101" -> 101
        if number > biggest:
            biggest = number
    return "P" + str(biggest + 1)


# ---------- file handling ----------

def load_products():
    # read products.txt when the program starts
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            product = {"id": parts[0], "name": parts[1],
                       "price": float(parts[2]), "stock": int(parts[3])}
            products.append(product)
        file.close()
    except FileNotFoundError:
        pass    # first run, the file does not exist yet


def save_products():
    # write all products to the file (called after every change)
    file = open(FILE_NAME, "w")
    for p in products:
        file.write(p["id"] + "," + p["name"] + "," + str(p["price"]) + "," + str(p["stock"]) + "\n")
    file.close()


# ---------- CRUD ----------

def add_product():
    name = input("Product name: ").strip()
    if name == "":
        print("Invalid name. Name cannot be empty.")
        return

    try:
        price = float(input("Price: "))
    except ValueError:
        print("Invalid price. Price must be a positive number.")
        return
    if price <= 0:
        print("Invalid price. Price must be a positive number.")
        return

    try:
        stock = int(input("Stock: "))
    except ValueError:
        print("Invalid stock. Stock must be 0 or more.")
        return
    if stock < 0:
        print("Invalid stock. Stock must be 0 or more.")
        return

    product = {"id": make_new_id(), "name": name, "price": price, "stock": stock}
    products.append(product)
    save_products()

    print("Product added.")
    print("ID: " + product["id"] + " | " + name + " | Price: " + str(show_number(price)) + " | Stock: " + str(stock))
    if stock == 0:
        print("Warning: " + name + " is out of stock.")


def view_products():
    if len(products) == 0:
        print("No products available.")
        return
    for p in products:
        print("ID: " + p["id"] + " | " + p["name"] + " | Price: " + str(show_number(p["price"])) + " | Stock: " + str(p["stock"]))


def update_product():
    pid = input("Product ID to update: ").strip()
    p = find_product(pid)
    if p is None:
        print("Product " + pid + " not found.")
        return

    try:
        price = float(input("New price: "))
    except ValueError:
        print("Invalid price. Price must be a positive number.")
        return
    if price <= 0:
        print("Invalid price. Price must be a positive number.")
        return

    try:
        stock = int(input("New stock: "))
    except ValueError:
        print("Invalid stock. Stock must be 0 or more.")
        return
    if stock < 0:
        print("Invalid stock. Stock must be 0 or more.")
        return

    p["price"] = price
    p["stock"] = stock
    save_products()
    print("Product " + p["id"] + " updated.")


def delete_product():
    pid = input("Product ID to delete: ").strip()
    p = find_product(pid)
    if p is None:
        print("Product " + pid + " not found.")
        return

    products.remove(p)
    if p["id"] in cart:      # also remove it from the cart if it was there
        del cart[p["id"]]
    save_products()
    print("Product '" + p["name"] + "' deleted. Products left: " + str(len(products)))


# ---------- cart and checkout ----------

def add_to_cart():
    pid = input("Product ID: ").strip()
    p = find_product(pid)
    if p is None:
        print("Product " + pid + " not found.")
        return

    try:
        qty = int(input("Quantity: "))
    except ValueError:
        print("Invalid quantity. Quantity must be a positive whole number.")
        return
    if qty <= 0:
        print("Invalid quantity. Quantity must be a positive whole number.")
        return

    # how many of this product are already in the cart
    already = 0
    if p["id"] in cart:
        already = cart[p["id"]]

    # do not allow more than the stock
    if already + qty > p["stock"]:
        print("Not enough stock. Only " + str(p["stock"]) + " available.")
        return

    cart[p["id"]] = already + qty
    print(p["name"] + " x" + str(qty) + " added | Amount: " + str(show_number(p["price"] * qty)))


def view_cart():
    if len(cart) == 0:
        print("Cart is empty.")
        return
    total = 0
    for pid in cart:
        p = find_product(pid)
        qty = cart[pid]
        amount = p["price"] * qty
        total = total + amount
        print(p["name"] + " x" + str(qty) + " | Amount: " + str(show_number(amount)))
    print("Cart total: " + str(show_number(total)))


def checkout():
    if len(cart) == 0:
        print("Cart is empty.")
        return

    total = 0
    messages = []
    for pid in cart:
        p = find_product(pid)
        qty = cart[pid]
        total = total + p["price"] * qty
        p["stock"] = p["stock"] - qty      # reduce the stock
        messages.append(p["name"] + " stock left: " + str(p["stock"]))

    cart.clear()
    save_products()
    print("Order total: " + str(show_number(total)) + " | " + " | ".join(messages))


# ---------- main menu ----------

def main():
    load_products()
    while True:
        print("\n=== Mini E-Commerce System ===")
        print("1. Add product      2. Update product   3. Delete product")
        print("4. View products    5. Add to cart      6. View cart")
        print("7. Checkout         0. Exit")
        choice = input("Choose option: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            view_products()
        elif choice == "5":
            add_to_cart()
        elif choice == "6":
            view_cart()
        elif choice == "7":
            checkout()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


main()
