num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Enter the operator you want to perform")
ch = input("Enter any of these operator for operation +, -, *, /  ")
result = 0
if ch == '+':
    result = num1+num2
elif ch == '-':
    result = num1-num2
elif ch == '*':
    result = num1*num2
elif ch == '/':
    result = num1/num2
else:
    print("char is not supported")
print(num1, ch, num2, ": ", result)
