import sys
user_list = {}
class Add_UserAccount():

    def __init__(self,account_open_balance = 0.00):
        self.account_open_balance = float(account_open_balance)
        print('Opening A New Account')
        if self.account_open_balance < 200:
            print('$200.00 minimum is required to open a new account')
            self.account_open_balance = float(input('Select a new amount to add to your balance:\n'))
        if self.account_open_balance < 200:
            print('Not enough funds to open account. Request has been denied')
            sys.exit()
        while True:
            self.username = input('Enter the UserName:')
            if self.username in user_list:
                print('UserName already Exists. Please Enter another')
                continue
            else:
                break
        while True:
            self.pin = input('Enter your new PIN:')
            self.pin_validation = input('Re-Enter the same PIN:')
            if self.pin != self.pin_validation:
                continue
            else:
                break
        user_list[self.username] = self.pin,self.account_open_balance


class ATM_Actions(object):
    def __init__(self):
        self.balance = 0.00
        self.name = ''
    def user_validation(self):
        current_username = input('Enter your UserName:')
        if current_username in user_list:
            self.name = current_username
            current_pin = input('Enter your PIN:')
            print(user_list[current_username][0])
            if user_list[current_username][0] != current_pin:
                print('Invalid PIN')
                return False
            else:
                print('UserName and Pin Accepted')
                return True
        else:
            print('UserName not found')
            return False
    def account_balance(self):
        #print(user_list[self.name][2])
        if user_list[self.name][1] == 0.00 or user_list[self.name][1] == 0:
            print('No funds account is being closed')
        else:
            print('Balance:',user_list[self.name][1])

if __name__ == "__main__":
    c1 = Add_UserAccount()
    #Print UserList
    #print(user_list)
    #c2 = Add_UserAccount()
    #Print UserList
    #print(user_list)
    #Account Balance
    #print(user_list['Zach'][1])
    #Pin Number
    #print(user_list['Zach'][0])
    c3= ATM_Actions()
    print('Start ATM Actions')
    val_iteration = 0
    while True:
        if val_iteration >=3:
            print('Multiple Invalid attempts - Please Try Again Later')
            sys.exit()
        if c3.user_validation():
            break
        val_iteration += 1
    print('Return Account Balance')
    c3.account_balance()
