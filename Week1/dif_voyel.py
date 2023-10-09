def dif_voyel():
    sentance=input("enter a sentance")
    sentance=sentance.lower()
    results=0
    voyels=["a","e","i","o","u"]
    for voyel in voyels:
        if sentance.count(voyel)>0:
            results+=1
    return results
print(dif_voyel())