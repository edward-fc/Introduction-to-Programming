def voyel():
    sentance=input("enter a sentance:")
    sentance=sentance.lower()
    return sentance.count("a")+sentance.count("e")+sentance.count("i")+sentance.count("o")+sentance.count("u")
print(voyel())