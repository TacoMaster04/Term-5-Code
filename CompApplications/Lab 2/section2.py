#Example (Recieving input)

birth_year = int(input("Birth year: "))                                  #TYPE CONVERSION "str" ---> "int"      "2000" ---> 2000
age = 2024 - birth_year
print(age)


#Type-Casting / Type-Conversion = process of converting a value of one data type to another (string-float-integer-boolean)
#Example 

name="Mohamed"
age = 22
gpa = 3.9
student = True

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

student =str(student)
print(student)
print(type(student))


#Example 2 (Reciveing input) Ask the user their weight in pounds, convert it to kilograms and print it on the terminal 

weight_lbs = int(input("Weight (lbs) : "))
weight_kg = weight_lbs * 0.45 

print(weight_kg)


                                             #-------------------------------------------------#

#STRINGS
#Strings in python are surrounded by either single quotation marks, or double quotation marks.

print("Hello")   
print('Hello')

name= ("What's your name")             #Quotes Inside Quotes


#Multi-line Strings

email = ''' Dear HR,
Lorem ipsum dolor sit amet
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(email)

#Strings are Arrays
course = "Computer Applications In Business"
         #01234-----------------
print(course[0])             #remember that the first character has the position 0
print(course[-1])            #index of the last character 
print(course[-2])
print(course[0:4])           #will return all the characters from index 0 till 4 but won't return the index of 4 
print(course[0:])            #return all the characters to the end of the string
print(course[9:])
print(course[:9])            #python will assume 0 as the start index
print(course[:])             #return all the characters of the string


#Example 
name="Mohammed"
print(name[1:-1])


#String Methods 
#upper()                     #The upper() method returns the string in upper case
greeting = "Welcome!"
print(greeting.upper())

#lower()                     #The lower() method returns the string in lower case
greeting = "Welcome!"
print(greeting.lower())

#capitalize()                #Converts the first character to upper case
greeting = "welcome!"
print(greeting.lower())

#strip()                     #strip() method removes any whitespace from the beginning or the end
greeting = " Welcome!"
print(greeting.strip())

#replace                     #replace() method replaces a string with another string
course = "Welcome to CAIB Course"
print(course.replace("to", "2"))        

#len                         #the len() function returns the number of characters in the string  
name=input("Enter your full name: ")
print(len(name))

#find                        #searches the string for a specified value and returns the index of where it was found
name=input("Enter your full name: ")
print(name.find("E"))                                                        #-1 ----> Error

#count()	                #Returns the number of times a specified value occurs in a string
name=input("Enter your full name: ")
print(name.count("a"))

#isdigit()	                 #Returns True if all characters in the string are digits
name=input("Enter your full name: ")
print(name.isdigit())

#isalpha()	                #Returns True if all characters in the string are in the alphabet
name=input("Enter your full name: ")
print(name.isalpha())



#Excercise
#Validate username:
#1 username is no more than 12 charachters 
#2 username must not contain spaces
#username must not contain digits


username = input("Enter username: ")

if len(username) > 12:
    print("username must not be more than 12 characters")
elif not username.find(" ")== -1:
    print("your username can't contain spaces")
elif not username.isalpha():
    print("your username can't contain digits")
else:
    print("welcome" , username)





