# Project: Inventory Management System with Git  
#  
# Description:  
# This project is an Inventory Management System. The main code has been developed by the code creator,  
# while database preparation was assisted by two contributors.  
#  
# Team Members:  
# 1. Code developed by:  
#    - Name: Sarbo Sarcar (Roll No: 002311001011)  
#  
# 2. Database Contributors:  
#    - Name: Anuska Nath (Roll No: 002311001003)  
#    - Name: Soham Das (Roll No: 002311001004)  


import sqlite3

def create_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    conn.execute("""CREATE TABLE INVENTORY(
                    ID int,
                    PRODUCT_NAME varchar(100),
                    UNIT_PRICE int,
                    QUANTITY int
                    );""")
    conn.execute("""CREATE TABLE TRANSACTIONS(
                    TRANSACTION_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    CUSTOMER_NAME varchar(100),
                    PRODUCT_ID int,
                    PRODUCT_NAME varchar(100),
                    QUANTITY int,
                    TOTAL_COST float,
                    DATE timestamp DEFAULT CURRENT_TIMESTAMP
                    );""")
    conn.commit()
    conn.close()

def add_row(item, price, quantity, id_):
    try:
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM INVENTORY WHERE ID = ?""", (id_,))
        res = cursor.fetchall()
        if res:
            update_entry(id_, item, price, quantity)
            return
        print("Inserting item: ({}) {}, Price: {:.2f}, Quantity: {}".format(id_, item, price, quantity))
        cursor.execute("""INSERT INTO INVENTORY (ID, PRODUCT_NAME, UNIT_PRICE, QUANTITY) 
                          VALUES (?, ?, ?, ?)""", (id_, item, price, quantity))
        conn.commit()
        print("Inserted successfully!")
    except sqlite3.Error as e:
        print("Error occurred: {}".format(e))
    finally:
        conn.close()

def make_purchase():
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity to purchase: "))
    customer_name = input("Enter customer name: ")
    
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM INVENTORY WHERE PRODUCT_NAME = ?""", (item,))
    result = cursor.fetchone()
    
    if result:
        id_, product_name, unit_price, stock_quantity = result
        if stock_quantity >= quantity:
            total_cost = unit_price * quantity
            print("Total cost for {} {} is: {:.2f}".format(quantity, product_name, total_cost))
            new_quantity = stock_quantity - quantity
            cursor.execute("""UPDATE INVENTORY SET QUANTITY = ? WHERE PRODUCT_NAME = ?""", (new_quantity, item))
            cursor.execute("""INSERT INTO TRANSACTIONS (CUSTOMER_NAME, PRODUCT_ID, PRODUCT_NAME, QUANTITY, TOTAL_COST) 
                              VALUES (?, ?, ?, ?, ?)""", (customer_name, id_, product_name, quantity, total_cost))
            conn.commit()  
            
            print("Purchase successful! Remaining stock of {} : {}".format(product_name, new_quantity))
        else:
            print("Not enough stock available. Only {} items in stock.".format(stock_quantity))
    else:
        print("Item not found in the inventory.")
    
    conn.close()

def disp_prods():
    print("Here is the list of all products in the store")
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM INVENTORY""")
    op = cursor.fetchall()
    print("="*44)
    print("|{:5}|{:15}|{:10}|{:9}|".format("ID", "Name", "Unit Cost", "Quantity"))
    print("="*44)
    for row in op:
        print("|{:5}|{:15}|{:10.2f}|{:9}|".format(row[0], row[1], row[2], row[3]))
    print("="*44)
    conn.commit()
    conn.close()

def update_entry(id_, name, price, quantity):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE INVENTORY SET PRODUCT_NAME = ?, UNIT_PRICE = ?, QUANTITY = ? WHERE ID = ?", (name, price, quantity, id_))
    conn.commit()
    conn.close()

valid_users = ["seller", "customer"]

def validate_user(user):
    if user not in valid_users:
        print("{} is invalid!\nUse one of {}".format(user, valid_users))

MENU = """
\t\tMENU\n
1. View existing products
2. Change role
3. Exit
"""

MENU_CUST = """
\t\tMENU\n
1. Make a purchase
2. View existing products
3. Change role
4. Exit
"""

MENU_SELLER = """
\t\tMENU\n
1. Update or Add a product
2. View existing products
3. View past transactions
4. Change role
5. Exit
"""

USER = ""

def display_intro():
    global USER
    message = """
Welcome to the Inventory Management System!

This system allows you to manage products in the inventory.
Please select your role (customer or seller) to proceed.

Customer: Make purchases and view products.
Seller: Add or update products in the inventory.

Enjoy using the application!
"""
    width = max(len(line) for line in message.split("\n")) + 4
    print("+" + "-" * (width - 2) + "+")
    for line in message.split("\n"):
        print("| " + line.ljust(width - 4) + " |")
    print("+" + "-" * (width - 2) + "+")
    
    USER = input("Enter the role of the user: ")

def view_transactions():
    print("Here are the transaction records")
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM TRANSACTIONS""")
    op = cursor.fetchall()
    print("="*92)
    print("|{:5}|{:15}|{:10}|{:15}|{:10}|{:9}|{:19}|".format("ID", "Customer", "Product ID", "Product Name", "Quantity", "Total Cost", "Date"))
    print("="*92)
    for row in op:
        print("|{:5}|{:15}|{:10}|{:15}|{:10}|{:10.2f}|{:19}|".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    print("="*92)
    conn.commit()
    conn.close()

def main():
    global USER, MENU
    while True:
        if USER == "customer":
            print(MENU_CUST) 
            choice = input("Enter a choice: ")
            if choice == '4':
                break
            elif choice == '1':
                if USER == "customer":
                    make_purchase()
                else:
                    print("Role {} is not allowed to make purchases. Select option 3 to change role instead")
            elif choice == '2':
                disp_prods()
            elif choice == '3':
                USER = input("Enter new role: ")
                validate_user(USER)
                continue
            else:
                print("Invalid choice!")
                continue
        elif USER == "seller":
            print(MENU_SELLER)
            choice = input("Enter a choice: ")
            if choice == '5':
                break
            elif choice == '2':
                if USER == "seller":
                    disp_prods()
            elif choice == '1':
                if USER == "seller":
                    print("Enter the details below to add/update a product")
                    id_ = int(input("Enter product ID: "))
                    item = input("Enter item name: ")
                    cost = float(input("Enter unit cost of {}: ".format(item)))
                    quantity = int(input("Enter total stock quantity of {}: ".format(item)))
                    add_row(item, cost, quantity, id_)
                    print("Added item successfully!")
                else:
                    print("Invalid role: {}. Select option 3 to change role".format(USER))
            elif choice == '3':
                view_transactions()                    
            elif choice == '4':
                USER = input("Enter new role: ")
                validate_user(USER)
                continue
            else:
                print("Invalid choice!")
                continue
        else:
            print("Current role {} is not one of {} or {}. Please change role to update your requirements by selecting option 2 from the menu below:".format(USER, valid_users[0], valid_users[1]))
            print(MENU)
            choice = input("Enter a choice: ")
            if choice=='1':
                disp_prods()
            elif choice=='2':
                USER = input("Enter new role: ")
                validate_user(USER)
            elif choice=='3':
                break
            else:
                print("Invalid choice!")
    print("Exiting...")

if __name__ == "__main__":
    #create_db()
    display_intro()
    main()
