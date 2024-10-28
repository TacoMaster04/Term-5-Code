# arithamtic operation

print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)

x = 10
x = x + 3     # x += 3
print(x)

x = 10
x = x - 3     # x -= 3
print(x)


x = (10 + 3) *2 **2
print(x)

#operation precedence
#parenthesis
#exponentiation
# multiplication \ Division
# sum \ subtraction


x = 2.9
print(round(x))

x = -2.9
print(abs(x))


first = float(input("Enter first number"))
operator =input("")
second= float(input("Enter second number"))

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


#If Conditions
if 5 > 2:
	print("yes")
else:
	print("no")


age = int(input("Enter your age"))

if age < 18:
	print("You are not allowed")
else:
	print("welcome")

food = input("Would you like food (Y/N)")

if food == "Y":
	print("Have some food")
else:
	print("no food for you")

#1 If it is hot -----> Drink Plenty of water
# If it is cold -----> Wear a jacket
#3 Otherwise ------> It's a lovely day

is_hot= True
is_cold = True

if is_hot:
	print("Drink plenty of water")
elif is_cold:
	print("Wear a jacket")
else:
	print("Its a lovely day")