#add import

from question_a.question_a import get_stock_list, Stock

def main():
    stock_list = get_stock_list()

    while True:
        print("Stock Report Menu")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Stock Report")
            print("Company\t\tSymbol")
            
            for stock in stock_list:
                print(f"{stock.get_company_name()}\t{stock.get_symbol()}")
        
        elif choice == "2":
            print("Exiting program.")
            break
        
        else:
            print("Invalid option. Please enter 1 or 2.")
