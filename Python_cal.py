operator = input("Enter an operator")
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))


if operator == "+":
    result = num1 + num2

    print(result)

elif operator == "-" :
    result = num2 - num1
    print(result)

elif operator == "*":
    result = num1 * num2
    print(result)

elif operator == "/":

 result = num2 // num1
 print(result)

else:
   print(f"{operator} is not a valid operator")