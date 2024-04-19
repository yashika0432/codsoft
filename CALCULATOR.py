print("----CALCULATOR----")
print("ENTER ALL ASKED VALUES IN NUMBERS/INTEGERS")
ch=1
while ch==1:
    print("WHICH OPERATION DO YOU WANT TO PERFORM")
    print("1. ADDITION")
    print("2. SUBSTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. SQUARE\n"
           "6. CUBE\n"
          "7. SQUARE ROOT\n")
    
    op=int(input())
    if op==1:
        num1=int(input("ENTER THE FIRST VALUE YOU WANT TO PERFORM THE OPERATION UPON"))
        num2=int(input("ENTER THE SECOND VALUE YOU WANT TO PERFORM THE OPERATIONS UPON"))
        s=num1+num2
        print("SUM IS",s)
    elif op==2:
        num1=int(input("ENTER THE FIRST VALUE YOU WANT TO PERFORM THE OPERATION UPON"))
        num2=int(input("ENTER THE SECOND VALUE YOU WANT TO PERFORM THE OPERATIONS UPON"))
        sub=num1-num2
        print("DIFFERENCE IS",sub)
    elif op==3:
        num1=int(input("ENTER THE FIRST VALUE YOU WANT TO PERFORM THE OPERATION UPON"))
        num2=int(input("ENTER THE SECOND VALUE YOU WANT TO PERFORM THE OPERATIONS UPON"))
        m=num1*num2
        print("PRODUCT IS",m)
    elif op==4:
        num1=int(input("ENTER THE FIRST VALUE YOU WANT TO PERFORM THE OPERATION UPON"))
        num2=int(input("ENTER THE SECOND VALUE YOU WANT TO PERFORM THE OPERATIONS UPON"))
        d=num1/num2
        print("QOUTIENT IS",d)
    elif op==5:
        num1=int(input("ENTER THE VALUE YOU WANT TO PERFORM THE OPERATION UPON"))
        sq=num1**2
        print("SQUARE IS",sq)
    elif op==6:
        num1=int(input("ENTER THE VALUE YOU WANT TO PERFORM THE OPERATION UPON"))
        cu=num1**3
        print("CUBE IS",cu)
    elif op==7:
        import math
        num=int(input("ENTER THE VALUE YOU WANT TO PERFORM THE OPERATION UPON"))
        root=math.sqrt(num)
        print("ROOT IS",root)
    else:
        print("INVALID INPUT")
    print("DO YOU WANT TO CONTINUE THE OPERATIONS\n"
          "1. YES\n"
          "2. NO\n")
    ch=int(input())
    if ch==2:
        print("THANKYOU")
        
    
        

