#conditionals
collins_is_programmer = True
first_number = input("First number: \n")
second_number = input("Second number: \n")

if(first_number > second_number):
    print(f"{first_number} is greater than {second_number}")
elif(first_number < second_number):
    print(f"{first_number} is less than {second_number}")
else:
    print("They are both equal")

if(collins_is_programmer):
    print("Collins is a wonderful programmer")
else:
    print("Collins is not a wonderful programmer. Not at all")