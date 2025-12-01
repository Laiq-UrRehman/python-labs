def get_area(val1, val2, shape="rectangle"):
    
    if shape == "square":
        return val1 * val1
        
    elif shape == "circle":
        return 3.14 * val1 * val1
        
    elif shape == "triangle":
        return 0.5 * val1 * val2
        
    elif shape == "rectangle":
        return val1 * val2

print("Types: square, circle, triangle, rectangle")
type_input = input("Enter shape type: ")
v1 = float(input("Enter first number (side/radius/length): "))
v2 = float(input("Enter second number (width/height): "))

print("Area:", get_area(v1, v2, type_input))