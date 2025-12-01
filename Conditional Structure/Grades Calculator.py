ict = int(input("Enter ICT marks: "))
pf = int(input("Enter PF marks: "))
sociology = int(input("Enter Sociology marks: "))
english = int(input("Enter English marks: "))
civics = int(input("Enter Civics marks: "))

total = ict + pf + sociology + english + civics
percentage = (total / 500) * 100

print("Percentage:", percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")