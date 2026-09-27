balance = 5000
count = 0
history = []
pin = int(input('Enter your pin:'))
if pin == 1234:
    print('Login Successfull')
    while True:
        print('\n1. Check balance')
        print('2. Deposit Money')
        print('3. Withdraw Money')
        print('4. Transaction history')
        print('5. Transaction count')
        print('6. Exit')
        choice = int(input('Enter your choice:'))
        if choice == 1:
            print('Your current balance is:',balance)
        elif choice == 2:
            amount = float(input('Enter deposit amount:'))
            if amount >  0:
                balance = balance + amount
                count = count + 1
                history.append('Deposited' +' '+ str(amount))
                print('Money deposited successfully')
            else:
                print('Invalid amount!')
        elif choice == 3:
            amount = float(input('Enter withdraw money:'))
            if amount > 0 and balance >= amount:
                balance = balance - amount
                count = count + 1
                history.append('Withdrawn' +' '+ str(amount))
                print('Money withdrawn successfully')
            else:
                print('Invalid amount or insufficient balance!')
        elif choice == 4:
            if len(history) == 0:
                print('No transactions yet')
            else:
                print('Transaction history:')
                for i in history:
                    print(i)
        elif choice == 5:
            print('Total transaction count:',count)
        elif choice == 6:
            print('Thank you for using the bank')
            break
        else:
            print('Invalid choice!')
else:
    print('Wrong PIN!')
