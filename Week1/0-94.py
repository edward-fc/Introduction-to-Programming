def find0_94():
    number=input("Choose a number")
    print(number)
    for i in range(95):
        if i == int(number):
            return "Correct"
    return "incorrect"
print(find0_94())