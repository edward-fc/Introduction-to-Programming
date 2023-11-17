
class luxirous_good():
    def __init__(self, Item, sold_date,Price):
        self.item = Item
        self.date = sold_date
        self.price = Price

    def Item_details(self):
        print("Item: {}".format(self.item))
        print("Purchase date: {}".format(self.date))
        print("Price: {}".format(self.price))


class RichClient (luxirous_good):
    # if Shopping_list is  None, create an empty list
    def __init__(self, id, name, email, shopping_list=None):
        super().__init__(id, name, email)
        if shopping_list is None:
            self.shopping_list = []
        else:
            self.shopping_list = shopping_list

    # method to add new luxirous_good to the list
    def add_student(self, luxirous_good):
        if luxirous_good not in self.shopping_list:
            self.shopping_list.append(luxirous_good)

    # method to remove a student from the list
    def remove_student(self, luxirous_good):
        if luxirous_good in self.shopping_list:
            self.shopping_list.remove(luxirous_good)

    # method to print all students in the list
    def print_students(self):
        for luxirous_goods in self.shopping_list:
            print(luxirous_goods.item)