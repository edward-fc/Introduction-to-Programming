def sorted_list():
    list=[]
    for i in range(5):
        lists = []
        for y in range (5):
            lists.append(i*5+y)
        list.append(lists)
    return print(list)
sorted_list()