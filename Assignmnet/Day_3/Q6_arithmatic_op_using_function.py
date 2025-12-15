def calulate(num1,num2,fun):
    result =fun(num1,num2)
    return result
    
def add(num1,num2):
    return num1+num2
    
def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2
    
def div(num1,num2):
    return num1/num2
    
num1 = int(input("enter 1st no:"))  
num2 = int(input("enter 2nd no:"))  

while(1):
    choice = int(input("1]add 2] sub 3] mul 4]div = "))

    match choice:
            case 1:
                print(calulate(num1,num2,add))
            case 2:
                print(calulate(num1,num2,sub))
            case 3:
                print(calulate(num1,num2,mul))
            case 4:
                print(calulate(num1,num2,div))
            case _:
                print("invalid choice!")
                