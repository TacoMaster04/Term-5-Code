
#print() function:
#print() function prints the message to the screen
#You can pass variables, strings, numbers, or other data types as one or more parameters when using the print() function.

#Examples:
print ("Hello World")         #string            #you can use single or double quotations
print(4)                      #integer
print(2.5)                    #float
print(False)                  #boolean                
print(1*10)                   #arithmatic operation

name = "Ahmed"                  
print(name)                   #variable


name = "Ahmed"
age = 30

print("Hello, my name is", name, "and I am", age, "years old.")         #can pass two parameters 

                                     #Python code gets excuted line by line
#SEP PARAMETER                                       

print(1,2,3,4,5)
print(1,2,3,4,5,sep=",")
print('01','12','2023', sep='-')  #for formatting a date 


#END PARAMETER 

print("On the" , end=" ")
print("same line")


#Python Indentation

#Python uses indentation to indicate a block of code, it will give you an error if you skip the indentation

if 10 > 5:
  print("True")

#This Example will result an error as there is no indentation 
#if 10 > 5:
#print("True")


#VARIABLES
#Python has no command for declaring a variable.

#Example 1
course="CAIB"
print(course)                           #output: course


#Example 2
course="CAIB"
course="Web Design"                    
print(course)                           #output: Web Design                      #python excutes code line by line


#Variable names are case-sensitive.
name="Ehdaa"
Name="Rowan"

print(name)
print(Name)

# Illegal variable names:

# 1myvar       #A variable name cannot start with a number
# my-var       #A variable name can only contain alpha-numeric characters and underscores
# my var       #No spaces


#Many Values to Multiple Variables
x,y,z = "CAIB" , "MultiMedia", "WebDesign"
print(x)
print(y)
print(z)

#LIST
courses = ["CAIB", "MultiMedia", "WebDesign"]
x, y, z = courses
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "CAIB"
print(x)
print(y)
print(z)

#CASTING
x = str(10)    # x will be '10'
y = int(10)    # y will be 10
z = float(10)  # z will be 10.0


#You can get the data type of a variable with the "type()"" function.
x = 5
y = 5.0
z = "John"
print(type(x))
print(type(y))
print(type(z))


#Recieving input
name= input ("What's your name")
print("hi", name)