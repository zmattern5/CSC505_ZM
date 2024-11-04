import itertools
class DeveloperTraits:
    def __init__(self):
        self.id_iteration = itertools.count()
        self.list_traits = {}
    def print_trait_info(self):
        for i in self.list_traits:
            #print(self.list_traits)
            print('Number:',i+1)
            print('Trait:',self.list_traits[i]['Trait'])
            print('Description:',self.list_traits[i]['Description'],'\n')
    def add_to_list(self):
        id = next(self.id_iteration)
        self.list_traits[id] =({'Trait': input('Enter Trait:'),'Description': input('Enter Description:')})
if __name__ == "__main__":
    c1 = DeveloperTraits()
    c1.add_to_list()
    c1.add_to_list()
    c1.add_to_list()
    c1.print_trait_info()
