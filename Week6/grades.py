list = []
with open("my_newfile", "r") as fileObject:
    # Read a line form the file
        line = fileObject.readline()
        # If the line is empty break the while loop
        if line == "":
            break
        else:
            list.append(line)
print(list)