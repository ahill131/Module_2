#Alex Hill
#AlexHill_M02_Lab.py
#This app accepts a last and first name and a grade point average and prints a message indicating honors for that individual
#Process repeats until sentinel value is entered

last_name = ""
first_name = ""
GPA = 0

while True:
    last_name = input("Enter last name or ZZZ to quit: ")
    if last_name == "ZZZ":
        break
    first_name = input("Enter first name: ")
    GPA = float(input("Enter grade point average: "))
    if GPA >= 3.5:
        print(first_name,last_name,"has made the Dean's List!")
    elif GPA>= 3.25:
        print(first_name,last_name,"has made the Honor Roll.")
    else:
        print(first_name,last_name,"has not earned any honors.")

