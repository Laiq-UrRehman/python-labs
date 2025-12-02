def print_pascal(rows):
    for i in range(rows):
        
        val = 1
        
        for j in range(i + 1):
            print(val, end=" ")
            
            val = val * (i - j) // (j + 1)
            
        print()

r = int(input("Enter how many rows: "))

print_pascal(r)
