import itertools
lists = {}
class ShoppingList:
    id_iteration = itertools.count()
    def __init__(self):
        # List Name
        self.name = input('Enter the List Name:')
        self.id = next(self.id_iteration)
        lists[self.id] = self.name,
    def list_items(self):
        mylist = ["Milk", "Eggs", "Cereal","Yogurt"]
        print(mylist)

    def list_name(self):
        print('List Name:',self.name)
    def list_ID(self):
        print('Shopping List ID:',self.id)

if __name__ == "__main__":
    print('Main Page Loaded')
    list1 = ShoppingList()
    print('Default list loaded - Future Enactment Added Here')

    list1.list_name()

    print('Items in Your list')
    list1.list_items()
    print("User Clicks 'Save List' Button")
    print("Create a new list")
    #Through Development we found that we may want to include a reset button on next iteration
    list2 = ShoppingList()
    print('Items in Your list')
    list2.list_items()
    print("User Clicks 'Save List' Button")
    print("User Clicks 'Saved Shopping List' Button")

    #print (lists) #This displays dictionary info to be referenced later
    temp_list = lists[1]
    temp_list2 = lists[0]
    print('Saved Lists:')
    list1.list_ID(),print('List Name:',*temp_list)
    list2.list_ID(),print('List Name:',*temp_list2)


    print('Select a list to display on Main Page')