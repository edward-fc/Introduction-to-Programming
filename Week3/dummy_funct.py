def dummy_function(user):
    try:
        for i in range(len(user)):
            user[i]
        return print("This is a list")
    except:
        return print("this is a dictionnairy")
dummy_function({"edward":1,"carter":2})