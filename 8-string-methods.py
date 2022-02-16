# string methods

name = "collins"
sir_name = "Oduor"
middle_name = "Derrick"
greeting = "Hello world!"

# print(name.capitalize(), name.casefold(), name.endswith("s"))
# print(sir_name.upper())

# check if a string is a palindrome
def check_palindrome(string):
    letters_in_middle_name = [letter.lower() for letter in string]
    letters_in_middle_name_reversed = [string[-count].lower() for count in range(1, len(letters_in_middle_name) + 1)]
    if(letters_in_middle_name == letters_in_middle_name_reversed):
        return(f"{string} is a palindrome")
    else:
        return(f"{string} is not a palindrome")


# print(check_palindrome(middle_name))
# print(check_palindrome("Bob"))

print(name.upper(), name.lower(), name.capitalize(), name.index("l"), name.endswith("s"))