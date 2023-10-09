def sorting_list(list_user):
    results=[]
    results.append([list_user[0]])
    for object in list_user:
        new_object=True
        for i in range(len(results)):
            if object == results[i][0]:
                results[i].append(object)
                new_object=False
        if new_object:  
            results.append([object])        
    return results
print(sorting_list([1, 2, 1, 3, 'a', 'b', "a", 'c']))
