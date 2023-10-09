def element_math(my_nums):
    results=[]
    for i in range(len(my_nums)):
        sum=0
        for element in my_nums:
            sum+=element[i]
        results.append(sum)
    return (results[0],results[1],results[2],results[3])
print(element_math(my_nums = ((5, 10, 15, 20),  (2, 4, 6, 8), (57, 68, 79, 81), (1, 3, 5, 7))))