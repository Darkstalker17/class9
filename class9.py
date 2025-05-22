
'''
1. Exam Eligibility Check
Outline:
Write a program to check whether the student can take an exam or not.(Y for yes and N for no).
Students will be allowed only in two conditions: If they have a medical cause 
If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
'''
y_n = "Y"#input("Enter weather you have a medical cause(Y for yes and N for no): ")

if y_n == "Y":
    print("You are allowed to take the exam")
else:
    if y_n == "N":
        attendance = int(input("Enter your Attendance: "))
        if attendance >= 75:
            print("You are allowed to take the exam.")
        else:
            print("Not allowed")
          
'''
2. Electricity bill
Outline:
Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed.
Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25.
If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that
bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26,
and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.
'''
n = 90#int(input("Enter the number of units consumed: "))
if n < 50:
    per_unit = 2.60*n
    tax = 25
    tot = per_unit+tax
    print("As you consumed below 50 units, Your electricity bill is:",tot)
elif n < 100 and n >= 50:
    per_unit = 3.25*n
    tax = 35
    tot = per_unit+tax
    print("As you consumed above 50 units and below 100 units, Your electricity bill is:",tot)
elif n < 200 and n >= 100:
    per_unit = 5.26*n
    tax = 45
    tot = per_unit+tax
    print("As you consumed above 100 units and below 200 units, Your electricity bill is:",tot)
else:
    per_unit = 8.45*n
    tax = 75
    tot = per_unit+tax
    print("As you consumed above 200 units, Your electricity bill is:",tot)

'''
3. Customise your ride
Outline:
Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2.
Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.
'''
ride_pref = int(input("Enter the ride you prefer: 1. Bike and 2.Car: "))
if ride_pref == 1:
    ans = int(input("Enter whether you want to choose a 1. Kawatski or a 2. Bullet: "))
    if ans == 1:
        print("Cool choice!")
    elif ans == 2:
        print("Speedy choice!")
    else:
        print("Choose a proper option, please.")
elif ride_pref == 2:
    ans = int(input("Enter whether you want to choose a 1. Ferrari or a 2. Mercedes G_wagon: "))
    if ans == 2:
        print("Cool choice!")
    elif ans == 1:
        print("Speedy choice!")
    else:
        print("Choose a proper option, please.")
else:
    print("Choose a proper option, please.")

