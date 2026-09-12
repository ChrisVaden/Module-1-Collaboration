# Name: Christopher A Vaden Jr
# Name of the App: GPA.py
# Description: This code wants the ser to input their last name, first name, and Gpa. If they enter their last name but its 'ZZZ', then the code will stop and print 'Record not Found. Else print the name.
# If gpa is above or equal to 3.5 then Dean's lift. If 3.25 or above then honor roll 


lastname = input("What is Your Last Name? ")
firstname = input("What is your First name? ")
gpa = float(input("What is your GPA? "))

if lastname == "ZZZ":
    print("Record not Found")
else:
    print(lastname)
    print(firstname)

if gpa >= 3.5:
    print("You have made the Dean's list")
elif gpa >= 3.25:
    print("You have made the Honor Roll")