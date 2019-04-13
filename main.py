import getpass
import os

accounts_list = [
        {
            'agency': '4789-3',
            'password': '123456',
            'name': 'Fellipe Popoviche',
            'value': 1500,
            'admin': True
        },
        {
            'agency': '1234-5', 
            'password': '654321',
            'name': 'João silva',
            'value': 450,
            'admin': False
        }
    ]

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5,
}

while True:
    print("**************************************")
    print("***     Cash Machine - Fellipe     ***")
    print("**************************************")

    account_typed = input("enter your account: ")
    password_typed = getpass.getpass("enter your password: ")

    ### method w/ dicionaries

    ## agency, password, name, value

    #accounts_list = {
    #    '4789-3': {
    #        'password': '123456',
    #        'name': 'Fellipe Popoviche',
    #        'value': 0
    #    },
    #    '1234-5': {
    #        'password': '654321',
    #        'name': 'João silva',
    #        'value': 0
    #    }
    #}

    #if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
    #    print("Valid account " + "\n" + "Your account: " + account_typed + "\n" + "Your password: " + password_typed
    #        + "\n" + "Your name: " + accounts_list[account_typed]['name'])
    #else: 
    #    print('Invalid account')    

    flag = False
    for account in accounts_list:
        if account_typed == account['agency'] and password_typed == account['password']:
            os.system('cls' if os.name == 'nt' else 'clear')
            flag = True

            print("                                      ")
            print("**************************************")
            print("***     Cash Machine - Fellipe     ***")
            print("**************************************")
            print("                                      ")
            print("1 - Bank balance")
            print("2 - Cash out")
            if account['admin']:
                print("10 - Include banknotes")
            option_typed = input('Choose an option: ')

            if option_typed == '1':
                print('Your balance: $%s' % account['value'])
            elif option_typed == '10' and account['admin']:
                amount_typed = input('Type the quantity of banknotes: ')
                banknote_typed = input('Type the banknote to be include: $')
                #money_slips[banknote_typed] = money_slips[banknote_typed] + int(amount_typed) 
                money_slips[banknote_typed] += int(amount_typed)
                print(money_slips)
            elif option_typed == '2':
                value_typed = input('Enter the amount to be withdrawn: $')

                money_slips_user = {}
                value_int = int(value_typed)

                if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                    money_slips_user['100'] = value_int // 100
                    value_int = value_int - value_int // 100 * 100

                if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                    money_slips_user['50'] = value_int // 50
                    value_int = value_int - value_int // 50 * 50

                if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                    money_slips_user['20'] = value_int // 20
                    value_int = value_int - value_int // 20 * 20       

                if value_int != 0:
                    print("The bank doesn't have banknotes for this amount ")
                else: 
                    for money_bill in money_slips_user:
                        money_slips[money_bill] -= money_slips_user[money_bill]
                    print('Take banknotes')
                    print(money_slips_user)    

    if not flag:
        print("Invalid account")  

    input("Press <enter> to continue: ") #PAUSE PROGRAMM       
    os.system('cls' if os.name == 'nt' else 'clear')