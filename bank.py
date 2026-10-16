#program for bank account report
balance=10000
def deposit():
    global balance
    amount=int(input('enter amount of deposit:'))
    balance=balance+amount
    print('account balance is',balance)

def withdraw():
    global balance
    amount=int(input('enter amount to be withdraw:'))
    if amount>balance:
        print('insufficent balance ,try again')
    else:
        balance=balance-amount
        print('account balance is',balance)
#main program

while True:
    print('account transactions')
    print('1.know balance')
    print('2.withdraw')
    print('3.deposit')
    print('4.exit')
    ch=int(input('select your choice [1...4]:'))
    if ch==1:
        print('account balance',balance)
    elif ch==2:
        withdraw()
    elif ch==3:
        deposit()
    elif ch==4:
        break
    else:
        print('invalid choice,try again..')
    
        
