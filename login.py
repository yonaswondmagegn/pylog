user={}

def page_choice():
    while True:
        page =input("enter l for login and s for sighn up:>")
        if not page:
            print('please enter some thing')
            continue   
        
        if page =='l' or page =='s':
            return page
            break
        if page !='l' or page !='s':
            print('l or s')
            continue


def name_validator():
    while True:
        name = input('enter your name')
        if name.isalpha():
            return name
            break
        if name =='':
            print('pleaser enter something ')
            continue
        else:
            print('numric value not allowed in user name')
            continue
        break


def password_validator():
    while True:
        password = input('password:')
        if not password:
            print('please enter some thing in password feild')
            continue
        if len(password) < 6:
            print('the password must be grater thatn sic charachters')
            continue
        else:
            return password
            break
def login():
    name =name_validator()
    password =password_validator()
    if name in user and user[name]==password:
        print('you are in the page congra')
        
    else:
        print('the uder does not exist')
       
    

def sighnin():
    while True:
        name =name_validator()
        password =password_validator()
        if name in user and user[name]==password:
            print('the user allreadu exist')
            continue
        else:
            user[name]=password
            break
    print(user)




for i in range(10):
    if page_choice() =='l':
        login()
    else:
        sighnin()





