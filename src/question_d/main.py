#add import

from question_d import stock_purchase_history, Stock

def main():
   
    while True:
        print("--- Stock Report Menu ---")
        print("1. Display stock purchase history")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            stock_purchase_history()
        
        elif choice == "2":
            print("Exiting program.")
            break
        
        else:
            print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()