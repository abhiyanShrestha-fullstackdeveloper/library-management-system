############################################
# Register

def register():
    username = input('Enter Username: ')
    password = input('Enter New Password: ')
    usertype = input('Enter Usertype(Superadmin or Manager): ')
    
    with open('userdata.txt','a') as f:
        print(f'{username},{password},{usertype}\n')
        print('Registration Successful')


def login():
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    
    with open('userdata.txt','r') as f:
        for line in f:
            user_name,user_password,usertype = line.strip().split(',')
            if user_name == username and user_password == password:
                return usertype
            print('Welcome to Our Library Management System')
        else:
            print('Username or Password is wrong!')
            

while True:
    Choice = input('1.register\t\t2.login\t\tq.quit: ')
    
    if Choice == '1':
        register()
        
    elif Choice == '2':
        login()
    
    elif Choice == 'q':
        break
    
    else:
        print('Invalid Input!')
        
    