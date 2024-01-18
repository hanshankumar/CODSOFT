def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "zero cannot Divide by Zero"
def modulus(a,b):
    return a % b
def exp(a,b):
    return a**b
def floor_div(a,b):
    return a//b

def calculator():
    print("Simple Calculator\n1.Addtion\n2.Subtraction\n3.Multiplication\n4.Division\n5.modulus\n6.Exponential")
    print("7.Floor Division")
   
    choice = input("Enter choice from(1,2,3,4,5,6,7): ")

    if choice in ('1', '2', '3', '4','5','6','7'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            result = addition(num1, num2)
            operation = 'Addition'
        elif choice == '2':
            result = subtraction(num1, num2)
            operation = 'Subtraction'
        elif choice == '3':
            result = multiplication(num1, num2)
            operation = 'Multiplication'
        elif choice == '4':
            result = division(num1, num2)
            operation = 'Divison'
        elif choice=='5':
            result=modulus(num1,num2)
            operation='Modulus'
        elif choice=='6':
            result=exp(num1,num2)
            operation='Power'
        elif choice=='7':
            result=floor_div(num1,num2)
            operation='Floor Divison'   

    

        print("The "f"{operation } ""of" f" {num1}" " and" f" {num2}" " is" f" {result}")
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5/6/7).")

if __name__ == "__main__":
    calculator()
