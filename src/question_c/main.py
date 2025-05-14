#add import

from question_c.question_c import create_multiplication_table, display_multiplication_table

def main():
   
    while True:
        table = create_multiplication_table()
        print("Multiplication Table:")
        display_multiplication_table(table)

        choice = input("Do you want to run again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()