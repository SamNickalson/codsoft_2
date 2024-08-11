
#Task-2 To Create An Simple Calculator 



def calc():
    while True:
        a=int(input("enter any no:"))
        b=int(input("enter the second no:"))
        c=input("enter the calculation type:")

        if c.casefold()=="addition":
            print(a+b)
        elif c.casefold()=="subtraction":
            print(a-b)
        elif c.casefold()=="multiplication":
            print(a*b)
        elif c.casefold()=="division":
            print(a/b)
        else:
            print("invalid input")


        x=input("do you want to stop:")
         
        if x.casefold()=="yes":
            break
        else:
            continue
calc()
