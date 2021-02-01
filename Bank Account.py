#Welcome to the Bank Account Program

class BankAccount():
    def __init__(self):
        self.ownerName = 'Annahari'
        self.balance = 0
    def deposit(self):
        Amount = float(input('Enter depositing balance : '))
        #print('Amount is deposited successfully : ',Amount)
        self.balance += Amount
    def withdraw(self):
        Amount = float(input('Enter how much draw your money : '))
        if self.balance>=Amount:
            self.balance -= Amount
            #print('withdraw Amount',Amount)
        else:
            print('Insufficient balance')

print("<----Welcome to the Bank Account---->")
bank = BankAccount()
print('Account Holder Name : ',bank.ownerName)
print('Initial Account Balance : ',bank.balance)
print()
bank.deposit()
bank.withdraw()
print('Net Available Balance : ',bank.balance)


'''
while True:
    print('<---Welcome to the Bank Account Progaram--->\n')
    Acc = BankAccount()
    print('Account Holder Name: ', Acc.ownerName)
    print('1.showBalance \t 2.Deposit \t 3.Withdraw \t 4.Exit')
    opt = int(input('Enter one option in the above options : '))
    if opt == 1:
        print('Bank balance : ',Acc.balance)
        print()
    elif opt == 2:
        print()
        Acc.deposit()
        print()
    elif opt == 3:
        Acc.withdraw()
        print()
    elif opt == 4:
        break
    else:
        print()
        print('Please Choose the options from 1 to 4 only\n')
'''