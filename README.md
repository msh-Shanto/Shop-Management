# Shop-Management

Golden Bakery - Console Invoice Generator

This Python script is a simple command-line application that simulates a bakery's checkout system. It allows users to select items to purchase, calculates the total price, and generates an invoice.

Usage:
1. Make sure you have Python installed on your computer.
2. Save this script as 'bakery_checkout.py'.
3. Open your terminal or command prompt.
4. Navigate to the directory where 'bakery_checkout.py' is saved.
5. Run the script using the command: python bakery_checkout.py

Functionality:
- The script displays a menu of bakery items with their prices.
- Users can select items by entering the corresponding numbers.
- Users can specify the quantity of each selected item.
- The script calculates the total price of selected items.
- Users can choose to checkout, which generates an invoice file named 'invoice.txt'.

Note:
- The script assumes a terminal width of 40 columns but adapts if your terminal is wider.
- The 'invoice.txt' file will be saved in the same directory as the script.
- Invoice content includes a list of items purchased, quantities, individual prices, and the total amount.

Usage Example:
1. Choose an item to buy:
2. Butter   -  50 tk
3. Jelly    -  60 tk
4. Sauce    -  70 tk
5. Toast    -  120 tk
6. Checkout

Enter your choice: 2
How many Butter you want to buy? 2
Butter added to the cart

Enter your choice: 4
How many Sauce you want to buy? 1
Sauce added to the cart

Enter your choice: 6
You have to pay  190  taka

Invoice Content (invoice.txt):
-------- Invoice --------
Butter x 2 - 100 taka
Sauce x 1 - 70 taka
--------------------------
Total: 190 taka

Feel free to customize the item list, prices, and any other parts of the script to match your bakery's offerings or your specific needs.
