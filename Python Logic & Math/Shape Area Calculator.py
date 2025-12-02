def get_area(v1, v2, shape="rectangle"):
    
    if shape == "square":
        return v1 * v1
        
    elif shape == "circle":
        return 3.14 * v1 * v1
        
    elif shape == "triangle":
        return 0.5 * v1 * v2
        
    elif shape == "rectangle":
        return v1 * v2

print("Shapes: square, circle, triangle, rectangle")
type_input = input("Enter shape: ")
val1 = float(input("Enter first value: "))
val2 = float(input("Enter second value (0 if not needed): "))

print("Area:", get_area(val1, val2, type_input))
