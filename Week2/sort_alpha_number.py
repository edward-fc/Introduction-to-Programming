def sort_alpha_numbers():
    user_str=input("enter str")
    number=[]
    str=[]
    for simple_str in user_str:
        try:
            if int(simple_str):
                number.append(simple_str)
        except:
            str.append(simple_str)
    return [number,str]
print(sort_alpha_numbers())
