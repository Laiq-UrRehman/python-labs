def fibonacci(limit):
    first = 0
    second = 1
    
    while first <= limit:
        print(first)
        
        next_num = first + second
        
        first = second
        second = next_num

num = int(input("Enter the limit: "))

fibonacci(num)
