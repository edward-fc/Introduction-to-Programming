list = []
# Open a file using the with feature
with open("Week6/grades.txt", "r") as fileObject:
    while True:
        # Read a line form the file
        line = fileObject.readline()
        # If the line is empty break the while loop
        if line == "":
            break
        else:
            if line[:-2] == "\n":
                line = line[:-2]
            list.append(int(line))
print(list)
print(len(list))
#max grade
max=0
mini = 100
moyen = 0
for element in list:
    moyen+=element
    if element > max:
        max = element
    if element < mini:
        mini = element
print(max)
print(mini)
print(moyen/len(list))
list.sort()
median=0
if len(list)%2:
    median = (list[len(list)/2]+list[len(list)/2+1])/2
else:
    median = list[round(len(list)/2)]/2
print(median)