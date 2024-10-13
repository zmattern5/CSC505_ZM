import random
class dice_generator:
    def __init__(self):
        self.first_number = 1
        self.second_number = 6
    def generate_number(self,first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number
        print(random.randint(self.first_number,self.second_number))


if __name__ == "__main__":
    while True:
        temp_class = dice_generator()
        first_number = int(input("Enter first number:"))
        second_number = int(input("Enter second number:"))
        temp_class.generate_number(first_number,second_number)
        str_continue = (input("Enter 'Y' to generate another number:"))
        if str_continue != 'Y':
            break
