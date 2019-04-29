import sqlite3
import getpass
import os
import sys

sql = sqlite3.connect('agencias.db')
comandos_sql = sql.cursor()

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5,
}

if os.path.getsize ('agencias.db') > 100:
    print('Tabela existe [ OK ]')
else:
    comandos_sql.execute("""
        CREATE TABLE agencias (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        agency VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL,
        name VARCHAR(20) NOT NULL,
        value VARCHAR(20) NOT NULL,
        admin VARCHAR(5) NOT NULL
);
""")


#    {
#            'agency': '4789-3',
#            'password': '123456',
#            'name': 'Fellipe Popoviche',
#            'value': 1500,
#            'admin': True
#        },
#        {
#            'agency': '1234-5', 
#            'password': '654321',
#            'name': 'João silva',
#            'value': 450,
#            'admin': False
#        }

    usuarios =[
     ( '4789-3', '123456', 'Fellipe Popoviche', '1500', 'True'),
     ('1234-5', '654321', 'João silva', '450', 'False')
    ]

    comandos_sql.executemany("""
INSERT INTO agencias (agency, password, name, value, admin)
VALUES (?, ?, ?, ?, ?)
""", usuarios)

    sql.commit()

    print('Tabelas criada com sucesso.')

while True:
    print("**************************************")
    print("***     Cash Machine - Fellipe     ***")
    print("**************************************")

    account_typed = input("enter your account: ")
    password_typed = getpass.getpass("enter your password: ")

    comandos_sql.execute('SELECT * FROM agencias WHERE agency=?',  (account_typed,))

    resultado =  comandos_sql.fetchone()

    flag = False
    
    if resultado == None:
        flag = True    
    else:
       if password_typed == resultado[2]:
           os.system('cls' if os.name == 'nt' else 'clear')

           print("                                      ")
           print("**************************************")
           print("***     Cash Machine - Fellipe     ***")
           print("**************************************")
           print("                                      ")
           print("1 - Bank balance")
           print("2 - Cash out")

           option_typed = input('Choose an option: ')

           if option_typed == '1':
               print('Your balance: $%s' % resultado[4])
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


           input("Press <enter> to continue: ") #PAUSE PROGRAMM 
           sql.close()   
           sys.exit()   
       else:
           flag = True 

    if flag == True:
        print("Invalid account")  
        input("Press <enter> to continue: ") #PAUSE PROGRAMM       
        os.system('cls' if os.name == 'nt' else 'clear')

sql.close()        
