# FOR LOOPS
for y in range (1, 21):
		print(y)

for y in range (1, 21):
	if y == 13:
		continue #Skip
	else:
		print(y)

for y in range (1, 21):
	if y == 13:
		break #Stop at 12
	else:
		print(y)

for y in range (3):
	print("Attempt")

#WHILE LOOP
i = 1
while(i <=10):
	print(i)
	i+=1

name = input("Enter your name: ")
while name == "":
	print("You didnt enter your name!")
	name = input("Enter your name again: ")
else:
	print("Hello", name)

num = int(input("Enter the number between 1-10: "))
while num < 1 or num > 10:
	print("Invalid number!")
	num = int(input("Enter the number between 1-10 again: "))
else:
	print("Valid Number", num)

for x in range (3):
	for y in range (1,10):
		print(y, end="")
	print()

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter a symbol: ")

for x in range (rows):
	for y in range (columns):
		print(symbol, end="")
	print()

correct_guess = 5
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
	guess = int(input("Enter a number: "))
	guess_count += 1

	if guess == correct_guess:
		print("You won!")
		break
	else:
		print("You lost")

# Lists, Sets, Tuppels
coursesList = ['History', 'Math', 'Physics', 'CompSci']
print(coursesList)
print(coursesList[0])

coursesSets = {'History', 'Math', 'Physics', 'CompSci'}
print(coursesSets)

coursesTuppels = ('History', 'Math', 'Physics', 'CompSci')
print(coursesTuppels)

# Appending
coursesList.append('Art')
print(coursesList)

courses1 = ['History', 'Math', 'Physics', 'CompSci']
courses2 = ['Art', 'Programing', 'Design']

#Extend
courses1.extend(courses2)
print(courses1)

#Remove
courses1.remove('Math')
print(courses1)

#Sort
nums = [1, 5, 2, 4, 3, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, 30, 20, 15, 25, 0]
nums.sort(reverse=True)
print(nums)

#Clear
nums.clear()
print(nums)

#Count the number of times an element appears in a list
names = ['John', 'Doe', 'Alice', 'Doe', 'Jane', 'Mary', 'Doe', 'Eve', 'Tom', 'Doe']
print(names.count('Doe'))

#Insert
names.insert(1, 'Smith')
print(names)

#Pop
names.pop(5)
print(names)

#Functions
def hello_func():
	print('Hello Function!')
 
hello_func()


def welcome(name, age):
	print(f'Hello {name}, you are {age} years old')
 
welcome('John', 25)


def cube(num):
	return num*num*num

print(cube(3))