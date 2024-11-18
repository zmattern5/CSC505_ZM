import inflect
import datetime
amount_in_words = ''
class CheckCreation:
    def amount_as_text(self,num_check_amount):
        global amount_in_words
        e = inflect.engine()
        amount_in_words = e.number_to_words(num_check_amount)
        if ' and' in amount_in_words:
            amount_in_words = amount_in_words.replace(' and','')
        if 'point' in amount_in_words:
            amount_in_words = amount_in_words.replace('point','and')
    def format_check(self,currentDate,payTo,amount_in_words,memo,numAmount,address):
        print(address,'     ',currentDate)
        print('Pay to the Order of:',payTo,'    $',f'{numAmount:.2f}')
        print(amount_in_words,'dollars')
        print('Memo:',memo,'    ','Signature: ________',)


if __name__ == "__main__":
    c1 = CheckCreation()
    #Get User Information
    #Save Check Amount
    num_check_amount = float(input('Enter the amount for the check:'))
    #Save Address
    address = input('Enter your address:')
    #Save Payee Information
    payTo = input('Enter who the payment is to:')
    #Save Current Date
    currentDate = str(datetime.datetime.today()).split()[0]
    #Save Memo
    memo = input('Enter memo:')
    print('')
    #Convert  Amount to Words
    c1.amount_as_text(num_check_amount)
    #Enter Details into Check Format & Print
    c1.format_check(currentDate,payTo,amount_in_words,memo,num_check_amount,address)
