def alchool():
    age=int(input("the customers age"))
    legal_age=int(input("the legal age to purchase alcohol"))
    paid_by_card=input("if the customer is paying by card: True or false")
    age_on_id=int(input("the age on the customers ID"))
    estimated_age=int(input("how old the customer looks"))
    if estimated_age >= 21:
        return True
    if age == age_on_id:
        if age >= legal_age:
            return True
    if paid_by_card:
        return True
    return False
print(alchool())