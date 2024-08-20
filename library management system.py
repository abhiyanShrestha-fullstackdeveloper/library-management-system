############################################
# Register

def register():
    print('Library Management System')
    print('Register')
    username = input('Enter Username: ')
    password = input('Enter New Password: ')
    usertype = input('Enter Usertype(Superadmin or Manager): ')
    
    with open('userdata.txt','a') as f:
        print(f'{username},{password},{usertype}\n')
        print('Registration Successful')

############################################
# Login
def login():
    print('Library Management System')
    print('Login')
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

############################################
# Add Books

def add_books():
    bookname = input('Enter Book Name: ')
    bookcategory = input('Enter Book Category: ')
    bookdescription = input('Enter Book Description: ')
    bookauthor = input('Enter Book Author Name: ')
    bookprice = int(input('Enter Book Price: '))
    
    with open('bookslist.txt','a') as f:
        f.write(f'{bookname},{bookcategory},{bookdescription},{bookauthor},{bookprice}\n')
        print('Book Added Successfully in System')

############################################
# View Book List

def view_booklist():
    try:
        with open('bookslist.txt','r') as f:
            print('Book Name\t\tBook Category\t\tBook Description\t\tBook Author\t\tBook Price')
            for line in f:
                try:
                    book_name,book_category,book_description,book_author,book_price = line.strip().split(',')
                    print(f'{book_name},{book_category},{book_description},{book_author},{book_price}\n')
                except ValueError:
                    print('Invalid Data!')
    except FileNotFoundError:
        print('File Not Found!')

############################################
# Book For Rent
                    
            
###########################################
# Main Program
def main():
    while True:
        print('Library Management System')
        print('Choices')
        Choice = input('1.Login\t\tq.Quit: ')
        
        if Choice == '1':
            usertype = login()
            
            if usertype:
                if usertype == 'superadmin':
                    while True:
                        Choice = input('1.Book List 2.Add Books 3.Book For Rent 4. Delete Book List 5. Add User q.Logout: ')
                        
                        if Choice == '1':
                            view_booklist()
                        
                        elif Choice == '2':
                            add_books()
                        
                        elif Choice == '3':
                            book_forrent()
                        
                        elif Choice == '4':
                            delete_booklist()
                        
                        elif Choice == '5':
                            register()
                        
                        elif Choice == 'q':
                            break
                        else:
                            print('Invalid Choice!')
                else:
                    while True:
                        Choice == input('1.Book List 2. Add Books 3. Book For Rent q. Logout: ')
                        
                        if Choice == '1':
                            view_booklist()
                        
                        elif Choice == '2':
                            add_books()
                        
                        elif Choice == '3':
                            book_forrent()
                        
                        elif Choice == 'q':
                            break
                        
                        else:
                            print('Invalid Choice!')
                            
        
        elif Choice == 'q':
            break
        
        else:
            print('Invalid Input!')
        
            
main()   