#function to add two numbers 
def add(num1,num2):
    return num1 + num2

#function to subtract two numbers
def sub(num1,num2):
    return num1 - num2

#function to multiply two numbers
def multiply(num1,num2):
    return num1 * num2

#function to divide two numbers
def divide(num1,num2):
    return num1 / num2

#function to multiply two numbers
def avg(num1,num2): 
    return num1 + num2

#uer input
print("Please select a operation:\n " \
      "1. Addition\n" \
      "2. Subtraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n")

Select = int(input("Select a option from 1,2,3,4,5: "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

#Print the result

if Select == 1:
    print("sum of two numbers is: ",  
          add(number1, number2))
    
elif Select == 2:
    print("sub of two numbers is: ",  
          sub(number1, number2))
    
elif Select == 3:
    print("multiply of two numbers is: ",  
          multiply(number1, number2))
    
elif Select == 4:
    print("division of two numbers is: ",  
          divide(number1, number2))
    
elif Select == 5:
    print("average of two numbers is: ",  
          avg(number1, number2))

else: 
    print("invalid operation! pls select again!")
    
    
    
        