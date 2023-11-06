with open("my_newfile", "w") as fileObject:
    for i in range(1,101):
        fileObject.write("{}\n".format(i*i))