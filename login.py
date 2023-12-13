from csv import DictWriter,DictReader
with open("login.py","r",newline="") as db:
    dbReader = list(DictReader(db))
    def sign_up():
        username=input('\nEnter your username: ')
        for i in username:
            if i==" ":
                print("\nNo space allowed")
        while True:
            gmail=input('Enter your Gmail: ')
            if gmail[-10:]=="@gmail.com":
                break
            else:
                print('Invalid Gmail')

        while True:
            try:
                ph_num=int(input('Enter your phone number: +91 '))
                if len(str(ph_num))==10:
                    break
                else:
                    print('Invalid phone number')
            except ValueError as e:
                print(e)
        capital=[chr(65+i) for i in range(26)]
        symbol=[chr(33+i) for i in range(15)]
        num=[str(i) for i in range(9)]
        while True:
            password=input('\nEnter password: ')
            if len(password)>=8:
                ifcap=[]
                for i in password:
                    if i in capital:
                        ifcap.append(True)
                    else:
                        ifcap.append(False)
                ifnum=[]
                for i in password:
                    if i in num:
                        ifnum.append(True)
                    else:
                        ifnum.append(False)
                ifsym=[]
                for i in password:
                    if i in symbol:
                        ifsym.append(True)
                    else:
                        ifsym.append(False)
                ifnum=sorted(ifnum,reverse=True)
                ifcap=sorted(ifcap,reverse=True)
                ifsym=sorted(ifsym,reverse=True)
                if (ifnum[0]&ifcap[0]&ifsym[0])==True:
                    while True:
                        confirm=input('\nconfirm password: ')
                        if confirm==password:
                            print("\nAccount created successfully")
                            break
                break    

        with open("login.csv","a") as db:
            headers = DictWriter(db,fieldnames=["username","gmail","ph_num","password"])
            # headers.writeheader()  
            headers.writerow({
                "username":username,
                "gmail":gmail,
                "ph_num":ph_num,
                "password":password
            })
    def sign_in():
        ph_num = input("Enter ph no.: ")
        for i in dbReader:
            if int(i["ph_num"]) == ph_num:
                password = input("Enter password: ")
                if i["password"] == password:
                    print("<<<<WELCOME>>>>")
            else:
                print("invalid ID or Password")


def loadpage():
    while True:
        try:
            choice=int(input('1.sign-up\n2.sign-in\n$'))
            if choice==1:
                sign_up()
            elif choice==2:
                sign_in()
            break
        except ValueError as e:
            print(e)




loadpage()                        



