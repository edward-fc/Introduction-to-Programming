def FloatorInt():
    User = input("enter an Float or Int")
    try:
        transformed = int(User)
        if str(transformed) == User:
            return print("this input was an Int")
    except:
        return print("this input was an float")
FloatorInt()
