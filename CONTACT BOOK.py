print("-----CONTACT -- BOOK ------")
print("THIS CONTACT BOOK CAN DO DIFFRENT OPERATIONS ON THE BASIS OF YOUR CHOICE")
print("DO YOU WANT TO CONTINUE\n 1.YES\n 2.NO")
choice=int(input())
contact={}
def display():
    print("Name [contact number, email, address]")
    for key in contact:
        print(key,contact.get(key))
if choice==1:
    ch=1
    while ch==1:
        print("WHAT OPERATION DO YOU WANT TO PERFORM ON THE CONTACT BOOK\n 1. ADD NEW CONTACT\n 2.DISPLAY CONTACT LIST\n 3.SEARCH CONTACT\n 4.UPDATE CONTACT\n 5.DELETE CONTACT")
        op=int(input())
        if op==1:
            name=input("enter the contact name")
            phone=input("enter the phone number")
            email=input("enter the email address")
            address=input("enter the address")
            contact[name]=[phone,email,address]
        elif op==2:
            if not contact:
                print("empty contact book")
            else:
                display()
        elif op==3:
            search=input("enter the name to be searched")
            if search in contact:
                print(search,"the details are",contact[search])
            else:
                print("name is not found in the contact book")
        elif op==4:
            edit=input("enter the name of the contact to be updated")
            e=1
            while e==1:
                print("WHICH DETAIL DO YOU WANT TO UPDATE")
                print("1. contact number\n 2. email address\n 3. address")
                n=int(input())
                if n==1:
                    contactno=input("enter new contact number")
                    contact[edit][0]=contactno
                    print("contact updated")
                    display()
                elif n==2:
                    emails=input("enter new email")
                    contact[edit][1]=emails
                    print("contact updated")
                    display()
                elif n==3:
                    ad=input("enter new address")
                    contact[edit][2]=ad
                    print("contact updated")
                    display()
                else:
                    print("enter the valid data")
                print("DO YOU WANT TO MAKE MORE UPDATES\n 1.YES\n 2.NO")
                e=int(input())
        elif op==5:
            delete=input("enter the contact to be deleted")
            if delete in contact:
                conf=input("DO YOU WANT TO DELETE THIS CONTACT y/n")
                if conf=='y' or conf=='Y':
                    contact.pop(delete)
                display()
            else:
                print("name is not in contact book")
        else:
            break
        print("do you want to continue")
        print("1.YES\n 2.NO")
        ch=int(input())
        if ch==2:
            print("THANKYOU")
                
            
                
                
                
                
            
            
            
