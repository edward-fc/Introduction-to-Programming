def sorting_system(list):
    sum4=[]
    mean=[]
    rounded_integer=[]
    counter=0
    for lists in list:
        counter+=1
        for i in range(len(lists)):
            sum4_2=0
            sum4_2=lists[i]+lists[i-1]+lists[i+1]
            if counter !=1:
                sum4_2+=list[counter-1][i]
            if counter != len(list):
                sum4_2+=list[counter+1][i]
            sum4.append(sum4_2)
    print(sum4)
sorting_system([[0, 1, 2, 3, 4],[5, 6, 7, 8, 9],[10, 11, 12, 13, 14],[15, 16, 17, 18, 19],[20, 21, 22, 23, 24]])      

