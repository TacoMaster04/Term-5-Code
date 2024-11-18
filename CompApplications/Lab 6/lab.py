num1 = int(input("Enter a number to muliply: "))
num2 = int(input("Enter another number to muliply: "))
print(num1 * num2)

print("===============================", end="\n\n")

a = int(input("Enter a number to check which is greater: "))
b = int(input("Enter another number to check which is greater: "))

if a > b:
	print(a, "is greater than", b)
else:
	print(b, "is greater than", a)
 
print("===============================", end="\n\n")

input1 = input("Enter input 1 to check equality: ")
input2 = input("Enter input 2 to check equality: ")

if input1 == input2:
	print("The inputs are the same.")
else:
	print("The inputs are different.")
 
print("===============================", end="\n\n")

first = int(input("Enter first number for calculator: "))
operator = input("Pick an operator (+, -, /, *): ")
second = int(input("Enter second number for calculator: "))

if operator == "+":
	print(first + second )
elif operator =="-":
	print(first - second)
elif operator == "*":
	print(first * second)
elif operator == "/":
	print(first / second)
else:
	print("error")
 
print("===============================", end="\n\n")

listOfNumbers = [10, 20, 33, 46, 55]

for number in listOfNumbers:
	if number % 5 == 0:
		print(number, "is divisible by 5")

print("===============================", end="\n\n")

listOfNumbersCondition = [12, 75, 150, 180, 145, 525, 50]

for number in listOfNumbersCondition:
    if number > 500:
        break
    elif number > 150:
        continue
    elif number % 5 == 0:
        print(number, "is divisible by 5")

print("===============================", end="\n\n")

def maxOfNumbers(a, b, c):
	print("The maximum number is: ", max(a, b, c))

maxOfNumbers(30, 22, 18)

print("===============================", end="\n\n")

def isEven(number):
	if number % 2 == 0:
		print(number, "is even")
	else:
		print(number, "is odd")
  
isEven(10)