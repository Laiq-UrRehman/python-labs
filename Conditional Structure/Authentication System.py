email = input("Enter email: ")
password = input("Enter password: ")

correct_email = "abc@gmail.com"
correct_pass = "abc"

if email == correct_email and password == correct_pass:
    print("User is logged in")
elif email == correct_email and password != correct_pass:
    print("Password is not correct")
elif password == correct_pass and email != correct_email:
    print("Enter the correct email")
else:
    print("Wrong email and password")