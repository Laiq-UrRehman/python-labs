def print_pascal(rows):
    previous_row = [1]

    for i in range(rows):
        print(previous_row)
        
        new_row = []
        new_row.append(1)
        
        for j in range(len(previous_row) - 1):
            sum_val = previous_row[j] + previous_row[j+1]
            new_row.append(sum_val)
            
        new_row.append(1)
        
        previous_row = new_row

num_rows = int(input("Enter how many rows: "))
print_pascal(num_rows)