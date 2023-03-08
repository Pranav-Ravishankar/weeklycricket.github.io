total_people = int(input("Enter total number of people: "))
total_hours = float(input("Enter total number of hours: "))
number_of_students = int(input("Enter number of Students: "))
students_pay = 0
total_cost = total_hours * 2250

if total_hours == 1.5:
    students_pay = 200
else:
    students_pay = 220

number_of_uncles = total_people - number_of_students
uncles_amount = total_cost - (number_of_students * students_pay)
uncles_pay = uncles_amount/number_of_uncles

print("Uncles should pay " + str(uncles_pay))