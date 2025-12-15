def add(num1,num2):
    print(num1+num2)
    
def sub(num1,num2):
    print(num1-num2)

def mul(num1,num2):
    print(num1*num2)
    
def div(num1,num2):
    print(num1/num2)
    
num1 = int(input("enter 1st no:"))  
num2 = int(input("enter 2nd no:"))  

while(1):
    choice = int(input("1]add 2] sub 3] mul 4]div = "))

    match choice:
            case 1:
                add(num1,num2)
            case 2:
                sub(num1,num2)
            case 3:
                mul(num1,num2)
            case 4:
                 div(num1,num2)
            case _:
                print("invalid choice!")