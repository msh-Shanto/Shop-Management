import os

def get_terminal_width():
    try:
        columns, _ = os.get_terminal_size()
        return columns
    except:
        return 80

def print_error(message):
    print("\x1b[31m" + message + "\x1b[0m")

def save_invoice_to_file(invoice_file, invoice_content):
    with open(invoice_file, 'w') as file:
        file.write(invoice_content)

total = 0
terminal_width = get_terminal_width()
center_width = 40

header = "Golden Bakery".center(center_width)
print(header)
print("-" * center_width)
print("\n")

item_prices = {
    "Bread": 20,
    "Butter": 50,
    "Jelly": 60,
    "Sauce": 70,
    "Toast": 120
}

purchase_details = {}

while True:
    print("Choose an item to buy:\n".center(center_width))
    print("1. Bread    -  20 tk".center(center_width))
    print("2. Butter   -  50 tk".center(center_width))
    print("3. Jelly    -  60 tk".center(center_width))
    print("4. Sauce    -  70 tk".center(center_width))
    print("5. Toast    -  120 tk".center(center_width))
    print("6. Checkout      ".center(center_width))
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        bread_qty = int(input("How many Bread you want to buy? "))
        bread_total = item_prices["Bread"] * bread_qty
        print("Bread added to the cart\n")
        total += bread_total
        purchase_details["Bread"] = bread_qty
        
    elif choice == "2":
        butter_qty = int(input("How many Butter you want to buy? "))
        butter_total = item_prices["Butter"] * butter_qty
        print("Butter added to the cart\n")
        total += butter_total
        purchase_details["Butter"] = butter_qty
        
    elif choice == "3":
        jelly_qty = int(input("How many Jelly you want to buy? "))
        jelly_total = item_prices["Jelly"] * jelly_qty
        print("Jelly added to the cart\n")
        total += jelly_total
        purchase_details["Jelly"] = jelly_qty
        
    elif choice == "4":
        sauce_qty = int(input("How many Sauce you want to buy? "))
        sauce_total = item_prices["Sauce"] * sauce_qty
        print("Sauce added to the cart\n")
        total += sauce_total
        purchase_details["Sauce"] = sauce_qty
        
    elif choice == "5":
        toast_qty = int(input("How many Toast you want to buy? "))
        print("Toast added to the cart\n")
        toast_total = item_prices["Toast"] * toast_qty
        total += toast_total
        purchase_details["Toast"] = toast_qty
    
    elif choice == "6":
        print("You have to pay ", total, " taka" )
        
        invoice_content = "-------- Invoice --------\n"
        for item, qty in purchase_details.items():
            price = item_prices[item] * qty
            invoice_content += f"{item} x {qty} - {price} taka\n"
        invoice_content += "--------------------------\n"
        invoice_content += f"Total: {total} taka\n"
        
        save_invoice_to_file("invoice.txt", invoice_content)
        exit(0)
              
    else:
        print_error("Sorry, wrong input!\n")
  