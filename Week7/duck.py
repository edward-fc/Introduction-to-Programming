class ducky():
    def __init__(self):
        self.sum = 0
    def sum_iter_value(iter):
        if type(iter) == list:
            for element in list:
                if type(element) == int:
                    sum += element
                elif type(element) == str:
                    try:
                        element = int(element)
                        sum+= element
                    except:
                        pass
        if type(iter) == str:
            