"""
Please write your name
@author:

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Diabetes:
    def __init__(self, filepath) -> None:
        self.data = []
        count = 0
        error = False
        try:
            for line in open(filepath, 'r'):
                if count == 0:
                    self.header = line.split(",")
                    count = 1
                else:
                    slip1 = line.split(",")
                    self.data.append(slip1)
            
        except:
            error = True
        assert not error, "Error input filename"
        

    def get_dimension(self) -> list:
        print(self.data)
        return len(self.data[0])

    def web_summary(self, filepath: str) -> None:
        with open(filepath,"w") as html:
            # write the boilerplate html stuff
            html.write("<html>\n")
            html.write("<head>\n")
            html.write("<meta charset=\"UTF-8\">\n")
            html.write("<style>\n")
            html.write("table, th, td {\n")
            html.write("border: 1px solid black;\n")
            html.write("border-collapse: collapse;\n")
            html.write("}\n")
            html.write("</style>\n")
            html.write("<title>Student grades</title>\n")
            html.write("</head>\n")
            html.write("<body>\n")
            html.write("<h2>Test scores</h2>\n")
            html.write("<table>\n")

            
            # format the table header 
            html.write("<tr>\n")
            html.write("<th rowspan=\"3\">Attributes</th>\n")
            html.write("<th colspan=\"4\">Class</th>\n")
            html.write("</tr>\n")
            html.write("<tr>\n")
            html.write("<th colspan=\"2\">Positive</th>\n")
            html.write("<th colspan=\"2\">Negative</th>\n")
            html.write("</tr>\n")
            html.write("<tr>\n")
            html.write("<td>Yes</td>\n")
            html.write("<td>No</td>\n")
            html.write("<td>Yes</td>\n")
            html.write("<td>No</td>\n")
            html.write("</tr>\n")

            

            

            # iterate over the lines in the file printing out formatted html
            list_things = []
            for y in range(2):
                list_things.append([])
                for i in range(2):
                    list_things[y].append([])
                    for z in range(len(self.data[0])-3):
                        zero = 0
                        list_things[y][i].append(zero)

            index_pos = 0
            
            for row in self.data:
                if row[-1] != "Positive\n":
                    index_pos = 1
                else:
                    index_pos = 0
                
                for i,elem in enumerate(row):
                    i-=2
                    if elem == "Yes":
                        list_things[index_pos][0][i]+=1
                    elif elem == "No":
                        list_things[index_pos][1][i]+=1
                    
                
            for i,element in enumerate(self.header):
                i-=2
                if element != self.header[0] and element != self.header[1] and element != self.header[-1]:
                    print(list_things)
                    html.write("<tr>\n")
                    html.write("<td>"+ element + "</td>\n")
                    html.write("<td>"+ str(list_things[0][0][i]) + "</td>\n")
                    html.write("<td>"+ str(list_things[0][1][i])+ "</td>\n")
                    html.write("<td>"+ str(list_things[1][0][i]) + "</td>\n")
                    html.write("<td>"+ str(list_things[1][1][i]) + "</td>\n")
                    html.write("</tr>\n")

            # close all the opened html tags
            html.write("</table>\n")
            html.write("</body>\n")
            html.write("</html>\n")

    def count_instances(self, criteria) -> int:
        # delete pass and this line to write your code
        # you can change the parameter criteria or the number of parameters
        # as you want, provided they are explained in doctring for this
        # method
        pass


if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    # d1.count_instances() # change according to your criteria
    print()

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    # d2.count_instances()  # change according to your criteria
