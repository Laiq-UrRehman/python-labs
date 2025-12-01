def get_biggest(a, b, c, d):
    biggest = a
    
    if b > biggest:
        biggest = b
    if c > biggest:
        biggest = c
    if d > biggest:
        biggest = d
        
    return biggest

# Get 4 numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))

print("The largest number is:", get_biggest(n1, n2, n3, n4))