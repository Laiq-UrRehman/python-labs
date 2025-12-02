def find_largest(n1, n2, n3, n4):
    winner = n1
    
    if n2 > winner:
        winner = n2
        
    if n3 > winner:
        winner = n3
        
    if n4 > winner:
        winner = n4
        
    return winner

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

print("Largest number is:", find_largest(a, b, c, d))
