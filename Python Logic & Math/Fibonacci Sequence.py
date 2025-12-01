def show_fibonacci(limit):
    a = 0
    b = 1
    
    while a <= limit:
        print(a)
        
        next_val = a + b
        
        a = b
        b = next_val

user_limit = int(input("Enter the limit number: "))
show_fibonacci(user_limit)