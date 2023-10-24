# -*- coding: utf-8 -*-

def check_upper_lower(x):
    """
    Counts the number of upper case letters and lower case letter
    in string x and returns the numbers as a list [upper, lower].
    If x is not a string, returns 'ValueError, string expected!'.
    """
    upper=0
    lower=0
    for string in x:
        if ord(string) < 91 and ord(string) > 64 :
            upper+=1
        else:
            if ord(string) < 123 and ord(string) > 96 :
                lower+=1
            else:
                return print("Error_input")
    return [upper,lower]
print(check_upper_lower("JFHLKJDSGH hljsfd"))

