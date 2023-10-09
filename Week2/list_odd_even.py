def list_odd_even():
    odd=[]
    even=[]
    for i in range(1,52):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd