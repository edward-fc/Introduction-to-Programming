
class luxirous_good():
    def __init__(self, Item, sold_date,Price):
        self.item = Item
        self.date = sold_date
        self.price = Price

    def Item_details(self):
        print("Item: {}".format(self.item))
        print("Purchase date: {}".format(self.date))
        print("Price: {}".format(self.price))
coco = luxirous_good("coco_chanel","1/3/2000",50)
coco.Item_details()
gucci = luxirous_good("gucci handbag","11/3/2010",70)
gucci.Item_details()

class RichClient ():
    # if Shopping_list is  None, create an empty list
    def __init__(self,shopping_list=None):
        super().__init__()
        if shopping_list is None:
            self.shopping_list = []
        else:
            self.shopping_list = shopping_list

    # method to add new luxirous_good to the list
    def add_item(self, luxirous_good):
        if luxirous_good not in self.shopping_list:
            self.shopping_list.append(luxirous_good)

    # method to remove a student from the list
    def remove_item(self, luxirous_good):
        if luxirous_good in self.shopping_list:
            self.shopping_list.remove(luxirous_good)

    # method to print all students in the list
    def print_item(self):
        for luxirous_goods in self.shopping_list:
            print(luxirous_goods.item)
ME = RichClient()
ME.add_item(coco)
ME.add_item(gucci)
ME.print_item()
ME.remove_item(coco)
ME.print_item()