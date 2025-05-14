#write functions here, don't add input('') statements here!

def create_multiplication_table():
    table = []
   
    for row in range(1, 6):  # Rows: 1 to 5
        current_row = []
        
        for col in range(1, 11):  # Columns: 1 to 10
            current_row.append(row * col)
        table.append(current_row)
   
    return table


def display_multiplication_table(table):
    
    for row in table:
        
        for value in row:
            print(f"{value:<3}", end=" ")  # Format spacing
        print()