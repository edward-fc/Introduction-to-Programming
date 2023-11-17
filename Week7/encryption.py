def check_key(x):
    if type(x) == int:
        if x > 0 and x < 95:
            return True
        else:
            return False
    else:
        return False

def shift_cipher(x,key = 3,option=1):
    result=""
    if option >2:
        print("Error in option input")
    if not check_key():
        print("Error in key input")
    if option == 1:
        if type(x) == str:
            for letter in x:
                result += chr((ord(letter) + key ))
            return result
    elif option == 2:
        if type(x) == str:
            for letter in x:
                result += chr((ord(letter) - key ))
            return result

            
print(shift_cipher("#Khoor#Zruog#=,",option = 2))#Khoor#Zruog#=,