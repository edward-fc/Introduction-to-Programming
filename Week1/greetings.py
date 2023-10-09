def greetings():
    name=input("what is your First and last name?")
    list_first_last=name.split(" ",1)
    capital_first=list_first_last[0][0]
    capital_last=list_first_last[1][0] 
    capital_first=capital_first.capitalize()
    capital_last=capital_last.capitalize()
    list_first_last[0]=list_first_last[0].replace(list_first_last[0][0],capital_first,1)
    list_first_last[1]=list_first_last[1].replace(list_first_last[1][0],capital_last,1)
    return print("Nice to meet u Mr{last} or {first} {last}".format(last=list_first_last[1],first=list_first_last[0]))
greetings()
